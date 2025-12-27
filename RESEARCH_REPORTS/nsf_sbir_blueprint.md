# NSF SBIR Phase I: Technical Blueprint for "Assistive Organic Textiles"

## 1. The Innovation: Physics-Aware Non-Rigid Manipulation
Current robotic manufacturing excels at rigid parts (cars, electronics). However, manipulating high-friction, non-linear organic materials like **Sweetgrass** and **Palmetto** is an unsolved "Grand Challenge" in robotics. 

LCG's innovation is the **Sweetgrass Slicer & Hive Engine**, which uses real-time tension feedback to compensate for the material's unpredictable elastic modulus.

## 2. Technical Objectives (Phase I)
- **Objective 1: Parameterization of Organic Slender Members.** 
    - Task: Use the "Material Characterizer" rig to generate a dataset of 500+ grass strands, mapping diameter taper to tensile strength.
- **Objective 2: Real-time Tension-Control Loop.** 
    - Task: Develop a 1000Hz feedback loop on the ESP32-S3 that adjusts motor torque to stay within 5% of the material's local "Snap Point."
- **Objective 3: Branching Topology Algorithms.** 
    - Task: Solve the mathematical "Branching" problem where a continuous spiral must split into multiple sub-spirals (e.g., legs of a chair or limbs of an assistive garment).

## 3. Commercial & Societal Impact
- **Assistive Technology**: Applying the "Woven STL" logic to create custom-fit, breathable, structural support garments for the elderly or disabled.
- **Sustainability**: Converting ocean-bound PET plastic into "Heritage Grade" materials, creating a circular economy for coastal communities.
- **Cultural Preservation**: Digitizing the 300-year-old dexterity of Gullah-Geechee masters, ensuring the craft outlives its physical limitations.

## 4. Technical Risk (The "SBIR Hook")
The primary risk is **Physical Hysteresis**. Unlike plastic filament, organic grass has a "memory" and changes behavior based on humidity and age. LCG's AI-driven approach is the only way to manufacture with these materials at scale.
