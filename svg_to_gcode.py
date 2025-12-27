import numpy as np

def svg_to_gcode(svg_path, output_path, feedrate=1500, z_up=5, z_down=0):
    """
    Converts an SVG path (from blueprint_generator.py) into G-code for a pen plotter.
    This is a simplified converter for polylines—not a full SVG parser.
    """
    import re

    with open(svg_path, 'r') as f:
        svg_content = f.read()

    # Find all polyline points
    polylines = re.findall(r'<polyline points="([^"]+)"', svg_content)
    # Also find line elements
    lines = re.findall(r'<line x1="([^"]+)" y1="([^"]+)" x2="([^"]+)" y2="([^"]+)"', svg_content)

    gcode = []
    gcode.append("G21 ; Set units to millimeters")
    gcode.append("G90 ; Absolute positioning")
    gcode.append(f"G0 Z{z_up} ; Pen up")

    for points_str in polylines:
        points = points_str.strip().split()
        first = True
        for p in points:
            if ',' not in p:
                continue
            x, y = p.split(',')
            x, y = float(x), float(y)
            if first:
                gcode.append(f"G0 X{x:.2f} Y{y:.2f} ; Rapid to start")
                gcode.append(f"G0 Z{z_down} ; Pen down")
                first = False
            else:
                gcode.append(f"G1 X{x:.2f} Y{y:.2f} F{feedrate}")
        gcode.append(f"G0 Z{z_up} ; Pen up")

    for line in lines:
        x1, y1, x2, y2 = [float(v) for v in line]
        gcode.append(f"G0 X{x1:.2f} Y{y1:.2f} ; Move to line start")
        gcode.append(f"G0 Z{z_down} ; Pen down")
        gcode.append(f"G1 X{x2:.2f} Y{y2:.2f} F{feedrate}")
        gcode.append(f"G0 Z{z_up} ; Pen up")

    gcode.append("G0 X0 Y0 ; Return home")
    gcode.append("M2 ; End program")

    with open(output_path, 'w') as f:
        f.write("\n".join(gcode))

    print(f"G-code written to {output_path}")
    print(f"Total commands: {len(gcode)}")

if __name__ == "__main__":
    svg_to_gcode("bear_weaving_blueprint.svg", "bear_plot.gcode")
