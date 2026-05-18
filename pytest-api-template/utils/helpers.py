import json
from pathlib import Path
from typing import Any, Dict

def load_json(file_path: str) -> Dict[str, Any]:
    """Loads a JSON file and returns its content as a dictionary."""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"JSON file not found: {file_path}")
    
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(file_path: str, data: Dict[str, Any]):
    """Saves a dictionary as a JSON file."""
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
