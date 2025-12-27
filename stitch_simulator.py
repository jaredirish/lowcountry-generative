import numpy as np

class StitchSimulator:
    """
    Simulates the Palmetto binding (the 'Stitch') that holds the grass coil together.
    Calculates material usage and 'Tuck' coordinates for the robot.
    """
    def __init__(self, stitches_per_rev=40, strip_width=3.0):
        self.stitches_per_rev = stitches_per_rev
        self.strip_width = strip_width # Width of the palmetto strip in mm

    def calculate_stitches(self, path, pitch=5.0):
        """
        Calculates where each stitch is 'tucked' through the previous row.
        path: coordinate array from the Slicer [x, y, z]
        """
        stitches = []
        total_strip_length = 0
        
        # We start placing stitches effectively after the first revolution
        # Handle 4-column data [x, y, z, mat_id]
        if path.shape[1] > 3:
            coords = path[:, :3]
        else:
            coords = path
            
        points_per_rev = len(coords) // (int(max(coords[:,2]) / pitch) if max(coords[:,2]) > 0 else 1)
        
        for i in range(points_per_rev, len(coords)):
            # Place a stitch every N points based on frequency
            if i % (points_per_rev // self.stitches_per_rev) == 0:
                current_pt = coords[i]
                
                # The 'Anchor' point is directly 'below' in the previous revolution
                anchor_pt = coords[max(0, i - points_per_rev)]
                
                # Approximate stitch length: wrapping around two bundles of thickness 'pitch'
                # Formula: 2 * bundle_circumference + some overlap
                bundle_radius = pitch / 2
                stitch_length = (2 * np.pi * bundle_radius) * 1.5 
                
                stitches.append({
                    "tuck_point": anchor_pt,
                    "wrap_point": current_pt,
                    "length": stitch_length
                })
                
                total_strip_length += stitch_length
                
        return stitches, total_strip_length

if __name__ == "__main__":
    from mesh_to_spiral import SweetgrassSlicer, lcg_turtle_shell
    
    # 1. Generate a path
    pitch = 8.0 # 8mm grass bundle
    slicer = SweetgrassSlicer(pitch=pitch)
    path = slicer.generate_surface_path(lcg_turtle_shell, height_range=(0, 40))
    
    # 2. Simulate Stitches
    simulator = StitchSimulator(stitches_per_rev=32)
    stitch_data, material_needed = simulator.calculate_stitches(path, pitch=pitch)
    
    print(f"--- STITCH SIMULATION COMPLETE ---")
    print(f"Total Stitches: {len(stitch_data)}")
    print(f"Bundle Length (Grass): {len(path) * 0.5:.2f} mm") # Estimate based on spacing
    print(f"Binding Length (Palmetto): {material_needed:.2f} mm")
    print(f"Efficiency: {material_needed / (len(path) * 0.5):.2f} units of Palmetto per unit of Grass")

    # Save stitch map for the Robot's 'Effector'
    # Format: WrapX, WrapY, WrapZ, TuckX, TuckY, TuckZ
    stitch_map = []
    for s in stitch_data:
        stitch_map.append(np.concatenate([s['wrap_point'], s['tuck_point']]))
    
    np.savetxt("stitch_map.csv", np.array(stitch_map), delimiter=",", header="wrap_x,wrap_y,wrap_z,tuck_x,tuck_y,tuck_z")
    print("\nRobot Stitch Map saved: stitch_map.csv")
