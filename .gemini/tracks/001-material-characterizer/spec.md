# Spec: Material Characterizer (Sprint 1)

## Problem
Neural networks and physical robots require quantitative data to handle organic materials. we cannot train an AI to weave sweetgrass if it doesn't know when the grass will snap or how much its radius tapers.

## Objective
Build a "Hacker's" benchtop rig to characterize sweetgrass and recycled materials using available hardware.

## Functional Requirements
1. **Dimensional Analysis**: Use an **Old Phone** as a 4K vision sensor to measure the radius of a strand.
2. **Tensile Testing**: Measure the force (Newtons) using a **Manual Winch** (screw-drive) against a load cell.
3. **The Hub**: Use a **Raspberry Pi** to run the CV scripts and aggregate data from the sensors.
4. **The Interface**: Use an **ESP32-S3** to read the HX711 Load Cell amplifier and stream data to the Pi.

## Hardware Components (Phase 1)
- **Mechanical**: Manual Winch (e.g., a threaded rod or simple pulley) to provide steady tension.
- **Load Cell**: 5kg S-Beam.
- **Amplifier**: HX711.
- **Vision Node**: High-end Old Phone (used as an IP Camera).
- **Control**: Raspberry Pi + ESP32-S3.

## Success Metrics
- Successfully characterize 50 strands of local sweetgrass.
- Generate a "Material Profile" JSON for each strand.
- Accuracy: +/- 0.1mm for radius and +/- 0.1N for force.
