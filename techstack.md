# Tech Stack: Lowcountry Generative

## Frontend / Mobile
- **Frame**: React Native / Expo (Core App)
- **AR**: ViroReact or Google Geospatial API (ARCore)
- **Haptics**: Pixel Watch / Android Wear SDK

## Backend / AI
- **Reasoning**: Google Gemini 1.5 Pro (via @google/generative-ai)
- **Computer Vision**: OpenCV (Python) for diameter and surface analysis.
- **Simulation**: NVIDIA Isaac Gym (for Reinforcement Learning)
- **Robotics Policy**: ALOHA / ACT (Action Chunking with Transformers)
- **Database**: InfluxDB (for real-time material characterization data)

## Hardware
- **Compute**: Minisforum N5 NAS (Ryzen AI 9 HX 370)
- **GPU**: MSI RTX 5060 Ti 16GB (eGPU via OCuLink)
- **Edge Sensors**: S-Beam Load Cell + HX711 (Tensile Testing)
- **Robotics**: Bimanual ALOHA-style arms (ViperX/Seeed)
