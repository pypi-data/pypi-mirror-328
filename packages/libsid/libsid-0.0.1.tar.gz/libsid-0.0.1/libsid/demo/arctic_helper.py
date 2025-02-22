import numpy as np
import torch
from smplx import MANO
from scipy.spatial.transform import Rotation as R
import matplotlib.pyplot as plt


def get_intrinsics_and_extrinsics(frame_number):
    cam_data =  np.load('/Users/hc23777/Library/CloudStorage/OneDrive-UniversityofBristol/main/egocentric_vision/projects/3d_hoi_rgb/data/arctic/data/arctic_data/data/raw_seqs/s02/capsulemachine_grab_01.egocam.dist.npy', allow_pickle=True).item()
    obj_pose_data = np.load('/Users/hc23777/Library/CloudStorage/OneDrive-UniversityofBristol/main/egocentric_vision/projects/3d_hoi_rgb/data/arctic/data/arctic_data/data/raw_seqs/s02/capsulemachine_grab_01.object.npy', allow_pickle=True)

    # Getting the camera pose
    cam_R = cam_data['R_k_cam_np'][frame_number]
    cam_T = cam_data['T_k_cam_np'][frame_number]
    w2e = np.eye(4)
    w2e[:3, :3] = cam_R
    w2e[:3, 3] = cam_T.squeeze() 

    # Getting the object pose
    obj_R_axis = obj_pose_data[frame_number][1:4]
    obj_T = obj_pose_data[frame_number][4:] / 1000# Convert to meters
    obj_R = R.from_rotvec(obj_R_axis).as_matrix()
    obj_pose = np.eye(4)
    obj_pose[:3, :3] = obj_R
    obj_pose[:3, 3] = obj_T
    
    # Getting the camera intrinsics
    intrinsics = cam_data['intrinsics']

    return np.array(intrinsics), w2e, obj_pose


def get_mano_mesh(frame_number, is_rhand=True, use_pca=False, num_betas=10):
    hand_side = 'right' if is_rhand else 'left'
    mano_params = np.load('/Users/hc23777/Library/CloudStorage/OneDrive-UniversityofBristol/main/egocentric_vision/projects/3d_hoi_rgb/data/arctic/data/arctic_data/data/raw_seqs/s02/capsulemachine_grab_01.mano.npy', allow_pickle=True).item()[hand_side]
    global_orient = mano_params['rot'][frame_number].reshape(1, 3)
    hand_pose = mano_params['pose'][frame_number].reshape(1, -1)
    transl = mano_params['trans'][frame_number].reshape(1, -1)
    betas = mano_params['shape'].reshape(1, -1)
    mano_model = MANO(
        '/Users/hc23777/Downloads/mano_v1_2/models',
        use_pca=use_pca,
        is_rhand=is_rhand,
        num_betas=num_betas,
    )
    # Forward pass to get the hand mesh
    output = mano_model(
        betas=torch.tensor(betas),
        global_orient=torch.tensor(global_orient),
        hand_pose=torch.tensor(hand_pose),
        transl=torch.tensor(transl),
    )
    return output.vertices.detach().cpu().numpy()[0], mano_model.faces
