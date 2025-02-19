import os
import json
from typing import Optional, Dict, Any
from pathlib import Path

DEFAULT_CONFIG_PATH = Path.home() / ".config" / "bike4py" / "config.json"

def load_config(config_path: Optional[Path] = None) -> Dict[str, Any]:
    """Load configuration from file"""
    path = config_path or DEFAULT_CONFIG_PATH
    
    if not path.exists():
        return {}
    
    with open(path) as f:
        return json.load(f)

def save_config(config: Dict[str, Any], config_path: Optional[Path] = None) -> None:
    """Save configuration to file"""
    path = config_path or DEFAULT_CONFIG_PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(path, 'w') as f:
        json.dump(config, f, indent=2) 