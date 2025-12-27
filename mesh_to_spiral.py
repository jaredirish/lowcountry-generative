import numpy as np

class SweetgrassSlicer:
    """
    The 'Ray-Casting' Slicer. 
    It imagines a vertical axis and 'wraps' the model by casting rays outward.
    """
    def __init__(self, pitch=5.0, points_per_rev=100):
        self.pitch = pitch # Bundle thickness in mm
        self.points_per_rev = points_per_rev

    def generate_surface_path(self, target_mesh_func, height_range=(0, 100)):
        """
        target_mesh_func: a function that returns radius for a given angle (theta) and height (z)
        """
        path = []
        z_start, z_end = height_range
        total_revolutions = (z_end - z_start) / self.pitch
        
        for i in range(int(total_revolutions * self.points_per_rev)):
            t = i / self.points_per_rev
            z = z_start + (t * self.pitch)
            theta = 2 * np.pi * t
            
            # Use the 'Ray-Cast' to find the surface at this exact spot
            radius = target_mesh_func(theta, z)
            
            x = radius * np.cos(theta)
            y = radius * np.sin(theta)
            
            path.append([x, y, z])
            
        return np.array(path)

# --- EXAMPLE MESH FUNCTIONS ---

def lcg_turtle_shell(theta, z):
    """
    Primitive math model of a turtle shell.
    A flattened hemisphere.
    """
    base_radius = 50
    # Create the 'dome' effect
    radius = base_radius * np.cos((z / 120) * (np.pi / 2))
    # Add some 'organic' wobbles to simulate hand-weaving
    wobble = 2 * np.sin(theta * 5) 
    return radius + wobble

def lcg_guitar_body(theta, z):
    """
    Primitive math model of a guitar body (Figure-8).
    """
    # Width changes based on angle (theta) to create the 'waist'
    width = 40 + 20 * np.abs(np.sin(theta))
    # Height taper
    taper = 1.0 - (z / 200)
    return width * taper

if __name__ == "__main__":
    slicer = SweetgrassSlicer(pitch=8.0) # Using thick 8mm grass bundles
    
    print("Slicing Turtle Shell...")
    turtle_path = slicer.generate_surface_path(lcg_turtle_shell, height_range=(0, 80))
    print(f"Generated {len(turtle_path)} waypoints for the Turtle.")

    print("\nSlicing Guitar Body...")
    guitar_path = slicer.generate_surface_path(lcg_guitar_body, height_range=(0, 150))
    print(f"Generated {len(guitar_path)} waypoints for the Guitar.")

    # Save to CSV for the "Case-Bot" or the Raspberry Pi
    np.savetxt("turtle_path.csv", turtle_path, delimiter=",", header="x,y,z")
    print("\nFiles saved: turtle_path.csv")
