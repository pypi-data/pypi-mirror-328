import os
import fabio
import h5py
import pyFAI
from time import time
import numpy as np
from subprocess import Popen
import shutil
import re

from . import handle as hdl
from . import misc as msc
from ..config import data_type
from ..input import integration_parameters

def setup_integration( sample_dir ):
    # read and edit integration_parameters.py
    intpar_path_sample = os.path.join(sample_dir,'integration_parameters.py')
    # check if there is already an integration file
    if not os.path.isfile( intpar_path_sample ):
        intpar_path_module = hdl.get_file_path('textom',os.path.join('input','integration_parameters.py'))
        hdl.open_with_editor(intpar_path_module) # take the one from the textom module
        shutil.copyfile(intpar_path_module, intpar_path_sample ) # copy to the sample diractory
    else:
        msc.cp_add_dt(intpar_path_sample, sample_dir, now=False) # save the old version with modification date
        hdl.open_with_editor(intpar_path_sample) # edit and use the same file
    par = msc.import_module_from_path('integration_parameters', intpar_path_sample)
    print(f'\tSaved integration parameters to {sample_dir}') 

    generate_caked_detector_mask(sample_dir, par)
    return par

def generate_caked_detector_mask(sample_dir, par:integration_parameters):
    os.makedirs(os.path.join( sample_dir, 'analysis'), exist_ok=True)
    path_mask = os.path.join( sample_dir, 'analysis', 'mask_detector_cake.h5' )
    if not os.path.isfile(path_mask):
        # get mask and save its azimutal integration for further analysis
        mask = fabio.open(par.mask_path).data
        ai = pyFAI.load(par.poni_path)
        mask_cake = ai.integrate2d(
            np.ones_like(mask), 
            par.npt_rad, 
            par.npt_azi, 
            radial_range = par.rad_range, 
            azimuth_range = par.azi_range, 
            unit=par.rad_unit,
            method = par.int_method, 
            correctSolidAngle = par.solidangle_correction, 
            mask = mask, 
            safe = False,
        )
        with h5py.File(path_mask, 'w') as hf:
            hf.create_dataset('mask_cake', data = mask_cake.intensity)

def update_filelist( sample_dir, par:integration_parameters ):

    # compile the pattern for name matching
    fid_in = h5py.File( par.path_in, 'r' )
    repattern = '^' + par.h5_proj_pattern.replace('*', '(.*?)') + '$'
    repattern = re.compile(repattern)

    # get all datasets that correspond to the pattern
    filtered_datasets = []
    scan_no = []
    n_integrated, n_missing = 0,0
    for entry in fid_in.keys():
        # Check if the name matches the pattern
        match = repattern.match(entry)
        if match:
            # print(entry)
            # Check if the dataset's data is actually present on the disk
            try:
                h5path_data = f'{entry}/{par.h5_data_path}'
                dataset = fid_in[h5path_data]
                # Attempt to access the dataset's shape (raises Error if the data is missing)
                _ = dataset.shape
            except:
                # print(f"Data for {entry} is missing on the disk.")
                continue  # Skip this entry if data is missing
        
            # Check if the dataset has already been integrated
            todo = False
            if par.mode%2:
                out_path = os.path.join(sample_dir,'data_integrated_1d', entry.split('.')[0]+'_integrate_1d.h5')
                todo = np.logical_or( todo, not os.path.isfile(out_path) )
                n_missing += todo
                n_integrated += not todo
            if par.mode>1:
                out_path = os.path.join(sample_dir,'data_integrated', entry.split('.')[0]+'_integrate_2d.h5')
                todo = np.logical_or( todo, not os.path.isfile(out_path) )
                n_missing += todo
                n_integrated += not todo
            if todo:
                # add the dataset to the integration list
                filtered_datasets.append(entry)
                try:
                    scan_no.append(int(match.group(1)))
                except ValueError:
                    pass
                    # print(f"Failed to extract scan number from entry: {entry}")
    print(f'\tupdated filelist, found {n_integrated} already integrated, {n_missing} to do')
    return fid_in, filtered_datasets

def start_integration_parallel( sample_dir ):
    par = setup_integration(sample_dir)
    print('Starting parallel pyFAI integration')
    t0 = time()
    # start parallel integration in separate processes
    int_path = hdl.get_file_path('textom',os.path.join('src','integration_launcher.py'))
    pids = []
    for k in range(par.n_tasks):
        command = [
            'taskset', '-c', '%d-%d' % (k*par.cores_per_task, (k+1)*par.cores_per_task),
            'python', int_path, 
            '-k', '%d' % (k),
            '-d', '%s' % (sample_dir),
        ]
        p = Popen(command)
        pids.append(p)
    for p in pids: # wait for all to be finished
        p.wait()
    for p in pids: # cleanup (not really necessary)
        p.kill()
    print('Integrations finished, total time: %d s' % (time()-t0))

def start_integration_online( sample_dir ):
    par = setup_integration(sample_dir)
    print('Starting online pyFAI integration')
    t0 = time()
    flat=None
    if isinstance( par.flatfield_correction, str ):
        flat = fabio.open(par.flatfield_correction).data

    mask = fabio.open(par.mask_path).data
    ai = pyFAI.load(par.poni_path)

    fid_in, filtered_datasets = update_filelist( sample_dir, par )
    while len(filtered_datasets) > 0:
        try:
            print(f'\tIntegrating {filtered_datasets[0]}')
            flexible_integrator(sample_dir, fid_in, filtered_datasets[0], par, ai, flat, mask)
        except:
            pass
        fid_in.close()
        fid_in, filtered_datasets = update_filelist( sample_dir, par )
    print('Integrations finished, total time: %d s' % (time()-t0))

def flexible_integrator(sample_dir:str, fid_in, dataset:str, par:integration_parameters, ai, flat, mask):
    
    # get paths for the correct h5 file
    h5path_data = '{}/{}'.format(dataset,par.h5_data_path)
    h5path_ty = '{}/{}'.format(dataset,par.h5_ty_path)
    h5path_tz = '{}/{}'.format(dataset,par.h5_tz_path)
    h5path_tilt = '{}/{}'.format(dataset, par.h5_tilt_angle_path)
    h5path_rot = '{}/{}'.format(dataset, par.h5_rot_angle_path)
    # save metadata for writing
    ty = fid_in[h5path_ty][()]
    tz = fid_in[h5path_tz][()]
    tilt_angle = fid_in[h5path_tilt][()]
    rot_angle = fid_in[h5path_rot][()]
    # this differs depending on scan or controt
    if par.h5_nfast_path:
        h5path_nfast = '{}/{}'.format(dataset,par.h5_nfast_path)
        h5path_nslow = '{}/{}'.format(dataset,par.h5_nslow_path)
        fov = ( fid_in[h5path_nfast][()], fid_in[h5path_nslow][()]  )
    if par.h5_ion_path:
        h5path_ion = '{}/{}'.format(dataset,par.h5_ion_path)
        ion = fid_in[h5path_ion][()]

    #     out_name = '{}_{:03d}_{:03d}_{:.0f}_{:08.2f}_diff_scan_0001_comb'.format(
    #                 par.title,
    #                 scan_no[l],scan_no[l],
    #                 fid_in[h5path_tilt][()],
    #                 fid_in[h5path_rot][()],
    #             ).replace('.','p')
    # else:
    out_name = dataset.split('.')[0]

    data_in = fid_in[h5path_data]
    n_frames = data_in.shape[0]

    if par.mode%2:
        os.makedirs(os.path.join(sample_dir, 'data_integrated_1d/'), exist_ok=True)
        path_out = os.path.join(
            sample_dir, 'data_integrated_1d/',
            out_name + '_integrate_1d.h5'
        )
        fid_out = h5py.File( path_out, 'w' )

        # Write some metadata
        fid_out.create_dataset( 'tilt_angle', data= tilt_angle )
        fid_out.create_dataset( 'rot_angle', data= rot_angle )
        fid_out.create_dataset( 'ty', data= ty )
        fid_out.create_dataset( 'tz', data= tz )
        if par.h5_nfast_path:
            fid_out.create_dataset( 'fov', data=fov )
        if par.h5_ion_path:
            fid_out.create_dataset( 'ion', data=ion )

        radial_dset = fid_out.create_dataset( 'radial_units', (1,par.npt_rad_1D) )
        intensity_dset = fid_out.create_dataset(
            'cake_integ',
            ( n_frames, par.npt_rad_1D ),
            chunks = ( 1, par.npt_rad_1D ),
            shuffle="True", compression="lzf",
            dtype=data_type,
            )

        t0 = time()
        for frame in range (0,n_frames):
            # print(frame)
                
            result1D = ai.integrate1d(
                data_in[frame,:,:], 
                par.npt_rad_1D, 
                radial_range = par.rad_range, 
                unit=par.rad_unit,
                method = par.int_method, 
                correctSolidAngle = par.solidangle_correction, 
                dark = par.darkcurrent_correction,
                flat = flat,
                mask = mask, 
                polarization_factor = par.polarisation_factor, 
                safe = False,
            )

            radial_dset[0,:] = result1D.radial
            intensity_dset[frame,:]= result1D.intensity

            # # Write some metadata
            # fid_out.create_dataset( 'tilt_angle', data= tilt_angle )
            # fid_out.create_dataset( 'rot_angle', data= rot_angle )
            # fid_out.create_dataset( 'ty', data= ty )
            # fid_out.create_dataset( 'tz', data= tz )
            # fid_out.create_dataset( 'fov', data=fov )
            # fid_out.create_dataset( 'ion', data=ion )

        ai.reset()
        fid_out.close()  

    if par.mode>1:
        os.makedirs(os.path.join(sample_dir, 'data_integrated/'), exist_ok=True)
        path_out = os.path.join(
            sample_dir, 'data_integrated/',
            out_name + '_integrate_2d.h5'
        )
        fid_out = h5py.File( path_out, 'w' )

        # Write some metadata
        fid_out.create_dataset( 'tilt_angle', data= tilt_angle )
        fid_out.create_dataset( 'rot_angle', data= rot_angle )
        fid_out.create_dataset( 'ty', data= ty )
        fid_out.create_dataset( 'tz', data= tz )
        if par.h5_nfast_path:
            fid_out.create_dataset( 'fov', data=fov )
        if par.h5_ion_path:
            fid_out.create_dataset( 'ion', data=ion )

        radial_dset = fid_out.create_dataset( 'radial_units', (1,par.npt_rad) )
        azimuthal_dset = fid_out.create_dataset( 'azimuthal_units', (1,par.npt_azi) )
        intensity_dset = fid_out.create_dataset(
                'cake_integ',
                ( n_frames, par.npt_azi, par.npt_rad ),
                chunks = ( 1, par.npt_azi, par.npt_rad ),
                shuffle="True", compression="lzf",
                dtype=data_type,
                )
        
        t0 = time()
        for frame in range (0,n_frames):
        
            result2D = ai.integrate2d(
                data_in[frame,:,:], 
                par.npt_rad, 
                par.npt_azi, 
                radial_range = par.rad_range, 
                azimuth_range= par.azi_range, 
                unit=par.rad_unit,
                method = par.int_method, 
                correctSolidAngle = par.solidangle_correction, 
                dark = par.darkcurrent_correction,
                flat = flat,
                mask = mask, 
                polarization_factor = par.polarisation_factor, 
                safe = False,
            )

            radial_dset[0,:] = result2D.radial
            azimuthal_dset[0,:] = result2D.azimuthal
            intensity_dset[frame,:,:]= result2D.intensity
        
        ai.reset()
        fid_out.close()