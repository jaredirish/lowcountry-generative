# Bill of Materials: LCG Art Plotter (Prototype v0.1)

This is the hardware needed to build a small-footprint pen plotter that can draw your weaving blueprints.

## Core Electronics
| Qty | Component | Est. Cost | Link/Notes |
|:---:|:---|:---:|:---|
| 1 | **ESP32-S3 DevKit** | $15 | You have this on the way! |
| 2 | **Nema 17 Stepper Motor (17HS4401)** | $10 each | Standard 1.7A motors for X/Y axis. |
| 2 | **A4988 Stepper Driver** | $2.50 each | Common, easily replaceable. |
| 1 | **Micro Servo (SG90)** | $3 | Pen lift mechanism (Z-axis). |
| 1 | **12V 2A Power Supply** | $10 | Powers the stepper motors. |

## Mechanical Frame
| Qty | Component | Est. Cost | Link/Notes |
|:---:|:---|:---:|:---|
| 2m | **V-Slot 2020 Aluminum Extrusion** | $25 | Cut to size for X/Y rails. |
| 4 | **V-Slot Gantry Plate (or 3D Print)** | $10-$15 | To mount the motors and carriage. |
| 2 | **GT2 Timing Belt (1m each)** | $5 per belt | Connects motors to carriage. |
| 4 | **GT2 Pulley (20 Tooth)** | $3 each | Attach to motor shafts. |
| 8 | **Smooth Idler Pulley** | $1 each | For belt tensioning. |

## Pen Holder & Misc
| Qty | Component | Est. Cost | Link/Notes |
|:---:|:---|:---:|:---|
| 1 | **3D Printed Pen Holder** | ~$5 (filament) | Design to hold Sakura Micron pens. |
| 1 | **Set of Sakura Micron Pens** | $15 | Archival ink, various nib sizes. |
| 1 | **USB Cable (USB-C)** | $5 | For ESP32-S3 connection. |
| 1 | **Acrylic Sheet (A3 Size) or MDF Board** | $10 | The "Bed" where paper is placed. |

## Total Estimated Cost: **~$150 - $200**

---

## Where to Buy
- **Amazon**: Fast shipping for most parts.
- **AliExpress**: Cheapest, but 2-3 week shipping for V-slot and motors.
- **OpenBuilds PartStore**: High-quality V-slot extrusions and kits.
- **Your Local Makerspace**: May have 3D printers and scrap materials.

## Firmware
- **Grbl_ESP32**: [https://github.com/bdring/Grbl_Esp32](https://github.com/bdring/Grbl_Esp32)
- Flash to your ESP32-S3 via PlatformIO or Arduino IDE.
- Control via **LaserGRBL** (Windows) or **UGS (Universal G-code Sender)**.

## G-Code Ready!
Your `bear_plot.gcode` file is already generated and contains **2,441 commands** ready to plot the Polar Bear blueprint.
