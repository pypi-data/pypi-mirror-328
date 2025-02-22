import torch
import numpy as np
from libsid.camera import CameraManager
from libsid.camera.converstions import PyTorchOpen3D
from libsid.visualise.Pytorch3dVis import Py3DVisualiser
from arctic_helper import get_intrinsics_and_extrinsics, get_mano_mesh


cam_coordinates = False
frame_number = 422

intrinsics, w2e, obj_pose = get_intrinsics_and_extrinsics(frame_number)
egocam = CameraManager('ego', w2e, intrinsics)
vis = Py3DVisualiser(img_height=2000, img_width=2800, device='cpu')
vis.add_obj('/Users/hc23777/Library/CloudStorage/OneDrive-UniversityofBristol/main/egocentric_vision/projects/3d_hoi_rgb/data/arctic/data/arctic_data/data/meta/object_vtemplates/capsulemachine/mesh.obj', verts_scale=1000) # Scaling the object by 1000 as the object is in mm
right_hand_verts, right_hand_faces = get_mano_mesh(frame_number)
left_hand_verts, left_hand_faces = get_mano_mesh(frame_number, is_rhand=False)
open2pytorch = PyTorchOpen3D()

if cam_coordinates:
    vis.add_mesh(
        torch.tensor(right_hand_verts, dtype=torch.float32),
        torch.tensor(right_hand_faces, dtype=torch.float32),
    )   # Adding right hand mano mesh
    vis.transform_obj(
        0,
        obj_R=torch.tensor(obj_pose[:3, :3]),
        obj_T=torch.tensor(obj_pose[:3, 3]),
    )   # Apply object's pose in world coordinates
    vis.transform_obj(
        0,
        obj_R=torch.tensor(egocam.w2c[:3, :3]),
        obj_T=torch.tensor(egocam.w2c[:3, 3]),
    )   # Project the object to camera coordinates
    vis.transform_obj(
        1,
        obj_R=torch.tensor(egocam.w2c[:3, :3]),
        obj_T=torch.tensor(egocam.w2c[:3, 3]),
    )   # Project the right hand to camera coordinates
    vis.add_mesh(
        torch.tensor(left_hand_verts, dtype=torch.float32),
        torch.tensor(left_hand_faces, dtype=torch.float32),
    )   # Adding left hand mano mesh
    vis.transform_obj(
        2,
        obj_R=torch.tensor(egocam.w2c[:3, :3]),
        obj_T=torch.tensor(egocam.w2c[:3, 3]),
    )   # Project the left hand to camera coordinates
    # Convert the camera pose to PyTorch3D format (from Open3D format)
    cam_R, cam_T = open2pytorch.convert_3x3(np.eye(3), np.zeros(3))
    vis.render_object(
        cam_R=torch.tensor(cam_R).T,
        cam_T=torch.tensor(cam_T),
        intrinsic=torch.tensor(egocam.intrinsics),
    )   # Visualise the object in camera coordinates with camera at the origin
else:   # Visualising in world coordinates
    vis.transform_obj(
        0,
        obj_R=torch.tensor(obj_pose[:3, :3]),
        obj_T=torch.tensor(obj_pose[:3, 3]),
    )   # Apply object's pose in world coordinates
    vis.add_mesh(
        torch.tensor(right_hand_verts, dtype=torch.float32),
        torch.tensor(right_hand_faces, dtype=torch.float32),
    )   # Adding right hand mano mesh
    vis.add_mesh(
        torch.tensor(left_hand_verts, dtype=torch.float32),
        torch.tensor(left_hand_faces, dtype=torch.float32),
    )   # Adding left hand mano mesh
    cam_R, cam_T = open2pytorch.convert_3x3(
        egocam.w2c[:3, :3],
        egocam.w2c[:3, 3],
    )   # Convert the camera pose to PyTorch3D format (from Open3D format)
    vis.render_object(
        cam_R=torch.tensor(cam_R).T,    # Because PyTorch3D is row-major
        cam_T=torch.tensor(cam_T),
        intrinsic=torch.tensor(egocam.intrinsics),
    )   # Visualise the object in world coordinates with camera at its original place
