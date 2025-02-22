import numpy as np
from libsid.camera import CameraManager
from libsid.visualise.Open3dVis import O3DVisualiser
from arctic_helper import get_intrinsics_and_extrinsics, get_mano_mesh

cam_coordinates = False
frame_number = 422

intrinsics, w2e, obj_pose = get_intrinsics_and_extrinsics(frame_number)
right_hand_verts, right_hand_faces = get_mano_mesh(frame_number)
left_hand_verts, left_hand_faces = get_mano_mesh(frame_number, is_rhand=False)
egocam = CameraManager('ego', w2e, intrinsics)
vis = O3DVisualiser()

if cam_coordinates:
    obj_cam = egocam.w2c @ obj_pose # Apply object's world pose and transform it to camera coordinates
    vis.add_obj('/Users/hc23777/Library/CloudStorage/OneDrive-UniversityofBristol/main/egocentric_vision/projects/3d_hoi_rgb/data/arctic/data/arctic_data/data/meta/object_vtemplates/capsulemachine/mesh.obj', obj_cam, verts_scale=1000) # Scaling the object by 1000 as the object is in mm
    vis.add_frame(size=1, pose=egocam.w2c)  # Add world origin in camera coordinates
    vis.add_mesh(right_hand_verts, right_hand_faces, apply_pose=True, mesh_pose=egocam.w2c)    # Adding MANO right hand mesh (and projecting it to camera coordinates)
    vis.add_mesh(left_hand_verts, left_hand_faces, apply_pose=True, mesh_pose=egocam.w2c)    # Adding MANO left hand mesh (and projecting it to camera coordinates)
    cam_origin = np.eye(4)
    vis.add_cam_frustum(
        egocam.intrinsics,
        cam_origin, # Keeping the camera at origin as the object is already transformed to camera coordinates
        (2800, 2000),
        scale=1,
        color=[1, 0, 0],
    )
    vis.add_frame(size=1, pose=cam_origin)  # Add the camera frame at camera coordinates' origin
    vis.render()
else:
    vis.add_frame(size=1, pose=np.eye(4))  # Add world origin in world coordinates
    vis.add_frame(size=1, pose=egocam.c2w) # Add camera in world coordinates
    vis.add_obj('/Users/hc23777/Library/CloudStorage/OneDrive-UniversityofBristol/main/egocentric_vision/projects/3d_hoi_rgb/data/arctic/data/arctic_data/data/meta/object_vtemplates/capsulemachine/mesh.obj', obj_pose, verts_scale=1000) # Scaling the object by 1000 as the object is in mm and positing it in world coordinates
    vis.add_mesh(right_hand_verts, right_hand_faces)    # Adding MANO right hand mesh
    vis.add_mesh(left_hand_verts, left_hand_faces)    # Adding MANO left hand mesh
    vis.add_cam_frustum(
        egocam.intrinsics,
        egocam.c2w,
        (2800, 2000),
        scale=1,
        color=[1, 0, 0],
    )
    vis.render()
