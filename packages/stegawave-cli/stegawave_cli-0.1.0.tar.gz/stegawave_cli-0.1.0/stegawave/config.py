# stegawave/config.py
import os
from pathlib import Path
import json
from typing import Optional

CONFIG_DIR = Path.home() / ".stegawave"
CONFIG_FILE = CONFIG_DIR / "config.json"

class Config:
    def __init__(self):
        self.api_key: Optional[str] = None
        self.api_url: str = "https://api.stegawave.com/v1"
        self.load()

    def load(self) -> None:
        """Load configuration from file."""
        if not CONFIG_FILE.exists():
            return

        try:
            with open(CONFIG_FILE) as f:
                config = json.load(f)
                self.api_key = config.get("api_key")
                self.api_url = config.get("api_url", self.api_url)
        except Exception as e:
            print(f"Error loading config: {e}")

    def save(self) -> None:
        """Save configuration to file."""
        CONFIG_DIR.mkdir(exist_ok=True)
        
        config = {
            "api_key": self.api_key,
            "api_url": self.api_url
        }

        with open(CONFIG_FILE, "w") as f:
            json.dump(config, f, indent=2)

    def set_api_key(self, api_key: str) -> None:
        """Set and save API key."""
        self.api_key = api_key
        self.save()

config = Config()