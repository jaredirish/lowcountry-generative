import json

class MaterialManager:
    """
    Central registry for all weaving materials and their physical properties.
    """
    DEFAULT_MATERIALS = {
        "sweetgrass": {
            "id": 1,
            "display_name": "Sweetgrass",
            "avg_diameter": 5.0,
            "tensile_strength": 15.0, # Newtons
            "color": "#8b9d77", # Sage Green
            "flexible": True,
            "type": "filler"
        },
        "palmetto": {
            "id": 2,
            "display_name": "Palmetto Strip",
            "avg_diameter": 3.0,
            "tensile_strength": 25.0,
            "color": "#e0d7c6", # Off-white/Cream
            "flexible": False,
            "type": "binder"
        },
        "pine_needle": {
            "id": 3,
            "display_name": "Long-leaf Pine",
            "avg_diameter": 4.0,
            "tensile_strength": 8.0,
            "color": "#6d4c41", # Brown
            "flexible": True,
            "type": "filler"
        },
        "copper_rebar": {
            "id": 4,
            "display_name": "Copper Wire",
            "avg_diameter": 2.0,
            "tensile_strength": 200.0,
            "color": "#b87333", # Copper
            "flexible": False,
            "type": "structure"
        }
    }

    def __init__(self, config_path="materials.json"):
        self.config_path = config_path
        self.materials = self.DEFAULT_MATERIALS

    def get_material(self, name):
        return self.materials.get(name.lower())

    def save_config(self):
        with open(self.config_path, 'w') as f:
            json.dump(self.materials, f, indent=4)

if __name__ == "__main__":
    mm = MaterialManager()
    mm.save_config()
    print("Material Registry Initialized.")
