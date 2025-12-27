# Spec: The Sweetgrass Slicer (Track 002)

## Problem
In 3D printing, a slicer turns a model into horizontal layers for a nozzle. But a sweetgrass weaver (human or robot) does not move in flat layers; they move in a **continuous, expanding spiral** (coiling). To automate this, we need a "Non-Planar Conformal Slicer" that understands the constraints of a grass bundle.

## Objective
Develop a generative CAD engine that converts a standard 3D mesh (.obj/.stl) into a single, continuous, non-intersecting spiral path (G-Code for humans/robots).

## Functional Requirements
1. **Conformal Pathing**: The path must follow the outer surface of the 3D model, not just flat slices.
2. **Spiral Continuity**: The algorithm must solve the "Branching Problem"—e.g., how to weave an elephant's legs without "jumping" through empty space.
3. **Variable Bundle Width**: Support for dynamic line-width based on the data we will collect in Track 001.
4. **Instruction Generator**: Export 2D "maps" for human weavers and 3D paths for robots.

## Logic Overview
- **Vase Mode on Steroids**: Use geodesic paths to ensure the coil always has a structural connection to the previous row.
- **Physics Constraint**: Enforce "Minimum Bend Radius"—the path cannot turn sharper than the grass can physically bend.
