# Deep Research: 3D Art Plotter with Recycled Non-Organic Materials

## Executive Summary
This analysis explores three distinct **3D art fabrication systems** that use easily-obtained, non-organic, recycled materials. Each offers a unique "impossible art" capability and aligns with your **Sweetgrass Slicer** IP as the generative engine.

---

## Option A: "PET Bottle Filament Printer" 🥤

### The Concept
Convert discarded PET plastic bottles into 3D printer filament, then print sculptures directly from your Slicer's STL outputs.

### Why It's Interesting
- **Zero Material Cost**: Charleston produces tons of plastic waste. Your raw material is free.
- **Sustainability Story**: "Ocean Grass"—printed art made from recycled coastal plastics.
- **Closed-Loop**: You slice, you extrude, you print. Full vertical integration.

### Key Hardware (DIY, ~$200-$400)
| Component | Est. Cost | Notes |
|:---|:---:|:---|
| **PETamentor Kit** (Open Source) | $100-$150 | Motor, heated nozzle, spool mechanism. Converts bottles to 1.75mm filament. |
| **Tylman PET-Machine** | ~$80-$120 (DIY kit) | Modular, affordable. 2-3 hours per 2L bottle. |
| **Any Ender 3 Printer** | $150-$200 | The most common, well-supported FDM printer. Prints your rPET filament. |
| **PET Bottle Cutter Jig** | $10-$20 | Cuts bottles into consistent strips for feeding. |

### The Art Angle
- Print your `STRUCTURAL_woven_polar_bear.stl` in **translucent recycled PET**.
- Each piece has a unique "Ocean Story"—the bottles came from a specific beach cleanup.
- Sell at galleries as **"Regenerative Heritage Art."**

### Challenges
- Filament quality consistency (humidity, impurities).
- Requires drying bottles and removing labels.
- Slower than buying commercial filament.

---

## Option B: "CNC Wire Bender" for Metal Sculptures 🔩

### The Concept
A machine that bends wire (steel, copper, aluminum) into 3D sculptural forms based on your Slicer's path data. Think: **"Wire-Frame Polar Bear."**

### Why It's Interesting
- **Impossible Precision**: Consistent bends at 0.5° increments that no human can replicate.
- **Hardware You Already Have**: ESP32-S3, Nema 17 motors, A4988 drivers.
- **Recycled Metal**: Use salvaged copper wire from old electronics (e-waste).

### Key Hardware (DIY, ~$150-$250)
| Component | Est. Cost | Notes |
|:---|:---:|:---|
| **ESP32-S3** | $15 | You have this! |
| **Nema 17 Stepper x3** | $30 | Feed, Bend, Z-Rotate axes. |
| **A4988 Drivers x3** | $8 | Standard drivers. |
| **Bending Die (3D Printed)** | ~$5 (filament) | Custom-designed for 1-2mm wire. |
| **Wire Feed Mechanism** | ~$20 | Rollers + motor. |
| **GT2 Belts/Pulleys** | ~$15 | For the rotation axis. |
| **Salvaged Copper Wire (14-18 AWG)** | $0 | From old extension cords, electronics. |

### Open-Source Projects
- **`jpraus/wirebender` (GitHub)**: Precise CNC wire bending, most parts 3D printed, for 1mm wire.
- **`kavers1/wirebender` (GitHub)**: ESP32-Grbl based, with STL files for mechanical parts.

### The Art Angle
- Convert your `bear_path.csv` into a **wire sculpture toolpath**.
- The machine bends a single continuous strand of copper into the Polar Bear's woven DNA.
- **"One Wire, One Bear."** Limited editions. Each is unique because of the wire's natural memory.

### G-Code Adaptation
Your existing `svg_to_gcode.py` can be modified to output **"bend commands"** instead of "move commands."
- `G1 X10` = Feed 10mm of wire.
- `G2 A30` = Bend 30 degrees.
- `G3 Z5` = Rotate Z-axis 5 degrees for 3D forms.

---

## Option C: "Clay/Paste Extruder" for Ceramic Sculptures 🏺

### The Concept
A 3D printer that extrudes clay or ceramic paste. Your Slicer generates the spiral path; the machine builds a **physical "woven" ceramic vessel**.

### Why It's Interesting
- **Tangible Heritage**: Combines Gullah coil-building technique with robotic precision.
- **Sellable End Product**: A fired ceramic piece is worth $100-$500+.
- **Platform for the Slicer**: Your spiral algorithm is the "secret sauce" for coil heights and widths.

### Key Hardware (DIY, ~$300-$600)
| Component | Est. Cost | Notes |
|:---|:---:|:---|
| **Ender 3 Pro (Modified)** | $150-$200 | Base printer with bed and frame. |
| **CERAMBOT Extruder Kit** | $100-$200 | Mounts to Ender 3. Air-pressure fed clay system. |
| **StoneFlower Extruder (Open Source)** | ~$80 (DIY) | Full-metal, screw-driven. Compatible with most printers. |
| **Air Compressor** | $50-$100 | For pressurizing the clay reservoir. |
| **Local Clay or Pottery Supplies** | $20-$50/bag | Available at craft stores. |

### Open-Source Projects
- **CeraStruder**: Open-source hardware with BOM and design files.
- **StoneFlower3D**: Robust, affordable clay extruder for desktop printers.
- **JetClay**: Large-format open-source extrusion for high-humidity clay.

### The Art Angle
- Your Slicer outputs a **3D spiral path at variable pitch** (mimicking sweetgrass bundle heights).
- The clay printer builds a vessel that **looks woven** but is solid ceramic.
- After firing, each piece is unique. Sell at the **Charleston City Market** or online.

### Material Sourcing
| Material | Source | Cost |
|:---|:---|:---:|
| Porcelain Clay | Local pottery supply (Carolina Clay) | $15-$25/25lb |
| Stoneware Clay | Ceramic shop or Amazon | $20-$30/25lb |
| Air-Dry Clay | Michael's, Hobby Lobby | $10/5lb |
| Recycled Pulp/Paper Paste | DIY from shredded paper + glue | ~$0 |

---

## Comparative Analysis: Which 3D Art Plotter?

| Factor | PET Printer | Wire Bender | Clay Extruder |
|:---|:---:|:---:|:---:|
| **Material Cost** | $0 (free bottles) | $0-$10 (salvaged wire) | $20-$50 (clay) |
| **Build Complexity** | Medium (filament making is fiddly) | Low-Medium (mostly 3D printed) | Medium-High (air system) |
| **Uniqueness** | High (few do this) | **Very High** (almost no one) | Medium (growing niche) |
| **Sellability** | Medium (plastic art) | **High** (metal art is premium) | **High** (ceramics are classic) |
| **Slicer Integration** | Direct (uses STL output) | Needs G-code adapter | Direct (uses spiral path) |
| **Heritage Tie-In** | Good ("Ocean Grass") | **Excellent** (metal rebar in baskets) | **Excellent** (coil building) |

---

## My Recommendation: The "Wire Bender" 🔩🏆

### Why the Wire Bender Wins
1.  **Hardware Alignment**: You already have the ESP32-S3s, Nema 17 motors, and A4988 drivers. The marginal cost is ~$50.
2.  **Unique Market Position**: Almost **no one** is selling algorithmically-bent wire sculptures. You would be first.
3.  **Heritage Tie-In**: Your "Copper Rebar" concept from the Structural Analyzer is already designed for this. The wire IS the rebar.
4.  **Premium Pricing**: Metal art commands higher prices than plastic. A wire Polar Bear could sell for $200-$500.
5.  **Show Stopper**: A machine that bends wire into a sculpture in real-time is hypnotic at markets.

### Immediate Action Plan (Wire Bender)
**Week 1:**
- [ ] Fork `jpraus/wirebender` on GitHub.
- [ ] Order 3x Nema 17 motors and 3x A4988 drivers (~$40).
- [ ] Source copper wire from old extension cords or thrift store electronics.

**Week 2-3:**
- [ ] 3D print the bending die and feed mechanism from STL files.
- [ ] Write `csv_to_bend_gcode.py` to convert your `bear_path.csv` into bend commands.
- [ ] First "dry run" with cheap aluminum wire.

**Week 4:**
- [ ] First complete **"One Wire Polar Bear"** sculpture.
- [ ] Photograph for social media and Etsy listing.

---

## Bonus: Hybrid Approach
Combine the **Wire Bender** and the **Pen Plotter**.
1.  The **Pen Plotter** draws the 2D "blueprint" on archival paper.
2.  The **Wire Bender** creates the 3D "skeleton" from the same path data.
3.  Sell them as a **"Blueprint + Sculpture" bundle** ($300-$800).

This tells a complete story: "Here is the algorithm (the drawing), and here is the artifact it produced (the wire)."
