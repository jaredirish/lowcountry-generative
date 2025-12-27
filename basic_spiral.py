import numpy as np

def generate_spiral_path(radius=50, total_height=100, pitch=5):
    """
    Generates a basic 3D spiral (the "Heart" of a basket) as a proof of concept.
    radius: starting radius of the basket
    total_height: total height of the object
    pitch: distance between each coil (the thickness of the grass bundle)
    """
    path = []
    
    # Simple spiral logic
    num_turns = int(total_height / pitch)
    points_per_turn = 100
    
    for i in range(num_turns * points_per_turn):
        t = i / points_per_turn
        # Current height
        z = t * (total_height / num_turns)
        
        # Angle
        theta = 2 * np.pi * t
        
        # Calculate x, y (expanding radius to make a bowl shape)
        current_radius = radius + (z * 0.5) 
        x = current_radius * np.cos(theta)
        y = current_radius * np.sin(theta)
        
        path.append([x, y, z])
        
    return np.array(path)

if __name__ == "__main__":
    spiral = generate_spiral_path()
    print(f"Generated a spiral path with {len(spiral)} coordinates.")
    print(f"Start Point: {spiral[0]}")
    print(f"End Point: {spiral[-1]}")
    # Next step: Export to CSV for visualizer or robot
