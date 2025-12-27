# Spec: The Hive Controller (Track 003)

## Problem
The Slicer (Track 002) generates "Where" to weave, but the Hive Controller determines "How" to move. It must synchronize the high-level path with real-time material tension to ensure the grass doesn't snap.

## Objective
Develop the orchestration layer that runs on the Raspberry Pi, communicating with ESP32-S3 nodes to drive the "Weaving Cell."

## Functional Requirements
1. **Command parsing**: Load `bear_path.csv` and `bear_stitch_map.csv` and convert them into time-sequenced motion packets.
2. **Tension-Feedback Loop**: Adjust motor speed/pull force based on real-time data from the Material Characterizer's load cell.
3. **Multi-Node Sync**: Orchestrate the "Spinner" (the basket base) and the "Tuck-Arm" (the palmetto binder).
4. **Safety Interlocks**: Emergency stop if grass tension exceeds the limit defined in `material_manager.py`.

## Architecture
- **Master Node (Raspberry Pi)**: Runs the Python `HiveEngine`.
- **Slave Nodes (ESP32-S3)**: Handles low-level PWM for motors and HX711 reading.
- **Protocol**: JSON-over-Serial (high frequency) or WebSockets.

## Success Metrics
- Successfully "dry run" the Polar Bear path in a virtual simulation.
- Latency < 10ms between sensor trigger and motor adjustment.
