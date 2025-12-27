# Plan: Material Characterizer Implementation

## Phase 1: Software Foundation (The "Brain")
- [ ] **Step 1.1**: Initialize a Python environment on the **Raspberry Pi** with `opencv-python`.
- [ ] **Step 1.2**: Update `characterizer_vision.py` to accept an IP Camera stream from the **Old Phone**.
- [ ] **Step 1.3**: Write the `esp32_hx711_streamer.ino` for the **ESP32-S3** to push load cell data via WebSockets or Serial.

## Phase 2: Hardware Assembly (The "Body")
- [ ] **Step 2.1**: Build the **Manual Winch**: A simple rig where turning a knob pulls the grass against the stationary load cell.
- [ ] **Step 2.2**: Mount the **Old Phone** on a fixed tripod or bracket to ensure consistent distance for CV calibration.
- [ ] **Step 2.3**: Calibrate the system using kitchen weights (e.g., 500g of flour = 4.9 Newtons).

## Phase 3: Data Collection (The "Soul")
- [ ] **Step 3.1**: Run a batch of 50 tests.
- [ ] **Step 3.2**: Export the data to a structured `material_library.csv`.
- [ ] **Step 3.3**: Analyze data to determine the "Elastic Modulus" of sweetgrass.

## Future Integration
- [ ] Inject the `material_library.csv` parameters into **NVIDIA Isaac Gym** for the first bimanual weaving sim.
