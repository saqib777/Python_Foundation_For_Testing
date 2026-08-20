# Test data loader utility
# Reads test data from JSON files and provides typed access

import json
import os
from typing import Any


class TestDataLoader:
    """
    Loads test data from JSON files in the data/ directory.
    Provides type-safe accessor methods with sensible defaults.

    Usage:
        loader = TestDataLoader()
        user   = loader.get("login.valid_user")
        email  = loader.get("login.valid_user.email")
    """

    def __init__(self, data_dir: str = None):
        self.data_dir = data_dir or os.path.join(
            os.path.dirname(__file__), '..', 'data'
        )
        self._cache: dict = {}

    def _load_file(self, filename: str) -> dict:
        if filename not in self._cache:
            filepath = os.path.join(self.data_dir, filename)
            if not os.path.exists(filepath):
                raise FileNotFoundError(f"Test data file not found: {filepath}")
            with open(filepath, 'r', encoding='utf-8') as f:
                self._cache[filename] = json.load(f)
        return self._cache[filename]

    def get(self, key_path: str, filename: str = "test_data.json",
            default: Any = None) -> Any:
        """
        Get a value using dot-notation key path.

        Examples:
            loader.get("login.valid_user.email")
            loader.get("api.base_url")
            loader.get("registration.invalid_emails")
        """
        try:
            data  = self._load_file(filename)
            keys  = key_path.split(".")
            value = data
            for key in keys:
                value = value[key]
            return value
        except (KeyError, TypeError):
            return default

    def get_user(self, user_type: str = "valid_user") -> dict:
        """Convenience method for login user data."""
        return self.get(f"login.{user_type}", default={})

    def get_api_config(self) -> dict:
        """Convenience method for API configuration."""
        return self.get("api", default={})

    def get_invalid_emails(self) -> list:
        """Convenience method for invalid email test data."""
        return self.get("registration.invalid_emails", default=[])

    def reload(self):
        """Clear cache and force re-read from disk."""
        self._cache.clear()


# ── Module-level singleton for convenience ─────────────────────────────────────
loader = TestDataLoader()


if __name__ == "__main__":
    td = TestDataLoader()
    print(td.get("login.valid_user"))
    print(td.get("api.base_url"))
    print(td.get("nonexistent.key", default="fallback"))
