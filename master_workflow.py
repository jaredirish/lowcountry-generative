import numpy as np
import os
from stl_slicer import STLSweetgrassSlicer
from mesh_to_spiral import SweetgrassSlicer
from stitch_simulator import StitchSimulator
from structural_analyzer import StructuralAnalyzer
from blueprint_generator import generate_svg_blueprint

def master_slice_workflow(stl_path, material_name="sweetgrass", binder_name="palmetto"):
    print(f"--- STARTING MASTER WEAVING WORKFLOW: {material_name.upper()} ---")
    
    # 1. SLICE THE STL
    slicer = STLSweetgrassSlicer(stl_path, material_name=material_name)
    path = slicer.slice()
    np.savetxt("bear_path.csv", path, delimiter=",", header="x,y,z,material_id")
    
    # 2. SIMULATE STITCHES
    print("\nSimulating Binding...")
    # Map binder width from material manager
    from material_manager import MaterialManager
    mm = MaterialManager()
    binder = mm.get_material(binder_name)
    
    simulator = StitchSimulator(stitches_per_rev=48, strip_width=binder['avg_diameter']) 
    stitch_data, material_needed = simulator.calculate_stitches(path, pitch=slicer.pitch)
    
    stitch_map = []
    for s in stitch_data:
        stitch_map.append(np.concatenate([s['wrap_point'], s['tuck_point']]))
    np.savetxt("bear_stitch_map.csv", np.array(stitch_map), delimiter=",", header="wrap_x,wrap_y,wrap_z,tuck_x,tuck_y,tuck_z")
    
    # 3. ANALYZE STRUCTURE (REBAR CHECK)
    print("\nAnalyzing Gravity Stability...")
    analyzer = StructuralAnalyzer(max_overhang_angle=40)
    critical_pts, logs = analyzer.analyze_path(path)
    
    if len(critical_pts) > 0:
        np.savetxt("bear_rebar_points.csv", critical_pts, delimiter=",", header="x,y,z")
        print(f"ALERT: Found {len(critical_pts)} unstable points. Rebar map saved.")
    
    # 4. GENERATE BLUEPRINT
    print("\nGenerating IKEA-style Blueprint...")
    generate_svg_blueprint("bear_path.csv", "bear_stitch_map.csv", output_file="bear_weaving_blueprint.svg")
    
    # 5. GENERATE STRUCTURAL STL
    print("\nGenerating Structural Multi-Material STL...")
    from path_to_structural_stl import generate_structural_woven_stl
    generate_structural_woven_stl("bear_path.csv", "bear_stitch_map.csv", "STRUCTURAL_woven_polar_bear.stl", binder_material=binder_name)
    
    print("\n--- WORKFLOW COMPLETE ---")
    print(f"Total Palmetto needed: {material_needed/1000:.2f} Meters")
    print("Files ready: bear_path.csv, bear_stitch_map.csv, bear_weaving_blueprint.svg")

if __name__ == "__main__":
    stl_file = r"C:\PROJECTS\Sweetgrass-gemini\Knitted Polar Bear - 7219009\files\knitted_polar-bear_singlecolor.stl"
    
    # Option A: Normal Sweetgrass Bear
    # master_slice_workflow(stl_file, material_name="sweetgrass")
    
    # Option B: Heavy-duty Palmetto Basket Style Bear
    master_slice_workflow(stl_file, material_name="palmetto", binder_name="palmetto")
