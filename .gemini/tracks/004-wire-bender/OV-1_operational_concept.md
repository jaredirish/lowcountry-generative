# OV-1: High-Level Operational Concept
## LCG Portable Wire Bender v0.1

### 1. System Overview
The LCG Wire Bender is a compact, ESP32-controlled CNC machine that bends metal wire into 3D sculptural forms based on algorithmically-generated paths from the Sweetgrass Slicer.

```
┌─────────────────────────────────────────────────────────────────┐
│                    LCG WIRE BENDER - TOP VIEW                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│    ┌──────┐                                                     │
│    │ WIRE │                                                     │
│    │SPOOL │──────┐                                              │
│    └──────┘      │                                              │
│                  ▼                                              │
│           ┌─────────────┐      ┌─────────────┐                  │
│           │   FEED      │      │   BEND      │                  │
│           │   MOTOR     │─────►│   MOTOR     │                  │
│           │  (NEMA 17)  │      │  (NEMA 17)  │                  │
│           │             │      │             │                  │
│           │  [ROLLERS]  │      │  [DIE+ARM]  │──────► OUTPUT    │
│           └─────────────┘      └─────────────┘       SCULPTURE  │
│                  │                    │                         │
│                  │              ┌─────────────┐                 │
│                  │              │  Z-ROTATE   │                 │
│                  │              │   MOTOR     │                 │
│                  │              │  (NEMA 17)  │                 │
│                  │              └─────────────┘                 │
│                  │                    │                         │
│           ┌──────┴────────────────────┴──────┐                  │
│           │          DRIVER BOARD            │                  │
│           │     (3x A4988 + ESP32-S3)        │                  │
│           └──────────────────────────────────┘                  │
│                          │                                      │
│                    ┌─────┴─────┐                                │
│                    │  12V PSU  │                                │
│                    └───────────┘                                │
└─────────────────────────────────────────────────────────────────┘
```

### 2. Operational Flow
```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   USER      │    │  SWEETGRASS │    │  G-CODE     │    │   WIRE      │
│   UPLOADS   │───►│   SLICER    │───►│  CONVERTER  │───►│   BENDER    │
│   3D MODEL  │    │ (bear_path) │    │ (csv_to_    │    │  EXECUTES   │
│   (.STL)    │    │             │    │  bend.py)   │    │  SCULPTURE  │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
```

### 3. Key Specifications
| Parameter | Value |
|:---|:---|
| **Footprint** | ~200mm x 150mm x 100mm |
| **Wire Diameter** | 0.5mm - 2.0mm |
| **Bend Resolution** | 1° increments |
| **Feed Resolution** | 0.1mm |
| **Max Wire Length** | Unlimited (spool-fed) |
| **Power** | 12V DC, 5A |
| **Controller** | ESP32-S3 + Grbl firmware |
| **Communication** | USB, WiFi, Bluetooth |

### 4. Use Cases
1. **Art Market Sales**: Create "One Wire" sculptures live at craft fairs.
2. **Custom Commissions**: Client uploads STL → Machine bends unique piece.
3. **Heritage Tie-In**: Wire "rebar" for the sweetgrass weaving structures.
4. **Jewelry Prototyping**: Bent wire rings, pendants, earrings.

### 5. Material Sources (Charleston Area)
- **Miller International Recovery**: Buys/sells copper wire.
- **Franklin Metals (Mt. Pleasant)**: Scrap metal recycler.
- **A&R Recycling (Mt. Pleasant)**: Non-ferrous metal buyer.
- **Old extension cords**: Free from neighbors/thrift stores.
