import trimesh
import numpy as np
import os
from material_manager import MaterialManager

class STLSweetgrassSlicer:
    """
    Slices a real STL mesh into a continuous Multi-Material Weaving Path.
    """
    def __init__(self, mesh_path, material_name="sweetgrass", points_per_rev=120):
        self.mm = MaterialManager()
        self.material = self.mm.get_material(material_name)
        self.pitch = self.material['avg_diameter']
        self.points_per_rev = points_per_rev
        
        # Load Mesh
        if not os.path.exists(mesh_path):
            raise FileNotFoundError(f"Could not find STL at {mesh_path}")
            
        print(f"Loading Mesh: {mesh_path}...")
        self.mesh = trimesh.load(mesh_path)
        
        # Center the mesh and align with Z-axis
        self.mesh.fill_holes()
        self.mesh.apply_translation(-self.mesh.center_mass)
        
        # Move so the bottom is at Z=0
        min_z = self.mesh.bounds[0][2]
        self.mesh.apply_translation([0, 0, -min_z])
        
        self.bounds = self.mesh.bounds
        self.height = self.bounds[1][2]
        print(f"Mesh Heights: 0 to {self.height:.2f}mm")

    def slice(self):
        """
        Generates the spiral path by casting rays from the Z-axis.
        """
        path = []
        total_revs = self.height / self.pitch
        num_points = int(total_revs * self.points_per_rev)
        
        print(f"Slicing {num_points} points for the Polar Bear...")
        
        for i in range(num_points):
            t = i / self.points_per_rev
            z = t * self.pitch
            theta = 2 * np.pi * t
            
            # Origin of ray: On the Z axis at height z
            ray_origin = [[0, 0, z]]
            # Direction: Outward at angle theta
            ray_direction = [[np.cos(theta), np.sin(theta), 0]]
            
            # Use trimesh to find the surface intersection
            locations, index_ray, index_tri = self.mesh.ray.intersects_location(
                ray_origins=ray_origin,
                ray_directions=ray_direction)
            
            if len(locations) > 0:
                dist = np.linalg.norm(locations, axis=1)
                best_idx = np.argmax(dist)
                # Store [x, y, z, material_id]
                path.append(np.append(locations[best_idx], self.material['id']))
            else:
                if path:
                    last_p = path[-1]
                    path.append([last_p[0], last_p[1], z, self.material['id']])
                    
        return np.array(path)

if __name__ == "__main__":
    stl_path = r"C:\PROJECTS\Sweetgrass-gemini\Knitted Polar Bear - 7219009\files\knitted_polar-bear_singlecolor.stl"
    
    try:
        # Initializing Slicer for a Palmetto-dominant basket
        slicer = STLSweetgrassSlicer(stl_path, material_name="palmetto")
        bear_path = slicer.slice()
        
        # Save results with material column
        np.savetxt("bear_path.csv", bear_path, delimiter=",", header="x,y,z,material_id")
        print(f"\nPOLAR BEAR SLICING COMPLETE!")
        print(f"Generated {len(bear_path)} points.")
        print("File saved to bear_path.csv")
        
    except Exception as e:
        print(f"FELL AT THE FINISH LINE: {e}")
