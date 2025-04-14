import yaml
from pathlib import Path


def load_config(config_name: str = "settings.yaml") -> dict:
    config_path = Path(__file__).parent.parent / "config" / config_name
    with open(config_path, "r") as f:
        return yaml.safe_load(f)
