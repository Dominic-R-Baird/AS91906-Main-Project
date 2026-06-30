"""This file helps to keep a permanent copy of known settings."""

import json

# defaults
DEFAULTS = {"speed": "Slow"}

# constraints
DEFAULT_FILENAME = "settings.json"


class Settings():
    """Represents a permanent copy of known settings."""

    def __init__(self, filename):
        """Initalise the filename and the defaults."""
        self._filename = filename
        self._settings = DEFAULTS
        # check for file and load settings

    def write_json(self, filename, object):
        """Write what you want in one file to json."""
        try:
            output_file = open(filename, "w", encoding="utf-8")
            output_file.write(json.dumps(object))
            output_file.close()
            return True
        except:
            print(f"Failed to open file {filename} for write")
            return False

    def write_settings(self):
        """Write from json into the file chosen."""
        result = self.write_json(self._filename, self._settings)
        return result

    def read_settings(self):
        """Read from the json."""
        result = self.read_json(self._filename)
        if result is not None:
            self._settings = result

    def read_json(self, filename):
        """Read from the json file."""
        try:
            with open(filename, "r", encoding="utf-8") as input_file:
                return json.load(input_file)

        except:
            print(f"file {filename} failed to read/decode.")
            return None

    def get_speed(self):
        """Get the speed."""
        return self._settings["speed"]

    def set_speed(self, speed):
        """Set the speed and make it a property."""
        self._settings["speed"] = speed
    speed = property(get_speed, set_speed, None)


if __name__ == "__main__":
    print("testing not yet implemented")
    my_setting = Settings(DEFAULT_FILENAME)
