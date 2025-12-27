# Bill of Materials: CNC Wire Bender (Recycled Metal Art)

This is the hardware needed to build a 3D wire bending machine that creates sculptural art from salvaged copper/aluminum wire.

## Core Electronics (You Already Have Most of This!)
| Qty | Component | Est. Cost | Status/Notes |
|:---:|:---|:---:|:---|
| 1 | **ESP32-S3 DevKit** | $15 | ✅ **ON THE WAY** |
| 3 | **Nema 17 Stepper Motor (17HS4401)** | $10 each | 🛒 Need to order 1 more (you have 2 on BOM) |
| 3 | **A4988 Stepper Driver** | $2.50 each | 🛒 Need to order 1 more |
| 1 | **12V 5A Power Supply** | $15 | Higher amperage for 3 motors. |
| 1 | **Limit Switches (3-pack)** | $5 | For homing the feed and bend axes. |

## Mechanical & 3D-Printed Parts
| Qty | Component | Est. Cost | Notes |
|:---:|:---|:---:|:---|
| 1 | **Bending Die (3D Printed)** | ~$5 (filament) | Curved block that wire wraps around. Design from `jpraus/wirebender`. |
| 1 | **Wire Feed Rollers (3D Printed)** | ~$3 (filament) | Knurled rollers grip the wire. |
| 2 | **608 Bearings** | $3 | For the feed rollers. |
| 1 | **Bending Arm (3D Printed)** | ~$5 (filament) | Pivots to push wire against the die. |
| 1 | **Frame/Base (3D Printed or Acrylic)** | $10-$20 | Holds all components in alignment. |
| 1 | **Flexible Coupling (5mm to 5mm)** | $3 | Connects motor shaft to feed roller. |

## Wire Material (FREE / Recycled!)
| Source | Wire Type | Diameter | Cost |
|:---|:---|:---:|:---:|
| Old extension cords | Copper (stranded) | 14-18 AWG | $0 |
| Thrift store electronics (lamps, fans) | Copper (solid/stranded) | 18-22 AWG | $0-$5 |
| Hardware store (if needed) | Aluminum craft wire | 1-2mm | $5-$10/roll |
| Old Ethernet cables | Copper (thin, solid) | 24 AWG | $0 |
| Salvaged coax cable (center conductor) | Copper-clad steel | 18 AWG | $0 |

## Total Estimated Cost: **~$80 - $150** (if you salvage wire)

---

## Open-Source References
- **`jpraus/wirebender` (GitHub)**: [https://github.com/jpraus/wirebender](https://github.com/jpraus/wirebender)
  - Precise CNC wire bending for 1mm wire.
  - Most parts 3D printable.
  - Good documentation for jewelry/art.
- **`kavers1/wirebender` (GitHub)**: [https://github.com/kavers1/wirebender](https://github.com/kavers1/wirebender)
  - Uses ESP32 + Grbl.
  - STL files for mechanical parts.

## Firmware
- **Grbl_ESP32**: [https://github.com/bdring/Grbl_Esp32](https://github.com/bdring/Grbl_Esp32)
- Or a custom firmware that interprets "bend angle" commands (you can write this).

## G-Code Adaptation
Your `bear_path.csv` can be converted to bend instructions:
```
# Example: csv_to_bend_gcode.py output
G1 F10      ; Feed 10mm of wire
G2 B30      ; Bend 30 degrees
G1 F5       ; Feed 5mm
G3 Z10      ; Rotate Z-axis 10 degrees (for 3D curve)
G2 B-15     ; Bend -15 degrees (reverse direction)
...
```

---

## The Art Product
**"One Wire, One Bear"**
A single continuous strand of recycled copper, bent by algorithm into the woven DNA of a Polar Bear.
- Estimated sale price: $200 - $500
- Edition size: 10 (each unique due to wire variations)
