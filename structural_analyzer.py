import numpy as np

class StructuralAnalyzer:
    """
    Analyzes the 'Weaving Path' for gravity-induced sag and identifies 
    where 'Copper Rebar' (Internal Skeleton) is required.
    """
    def __init__(self, grass_stiffness_factor=1.0, max_overhang_angle=45):
        self.grass_stiffness = grass_stiffness_factor
        self.max_overhang = max_overhang_angle # degrees

    def analyze_path(self, raw_path):
        """
        Analyzes the path for stability.
        """
        if raw_path.shape[1] > 3:
            path = raw_path[:, :3]
        else:
            path = raw_path
            
        critical_points = []
        instability_log = []
        
        for i in range(1, len(path)):
            p1 = path[i-1]
            p2 = path[i]
            
            # 1. Calculate the Slope (Angle) relative to vertical
            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]
            dz = p2[2] - p1[2]
            
            distance_xy = np.sqrt(dx**2 + dy**2)
            
            if dz == 0:
                angle = 90 # Horizontal
            else:
                angle = np.degrees(np.arctan(distance_xy / dz))
            
            # 2. Overhang Check: Is it too flat to support its own weight?
            if angle > self.max_overhang:
                critical_points.append(p2)
                instability_log.append({
                    "point": p2,
                    "angle": angle,
                    "severity": (angle - self.max_overhang) / 45.0 # normalized 0-1
                })
        
        return np.array(critical_points), instability_log

if __name__ == "__main__":
    # Load previously generated turtle path
    try:
        data = np.loadtxt("turtle_path.csv", delimiter=",", skiprows=1)
        analyzer = StructuralAnalyzer(max_overhang_angle=35) # Strict settings for wet grass
        critical_pts, logs = analyzer.analyze_path(data)
        
        print(f"--- STRUCTURAL ANALYSIS COMPLETE ---")
        print(f"Total Waypoints: {len(data)}")
        print(f"Critical Stability Points: {len(critical_pts)}")
        
        if len(critical_pts) > 0:
            print(f"Advice: Add Copper skeletal rings at Z-heights: {np.unique(np.round(critical_pts[:,2], 1))}")
            np.savetxt("rebar_points.csv", critical_pts, delimiter=",", header="x,y,z")
            print("Saved reinforcement map to: rebar_points.csv")
        else:
            print("Structure is self-supporting. No rebar needed.")
            
    except Exception as e:
        print(f"Error: {e}. Please run mesh_to_spiral.py first.")
