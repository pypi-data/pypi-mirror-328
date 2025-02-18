import os
import sys
from functools import lru_cache
from pathlib import Path
import configparser

HOME_DIR = Path.home()
SETTINGS_DIR = HOME_DIR / ".geai"
SETTINGS_DIR.mkdir(parents=True, exist_ok=True)


class SettingsManager:
    """
    Base class to handle settings.
    If environment variables are defined, it retrieves settings from them first.
    Else, it looks for settings in the .geai/credentials file
    """

    GEAI_SETTINGS_DIR = str(SETTINGS_DIR)
    GEAI_CREDS_FILE = SETTINGS_DIR / "credentials"

    def __init__(self):
        self.config = configparser.ConfigParser()

        if self.GEAI_CREDS_FILE.exists():
            self.config.read(self.GEAI_CREDS_FILE)
        else:
            self.GEAI_CREDS_FILE.touch()
            # raise FileNotFoundError(f"Credentials file not found at {self.GEAI_CREDS_FILE}")
            sys.stdout.write(f"INFO: Credentials file not found. Creating empty one at {self.GEAI_CREDS_FILE}\n")

    def get_setting_value(self, setting_key: str, alias: str):
        """Reads a setting value for a specific alias from the credentials file."""
        if alias not in self.config:
            raise ValueError(f"Alias '{alias}' not found in the credentials file.")

        if setting_key not in self.config[alias]:
            raise ValueError(f"'{setting_key}' not found in alias '{alias}' in the credentials file.")

        return self.config[alias][setting_key]

    def set_setting_value(self, setting_key: str, setting_value: str, alias: str):
        """Writes or updates a setting value for a specific alias in the credentials file."""
        if alias not in self.config:
            self.config.add_section(alias)

        self.config[alias][setting_key] = setting_value

        with self.GEAI_CREDS_FILE.open("w") as file:
            self.config.write(file)

    def get_api_key(self, alias: str = "default"):
        api_key = os.environ.get("GEAI_API_KEY") if alias == "default" else None
        if not api_key:
            api_key = self.get_setting_value("GEAI_API_KEY", alias)

        return api_key

    def set_api_key(self, api_key, alias: str = "default"):
        self.set_setting_value("GEAI_API_KEY", api_key, alias)

    def get_base_url(self, alias: str = "default"):
        base_url = os.environ.get("GEAI_API_BASE_URL") if alias == "default" else None
        if not base_url:
            base_url = self.get_setting_value("GEAI_API_BASE_URL", alias)

        return base_url

    def set_base_url(self, base_url, alias: str = "default"):
        self.set_setting_value("GEAI_API_BASE_URL", base_url, alias)


@lru_cache()
def get_settings():
    return SettingsManager()


if __name__ == "__main__":
    settings = get_settings()
    geai_api_key = settings.get_api_key()
    geai_base_url = settings.get_base_url()
    print(f"api_key: {geai_api_key}")
    print(f"base_url: {geai_base_url}")