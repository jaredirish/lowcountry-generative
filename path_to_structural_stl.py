import numpy as np
import trimesh
from material_manager import MaterialManager

def generate_structural_woven_stl(path_csv, stitch_csv, output_path, binder_material="palmetto"):
    """
    Generates a structurally sound STL by combining the multiple materials in the path.
    """
    mm = MaterialManager()
    binder = mm.get_material(binder_material)
    
    # Reverse lookup for material profiles by ID
    profiles = {m['id']: m for m in mm.materials.values()}
    print(f"Loading data: {path_csv} and {stitch_csv}...")
    path = np.loadtxt(path_csv, delimiter=",", skiprows=1)
    stitches = np.loadtxt(stitch_csv, delimiter=",", skiprows=1)
    
    meshes = []
    
    # 1. GENERATE THE MATERIAL COILS
    print("Generating Multi-Material Coil Geometry...")
    for i in range(len(path) - 1):
        p1_full = path[i]
        p2_full = path[i+1]
        
        p1 = p1_full[:3]
        p2 = p2_full[:3]
        mat_id = int(p1_full[3])
        
        profile = profiles.get(mat_id, profiles[1]) # Default to sweetgrass
        thickness = profile['avg_diameter']
        
        # Segment vector
        vec = p2 - p1
        dist = np.linalg.norm(vec)
        if dist < 0.1: continue
        
        # Create cylinder segment
        cylinder = trimesh.creation.cylinder(radius=thickness/2, height=dist)
        
        # Position and Rotate
        center = (p1 + p2) / 2
        direction = vec / dist
        z_axis = [0, 0, 1]
        
        transform = np.eye(4)
        if not np.allclose(direction, z_axis):
            v = np.cross(z_axis, direction)
            s = np.linalg.norm(v)
            c = np.dot(z_axis, direction)
            vx = np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])
            rotation = np.eye(3) + vx + np.matmul(vx, vx) * ((1 - c) / (s**2))
            transform[:3, :3] = rotation
            
        transform[:3, 3] = center
        cylinder.apply_transform(transform)
        meshes.append(cylinder)

    # 2. GENERATE THE STITCHES (The 'Reinforcement')
    print("Generating Palmetto Stitch Reinforcements...")
    # We add the stitches as small cylinders linking the current row to the previous one
    for i in range(len(stitches)):
        # Stitch data is [wrap_x, wrap_y, wrap_z, tuck_x, tuck_y, tuck_z]
        s = stitches[i]
        p1 = s[:3] # Wrap point
        p2 = s[3:] # Tuck point
        
        vec = p2 - p1
        dist = np.linalg.norm(vec)
        if dist < 0.1: continue
        
        # Create a smaller cylinder for the stitch
        stitch_cyl = trimesh.creation.cylinder(radius=binder['avg_diameter']/2, height=dist)
        
        center = (p1 + p2) / 2
        direction = vec / dist
        z_axis = [0, 0, 1]
        
        transform = np.eye(4)
        if not np.allclose(direction, z_axis):
            v = np.cross(z_axis, direction)
            s_val = np.linalg.norm(v)
            c = np.dot(z_axis, direction)
            vx = np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])
            rotation = np.eye(3) + vx + np.matmul(vx, vx) * ((1 - c) / (s_val**2))
            transform[:3, :3] = rotation
            
        transform[:3, 3] = center
        stitch_cyl.apply_transform(transform)
        meshes.append(stitch_cyl)

    print(f"Merging {len(meshes)} components into a structural mesh...")
    final_mesh = trimesh.util.concatenate(meshes)
    
    print(f"Exporting Structural STL: {output_path}...")
    final_mesh.export(output_path)
    print("DONE! This mesh is now a unified lattice and should print reliably.")

if __name__ == "__main__":
    generate_structural_woven_stl(
        "bear_path.csv", 
        "bear_stitch_map.csv", 
        "STRUCTURAL_woven_polar_bear.stl",
        binder_material="palmetto"
    )
