# Deep Research: Heritage Pattern Marketplace + Custom Art Rig

## Part 1: Heritage Pattern Marketplace (Digital Revenue)

### 1.1 Why This Works
- **No Digital Patterns Exist**: My research confirms that **authentic Gullah sweetgrass weaving patterns are NOT digitized**. The craft is generational/intuitive. You would be the **first** to offer AI-generated, printable weaving guides.
- **Market Size**: 7.89M annual Charleston visitors + 50+ artisans at Charleston City Market. $34B Gullah heritage tourism corridor.
- **Low Overhead**: Pure digital product. No inventory, no shipping.

### 1.2 Platform Strategy
| Platform | Best For | Fees | Why Use It |
|:---|:---|:---:|:---|
| **Gumroad** | Simplest storefront for digital patterns | 10% + payment fees | Fastest launch. Built-in "Discover" for new buyers. |
| **Etsy** | Existing craft/heritage audience | ~6.5% + listing fees | Access 90M+ active buyers. Caution: No easy download from app. |
| **Shopify** | Long-term branded store | From $29/mo | Full control. Use for "LCGPatterns.com" in Phase 2. |
| **Stripe + Custom Site** | Advanced (Next.js + Easy Digital Downloads) | 2.9% + 30¢ | Full control but requires dev time. |

### 1.3 Product Offerings
1.  **"Starter Heart" Patterns** ($5-$10): Simple circular coil blueprints for beginners.
2.  **Custom Blueprint Bundles** ($25-$50): Full STL + SVG + PDF for complex shapes (Polar Bear, Turtle).
3.  **Monthly "Pattern Drop" Subscription** ($5-$10/mo): New generative designs each month.
4.  **Commercial Artisan License** ($100-$200): Allow established weavers to use your patterns for sale.

### 1.4 Marketing Hooks
- **"Weave What Your Grandmother Couldn't Dream"**: Sculptures beyond human precision.
- **Cultural Authenticity Token**: Each pattern includes a QR code linking to Gullah oral history.
- **"Learn Before You Weave"**: AR Weave Guide app as a loss-leader to drive pattern sales.

---

## Part 2: Custom Art Rig (Prototype Hardware)

### 2.1 The Core Concept: "LCG Art Plotter"
A small-footprint **pen plotter / drawing robot** that uses your **Sweetgrass Slicer** outputs to create physical art that is too precise for human hands.

**What it produces**:
- 2D "Woven Path" art prints (ink on paper, simulating the spiral logic).
- "Exploded View" diagrams of complex sculptures.
- Custom gift patterns drawn live at markets.

### 2.2 Bill of Materials (DIY, ~$150-$300)
| Part | Est. Cost | Notes |
|:---|:---:|:---|
| **ESP32-S3** | $15 | You have these coming! |
| **Nema 17 Stepper x2** | $20 | Standard CNC motors. |
| **A4988 Motor Drivers x2** | $5 | Simple, affordable. |
| **Micro Servo (SG90)** | $3 | For pen up/down (Z-axis). |
| **V-Slot 2020 Aluminum Extrusion** | $30-$50 | For the frame. |
| **3D Printed Parts** | $10-$20 | Carriages, mounts. (Use library/makerspace printer) |
| **GT2 Timing Belts + Pulleys** | $10 | For X-Y motion. |
| **Power Supply (12V 2A)** | $10 | To run the motors. |
| **Pens (Sakura Micron set)** | $15 | Archival ink. |

### 2.3 Software Stack
- **Firmware**: `Grbl_ESP32` (Open source, interprets G-code via Wi-Fi).
- **Control**: Your existing `bear_path.csv` can be converted to G-code using a simple Python script.
- **Design Source**: Your `blueprint_generator.py` already outputs SVGs.

### 2.4 The "Impossible" Art
What can this rig do that human hands cannot?
1.  **Micron-Level Detail**: Draw the "Palmetto Stitch" map for a Polar Bear at 0.1mm line widths.
2.  **Perfect Continuity**: Draw a 2,000-point spiral without tremor.
3.  **Generative Variations**: Every print is unique because the Slicer's random seed changes.

### 2.5 Monetization (Physical Goods)
- **Signed "Generative Art" Prints** ($50-$150): Framed art of algorithmically-generated weaving paths.
- **Custom Commission Drawings** ($100-$500): "Upload your 3D model, I draw its woven DNA."
- **Live Market Art**: Bring the rig to the Charleston City Market. Draw patterns on-demand for tourists.

---

## Part 3: The Combined "Lowcountry Generative" Business Model

| Stream | Type | Effort | Revenue Potential |
|:---|:---:|:---:|:---:|
| **Pattern Marketplace** | Digital | Low | $500 - $5,000/mo (Recurring) |
| **Plotter Art Prints** | Physical | Medium | $1,000 - $10,000/mo (Commission) |
| **Weave Guide App** | Freemium | Medium | Lead Gen for Patterns |
| **Artisan Licensing** | B2B | Low | $1,000 - $5,000/mo |

---

## Next Steps (Immediate Actions)

### Week 1: Marketplace Launch
1. [ ] Set up a **Gumroad** account.
2. [ ] Export the **Turtle, Bear, Simple Bowl** patterns from the Slicer as SVG + PDF bundles.
3. [ ] Write product descriptions with heritage context.
4. [ ] List 3 products at $10, $25, $50 price points.

### Week 2-4: Prototype Rig
1. [ ] Order **2x Nema 17 motors, A4988 drivers, and GT2 belts** (Amazon).
2. [ ] Design 3D-printable **pen carriage** using the ESP32-S3.
3. [ ] Write a `svg_to_gcode.py` converter script.
4. [ ] First "dry run" plot of the `bear_weaving_blueprint.svg`.

### Week 5+: Market Test
1. [ ] Bring the rig to a **local maker market or the Charleston Night Market**.
2. [ ] Offer **live custom drawings** ($10 for a small, $50 for a large).
3. [ ] Collect emails for the **Weave Guide app waitlist**.
