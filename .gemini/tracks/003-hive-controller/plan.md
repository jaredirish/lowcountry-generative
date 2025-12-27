# Plan: Hive Controller Implementation

## Phase 1: Communication Protocol (The "Nervous System")
- [ ] **Step 1.1**: Define a JSON message format for `COMMAND` (Pi -> ESP) and `TELEMETRY` (ESP -> Pi).
- [ ] **Step 1.2**: Write the `esp32_bridge.py` on the Pi to handle asynchronous serial communication.
- [ ] **Step 1.3**: Test connectivity with a dummy ESP32 response.

## Phase 2: Orchestration (The "Cortex")
- [ ] **Step 2.1**: Implement the `HiveEngine` to sequence the CSV waypoints.
- [ ] **Step 2.2**: Integrate the `MaterialManager` to set tension thresholds dynamically.
- [ ] **Step 2.3**: Build the "Tension Compensator"—an algorithm that slows down movement when the grass bundle is getting tight.

## Phase 3: Integration & Safety (The "Reflexes")
- [ ] **Step 3.1**: Implement "Limit Switch" logic to prevent the winch from over-extending.
- [ ] **Step 3.2**: Log all run-data to `production_history.db` for future AI training (NVIDIA Isaac Gym).
