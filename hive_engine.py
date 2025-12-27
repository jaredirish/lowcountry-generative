import time
import json
import pandas as pd
from material_manager import MaterialManager

class HiveEngine:
    """
    The Master Controller running on the Raspberry Pi.
    Coordinates between the Slicer output and the ESP32 hardware nodes.
    """
    def __init__(self, path_csv, stitch_csv):
        self.path_data = pd.read_csv(path_csv)
        self.stitch_data = pd.read_csv(stitch_csv)
        self.mm = MaterialManager()
        
        self.is_running = False
        self.current_step = 0
        self.current_tension = 0.0 # Feedback from ESP32
        
        # PRODUCTION LOGGING (For NVIDIA Isaac Gym Injection)
        self.log_filename = f"production_log_{int(time.time())}.csv"
        self.production_log = []
        
    def start_production(self):
        print("--- HIVE ENGINE: PRODUCTION START ---")
        self.is_running = True
        
        # Determine material properties for safety
        # Assuming the path shows the material ID in column 3
        mat_id = int(self.path_data.iloc[0, 3])
        # Find material by ID
        material = next((m for m in self.mm.materials.values() if m['id'] == mat_id), self.mm.materials['sweetgrass'])
        
        self.max_allowed_tension = material['tensile_strength'] * 0.8 # 20% safety margin
        print(f"Material: {material['display_name']} | Max Safe Tension: {self.max_allowed_tension}N")
        
        for i, row in self.path_data.iterrows():
            if not self.is_running: break
            
            # Use column indices if named access fails
            try:
                x = row['x']
                y = row['y']
                z = row['z']
            except KeyError:
                x = row.iloc[0]
                y = row.iloc[1]
                z = row.iloc[2]

            # 1. PREPARE COMMAND
            target_pos = {
                "x": round(x, 2),
                "y": round(y, 2),
                "z": round(z, 2),
                "action": "move"
            }
            
            # 2. CHECK TENSION (Simulated feedback)
            if self.current_tension > self.max_allowed_tension:
                print(f"WARNING: Tension {self.current_tension}N exceeds limit! Slowing down...")
                time.sleep(0.5) # Wait for material to relax or robot to adjust
            
            # 3. DISPATCH TO ESP32 (Simulated Serial)
            self.dispatch_command(target_pos)
            
            # 4. MONITOR STITCHES
            self.check_and_stitch(i)
            
            # 5. LOG AS-BUILT DATA
            self.log_step(target_pos)
            
            self.current_step = i
            time.sleep(0.01) # Faster simulation

        self.save_production_log()
        print("--- PRODUCTION COMPLETE ---")

    def log_step(self, cmd):
        # We record the COMMANDED vs ACTUAL (simulated) for AI training
        log_entry = {
            "step": self.current_step,
            "x": cmd['x'], "y": cmd['y'], "z": cmd['z'],
            "tension": self.current_tension,
            "timestamp": time.time()
        }
        self.production_log.append(log_entry)

    def save_production_log(self):
        df = pd.DataFrame(self.production_log)
        df.to_csv(self.log_filename, index=False)
        print(f"Production log saved: {self.log_filename}")

    def dispatch_command(self, cmd):
        # In the future, this will use pyserial to talk to your ESP32-S3
        # json_payload = json.dumps(cmd)
        # ser.write(json_payload.encode())
        print(f"STEP {self.current_step}: Moving to {cmd['x']}, {cmd['y']}, {cmd['z']}")

    def check_and_stitch(self, path_idx):
        # Logical check: if path_idx matches a scheduled stitch wrap point
        # This is a placeholder for the more complex alignment logic
        if path_idx % 20 == 0:
            print(f" >> [ACTION] PERFORMING PALMETTO STITCH AT STEP {path_idx}")
            time.sleep(0.2) # Simulate stitching time

    def update_telemetry(self, tension):
        """Called when data arrives from the ESP32 Serial/WebSocket"""
        self.current_tension = tension

if __name__ == "__main__":
    # Test run with the bear we just sliced
    engine = HiveEngine("bear_path.csv", "bear_stitch_map.csv")
    engine.start_production()
