# OV-2: Technical Systems Design
## LCG Portable Wire Bender v0.1

### 1. Mechanical Assembly

#### 1.1 Frame Structure
```
                    FRONT VIEW
        ┌─────────────────────────────────┐
        │         Z-ROTATE MOTOR          │
        │            (top)                │
        │              ▼                  │
        │     ┌───────────────────┐       │
        │     │    BENDING ARM    │       │
        │     │   ┌───┐           │       │
        │     │   │DIE│◄──────────┼───── Wire exits here
        │     │   └───┘           │       │
        │     └───────────────────┘       │
        │              │                  │
        │     ┌────────┴────────┐         │
        │     │   BEND MOTOR    │         │
        │     └─────────────────┘         │
        │                                 │
        │  ══════════════════════════     │ ◄── Wire path
        │                                 │
        │     ┌─────────────────┐         │
        │     │   FEED MOTOR    │         │
        │     │   [○]═══[○]     │ ◄── Knurled rollers
        │     └─────────────────┘         │
        │              ▲                  │
        └──────────────┼──────────────────┘
                       │
                  Wire from spool
```

#### 1.2 Side View
```
                    SIDE VIEW
              ┌──────────────┐
              │  Z-ROTATE    │
              │    MOTOR     │
              └──────┬───────┘
                     │
            ┌────────┴────────┐
            │   BENDING ARM   │
            │      ┌───┐      │
            │ ─────│DIE│───── │ ◄── Wire wraps around die
            │      └───┘      │
            └────────┬────────┘
                     │
            ┌────────┴────────┐
            │   BEND MOTOR    │
            └─────────────────┘
                     │
            ┌────────┴────────┐
            │   BASE PLATE    │
            │  (3D Printed)   │
            └─────────────────┘
```

### 2. Electronics Schematic

```
    ┌─────────────────────────────────────────────────────────────┐
    │                      ESP32-S3 DevKit                        │
    ├─────────────────────────────────────────────────────────────┤
    │  GPIO 12 ──► STEP (Feed Motor)                              │
    │  GPIO 13 ──► DIR  (Feed Motor)                              │
    │  GPIO 14 ──► STEP (Bend Motor)                              │
    │  GPIO 15 ──► DIR  (Bend Motor)                              │
    │  GPIO 16 ──► STEP (Z-Rotate Motor)                          │
    │  GPIO 17 ──► DIR  (Z-Rotate Motor)                          │
    │  GPIO 18 ──► EN   (All Motors Enable)                       │
    │  GPIO 21 ──► Limit Switch (Feed Home)                       │
    │  GPIO 22 ──► Limit Switch (Bend Home)                       │
    │  GND ──────► Common Ground                                  │
    │  5V ───────► Logic Power                                    │
    └─────────────────────────────────────────────────────────────┘
                              │
                              ▼
    ┌─────────────────────────────────────────────────────────────┐
    │                    DRIVER BOARD                             │
    ├────────────────┬────────────────┬───────────────────────────┤
    │   A4988 #1     │   A4988 #2     │   A4988 #3                │
    │  (Feed Motor)  │  (Bend Motor)  │  (Z-Rotate Motor)         │
    │                │                │                           │
    │  VMOT ◄────────┴────────────────┴──────── 12V PSU           │
    │  GND  ◄────────────────────────────────── GND               │
    │                                                             │
    │  1A, 1B ──► Motor Coil A                                    │
    │  2A, 2B ──► Motor Coil B                                    │
    └─────────────────────────────────────────────────────────────┘
```

### 3. Bill of Materials (With Shopping Links)

#### Electronics
| Qty | Part | Price | Link |
|:---:|:---|:---:|:---|
| 1 | ESP32-S3 DevKit | $15 | **You have this coming!** |
| 3 | NEMA 17 Stepper Motor (17HS4401) | $10 ea | [Amazon: NEMA 17 4-Pack](https://www.amazon.com/dp/B00PNEQI7W) |
| 5 | A4988 Stepper Driver + Heatsink | $8 (5-pack) | [Amazon: A4988 5-Pack](https://www.amazon.com/dp/B01FFGAKK8) |
| 1 | 12V 5A Power Supply | $12 | [Amazon: 12V 5A PSU](https://www.amazon.com/dp/B01GEA8PQA) |
| 1 | Limit Switch 3-Pack | $6 | [Amazon: Micro Limit Switches](https://www.amazon.com/dp/B07CG27D6F) |
| 1 | Jumper Wire Kit | $8 | [Amazon: Dupont Wire Kit](https://www.amazon.com/dp/B01EV70C78) |

#### Mechanical
| Qty | Part | Price | Link |
|:---:|:---|:---:|:---|
| 2 | 608 Bearings (for rollers) | $6 (10-pack) | [Amazon: 608 Bearings](https://www.amazon.com/dp/B07GVWWTR7) |
| 2 | 5mm to 5mm Flexible Coupling | $7 (2-pack) | [Amazon: Shaft Coupler](https://www.amazon.com/dp/B07MPXH7QX) |
| 1 | GT2 Timing Belt (2m) | $8 | Optional (if using belt drive) |
| - | 3D Printed Parts | $5-10 | Print from STL files |

#### Wire Material
| Source | Type | Cost |
|:---|:---|:---:|
| **Miller International Recovery** (Charleston) | Copper wire | $0 - negotiated |
| **Franklin Metals** (Mt. Pleasant) | Salvage copper | $0 - negotiated |
| **Amazon** (to test) | 18 AWG Copper Wire 100ft | [$12](https://www.amazon.com/dp/B07WHHM2P7) |
| **Amazon** (to test) | 1mm Aluminum Craft Wire | [$8](https://www.amazon.com/dp/B08LPYKMLL) |

### 4. Software Stack

| Layer | Component | Notes |
|:---|:---|:---|
| **Firmware** | Grbl_ESP32 | [GitHub](https://github.com/bdring/Grbl_Esp32) |
| **G-Code Sender** | Universal Gcode Sender (UGS) | [Download](https://winder.github.io/ugs_website/) |
| **Path Generator** | `csv_to_bend_gcode.py` | **Already created!** |
| **Design Source** | Sweetgrass Slicer (`stl_slicer.py`) | **Already created!** |

### 5. 3D Printable Parts (STL Sources)
- **Frame & Die**: Fork from [jpraus/wirebender](https://github.com/jpraus/wirebender)
- **Feed Rollers**: Design custom or use [Thingiverse: Wire Feeder](https://www.thingiverse.com/search?q=wire+feeder)

---

## Image Generation Prompts

Use these prompts with Midjourney, DALL-E, or Stable Diffusion to visualize the machine:

### Prompt 1: Product Shot (Realistic)
```
A compact, portable DIY CNC wire bending machine on a wooden workbench. The machine 
has a clean, minimalist design with these visible components: a black ESP32-S3 
microcontroller board mounted on the side, three small black NEMA 17 stepper motors 
(one for wire feed with knurled rollers, one for the bending arm with a curved metal 
die, one for Z-axis rotation), green A4988 driver boards with small aluminum heatsinks, 
and a spool of copper wire feeding into the machine. The frame is made of 3D-printed 
black PLA parts with some aluminum brackets. There's a finished wire sculpture of a 
small geometric bear shape next to the machine. The lighting is warm workshop lighting. 
Photorealistic, product photography style, shallow depth of field, 8K resolution.
```

### Prompt 2: Technical Illustration (Clean)
```
Technical illustration of a compact CNC wire bending machine, isometric view on a 
clean white background. The machine shows: an ESP32 microcontroller board, three 
NEMA 17 stepper motors arranged for Feed axis (with dual grooved rollers gripping 
wire), Bend axis (with a curved cylindrical bending die and pivoting arm), and 
Z-Rotate axis (rotating the entire bend mechanism). 3D printed matte black frame 
parts. Green A4988 driver boards visible on a small PCB. A copper wire spool mounted 
on the left side. Subtle labels pointing to each component. Engineering diagram style, 
clean vector-like lines, professional technical documentation illustration.
```

### Prompt 3: Exploded View (Assembly Guide)
```
Exploded view diagram of a DIY CNC wire bending machine showing all components 
separated but aligned along their assembly axes. Components include: ESP32-S3 
development board, three NEMA 17 stepper motors, three A4988 driver boards, 
3D printed black frame pieces (base plate, motor mounts, bending arm, roller 
housing), two 608 bearings, two knurled feed rollers, one curved bending die, 
shaft couplers, and mounting screws. White background, technical illustration 
style, assembly manual aesthetic, numbered callouts for each part.
```

### Prompt 4: In Action (Market Demo)
```
A maker demonstrating a small CNC wire bending machine at a craft market booth. 
The machine is actively bending copper wire into a spiral sculpture shape. The 
operator is watching as wire feeds from a spool, passes through motorized rollers, 
and gets bent around a die by a rotating arm. Finished wire art sculptures 
(geometric animals, abstract shapes) are displayed on the table. Warm outdoor 
lighting, craft fair atmosphere, bokeh background with other market stalls. 
Candid photography style.
```
