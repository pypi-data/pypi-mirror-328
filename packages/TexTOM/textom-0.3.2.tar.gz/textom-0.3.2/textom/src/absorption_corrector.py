import numpy as np
import matplotlib.pyplot as plt
from numba import njit, prange

import textom.src.rotation as rot
from textom.input import geometry as geo
# from textom.config import data_type

# from . import rotation as rot
# from ..input import geometry as geo
# from ..config import data_type # azimuthal binning on the detector

def absorption_correction( tomogram, mask, scattering_angles, azimuthal_angles, Gs, 
                        #   iBeams, 
                          x_p,
                          ):
    """_summary_

    Parameters
    ----------
    tomogram : _type_
        absorption tomogram
    mask :
        mask or threshold for not calculating everything
    scattering_angles : _type_
        relevant angles 2theta / q-values on the detector (peaks)
    chi :
        detector angles (binned)
    Gs : _type_
        sample rotations ? might do this afterwards.

    Returns
    -------
    _type_
        _description_
    """
    g,t = 0,0
    # for each projection (g):
    beam_direction = geo.beam_direction @ rot.OTP_to_matrix(Gs[g,0],Gs[g,1],Gs[g,2])
    detector_direction_origin = geo.detector_direction_origin @ rot.OTP_to_matrix(Gs[g,0],Gs[g,1],Gs[g,2])
    detector_direction_positive_90 = geo.detector_direction_positive_90 @ rot.OTP_to_matrix(Gs[g,0],Gs[g,1],Gs[g,2])
    # for each g and t:
    entry_point = np.array([0,0,0]) #x_p[iBeams[g,t]] # tip of the cone
    entry_point = np.array([-0.1,20,5]) #x_p[iBeams[g,t]] # tip of the cone
    
    absorption_pattern = np.empty((scattering_angles.size,azimuthal_angles.size), np.float64)
    for q, twotheta in enumerate(scattering_angles): # cone angle ~ 2theta
        for c, chi in enumerate(azimuthal_angles):
            absorption_pattern[q,c] = integrate_paths(
                tomogram, entry_point, np.array(beam_direction), twotheta, chi, 
                np.array(detector_direction_origin), np.array(detector_direction_positive_90)
            )
            # absorption_pattern[q,c] = integrate_middle_path(
            #     tomogram, entry_point, np.array(beam_direction), twotheta, chi, 
            #     np.array(detector_direction_origin), np.array(detector_direction_positive_90)
            # )
    return absorption_pattern

@njit
def cone_wedge_to_cartesian(h, r, theta, tip, axis, origin_vec, pos_dir_vec):
    """
    Convert cone wedge coordinates (h, r, theta) to Cartesian coordinates.
    """
    # Compute position in local frame
    point = tip + h * axis + r * (np.cos(theta) * origin_vec + np.sin(theta) * pos_dir_vec)
    return point

def sample_paths( h, tip, axis, opening_angle, chi, origin_vec, pos_dir_vec, dV ):
    dr = dV**(1/3)
    paths = []
    zz = np.arange(0,h,dr) # start value for each path
    p = np.arange(0,h/np.cos(opening_angle),dr) # path variable
    for z in zz:
        z_p = p * np.cos(opening_angle) + z
        r_p = p * np.sin(opening_angle)
        paths.append(np.array([
            cone_wedge_to_cartesian(z, r, t, tip, axis, origin_vec, pos_dir_vec) for z,r,t in
            zip(z_p, r_p, chi*np.ones_like(z_p))]))
    return paths

def integrate_paths(grid, cone_tip, cone_axis, opening_angle, chi, origin_vec, pos_dir_vec,
                   dV=1):
    """
    Perform an integration over a cone wedge by sampling points equal-volume
    """
    h = np.sqrt(grid.shape[0]**2+grid.shape[2]**2)# max length of the cone
    paths = sample_paths( h, cone_tip, cone_axis, opening_angle, chi, origin_vec, pos_dir_vec, dV )
    path_ints = []
    for path in paths:
        path_int = 0.
        points = np.round(path).astype(np.int64)
        for p in points:
            if np.all( p >= np.zeros_like(p) ) and np.all( p < np.array(grid.shape) ):
                path_int += grid[p[0],p[1],p[2]]
        path_ints.append(path_int)            
    return np.mean(path_ints)

def middle_path( h, tip, axis, opening_angle, chi, origin_vec, pos_dir_vec, dV ):
    # to calculate the middle i should actually take it out of iBeams
    dr = dV**(1/3)
    p = np.arange(0,h/np.cos(opening_angle),dr) # path variable
    z_p = p * np.cos(opening_angle) + h/2 # z_middle
    r_p = p * np.sin(opening_angle)
    middle_path = np.array([
            cone_wedge_to_cartesian(z, r, t, tip, axis, origin_vec, pos_dir_vec) for z,r,t in
            zip(z_p, r_p, chi*np.ones_like(z_p))])
    return middle_path

def integrate_middle_path(grid, cone_tip, cone_axis, opening_angle, chi, origin_vec, pos_dir_vec,
                   dV=1):
    """

    """
    h = np.sqrt(grid.shape[0]**2+grid.shape[2]**2)# max length of the cone
    path = middle_path( h, cone_tip, cone_axis, opening_angle, chi, origin_vec, pos_dir_vec, dV )
    path_int = 0.
    points = np.round(path).astype(np.int64)
    for p in points:
        if np.all( p >= np.zeros_like(p) ) and np.all( p < np.array(grid.shape) ):
            path_int += grid[p[0],p[1],p[2]]
    return path_int

# tomogram = np.ones((40,40,10), np.float64)
# nchi = 30
# Chi = np.linspace(0,2*np.pi, num=nchi, endpoint=False) + 2*np.pi/nchi/2
# Q = np.linspace(10, 35, num=10, endpoint=False) # nm^-1
# lam = 0.0826565
# two_theta = 2 * np.arcsin( Q*lam / (4*np.pi) )
# Gs = np.array([[0,0,0]])
# # Gs = np.array([[np.pi/4,np.pi/2,np.pi/2]])
# Gs = np.array([[0.7,0.2,0.3]])

# absorption_pattern = absorption_correction(tomogram,0,
#                                 two_theta,Chi,Gs,0)
# # print(absorption_pattern)
# CHi, QQ = np.meshgrid( Chi, Q )
# X1 = -QQ*np.sin(CHi)
# X2 = QQ*np.cos(CHi)
# m = plt.pcolormesh( X1, X2, absorption_pattern, cmap='plasma', vmin=0, vmax=absorption_pattern.max() )
# plt.axis('equal')
# plt.grid(False)
# plt.colorbar(m)

# # points = sample_cone_wedge(30, np.array([0,0,0]), np.array([1,0,0]), np.pi/6, 
# #                                       0, np.pi/6, np.array([0,0,1]), np.array([0,-1,0]), 2)
# # print(points.shape)
# # fig = plt.figure()#figsize=(10, 10))
# # ax = fig.add_subplot(111, projection='3d')
# # ax.scatter(points[:,0],points[:,1],points[:,2])

# plt.show()