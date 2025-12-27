import numpy as np
import trimesh

def path_to_mesh_stl(csv_path, output_path, thickness=3.0):
    """
    Converts a 3D path (the grass coil) into a printable STL 'tube' mesh.
    thickness: diameter of the 'grass' in the STL.
    """
    print(f"Loading path from {csv_path}...")
    path = np.loadtxt(csv_path, delimiter=",", skiprows=1)
    
    # Create a tube following the path
    # We use trimesh's sweep or simple cylinder segmenting
    segments = []
    
    print("Generating tube segments...")
    for i in range(len(path) - 1):
        p1 = path[i]
        p2 = path[i+1]
        
        # Create a cylinder for each segment
        segment_len = np.linalg.norm(p2 - p1)
        if segment_len < 0.1: continue
        
        # Simple point-to-point cylinder
        cylinder = trimesh.creation.cylinder(radius=thickness/2, height=segment_len)
        
        # Align cylinder to the vector (p2 - p1)
        direction = (p2 - p1) / segment_len
        center = (p1 + p2) / 2
        
        # Find rotation matrix to align Z-axis with 'direction'
        z_axis = [0, 0, 1]
        if not np.allclose(direction, z_axis):
            v = np.cross(z_axis, direction)
            s = np.linalg.norm(v)
            c = np.dot(z_axis, direction)
            vx = np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])
            rotation = np.eye(3) + vx + np.matmul(vx, vx) * ((1 - c) / (s**2))
            
            transform = np.eye(4)
            transform[:3, :3] = rotation
            transform[:3, 3] = center
            cylinder.apply_transform(transform)
        else:
            cylinder.apply_translation(center)
            
        segments.append(cylinder)
        
    print(f"Merging {len(segments)} segments into a single mesh...")
    full_mesh = trimesh.util.concatenate(segments)
    
    print(f"Exporting to {output_path}...")
    full_mesh.export(output_path)
    print("Export Complete!")

if __name__ == "__main__":
    path_to_mesh_stl("bear_path.csv", "woven_polar_bear_structure.stl", thickness=6.0)
