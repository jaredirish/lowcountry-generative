import numpy as np

def generate_svg_blueprint(path_file, stitch_file, output_file="weaving_blueprint.svg"):
    """
    Generates a 2D 'Instruction Map' (SVG) showing the spiral and the tuck points.
    Think of this as the 'IKEA Manual' for sweetgrass.
    """
    try:
        path = np.loadtxt(path_file, delimiter=",", skiprows=1)
        stitches = np.loadtxt(stitch_file, delimiter=",", skiprows=1)
        
        # Scaling and Offsetting for SVG
        scale = 5
        offset = 300 # Center of a 600x600 canvas
        
        with open(output_file, 'w') as f:
            f.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
            f.write('<svg width="600" height="600" xmlns="http://www.w3.org/2000/svg">\n')
            f.write('<rect width="100%" height="100%" fill="#1a1a1a" />\n') # Dark mode background
            
            # 1. Draw the Grass Coil (The Spiral)
            f.write('<polyline points="')
            for p in path:
                # We project the 3D path into 2D (Top-down view)
                f.write(f"{p[0]*scale + offset},{p[1]*scale + offset} ")
            f.write('" stroke="#8b9d77" stroke-width="2" fill="none" opacity="0.6" />\n')
            
            # 2. Draw the Stitches (The Palmetto Ties)
            # We only draw a few key ones to avoid cluttering the blueprint
            for i, s in enumerate(stitches):
                if i % 5 == 0: # Every 5th stitch for readability
                    # s is [wrap_x, wrap_y, wrap_z, tuck_x, tuck_y, tuck_z]
                    f.write(f'<line x1="{s[0]*scale + offset}" y1="{s[1]*scale + offset}" ')
                    f.write(f'x2="{s[3]*scale + offset}" y2="{s[4]*scale + offset}" ')
                    f.write('stroke="#e0d7c6" stroke-width="1" opacity="0.8" />\n')
            
            # 3. Add Title and Version
            f.write(f'<text x="20" y="40" fill="#FFFFFF" font-family="Arial" font-size="20">LCG Weaving Blueprint: v0.1</text>\n')
            f.write(f'<text x="20" y="65" fill="#888888" font-family="Arial" font-size="12">Grass Path: {len(path)} points | Stitches: {len(stitches)}</text>\n')
            
            f.write('</svg>')
            
        print(f"Success! Blueprint generated: {output_file}")
        
    except Exception as e:
        print(f"Blueprint Error: {e}. Ensure path and stitch files exist.")

if __name__ == "__main__":
    generate_svg_blueprint("turtle_path.csv", "stitch_map.csv")
