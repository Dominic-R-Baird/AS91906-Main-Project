import json
from os.path import exists
# defaults
DEFAULTS = {"brightness": 100

}

# constraints
TEST_FILENAME = "test.json"
MIN_BRIGHTNESS = 0
MAX_BRIGHTNESS = 100
class Settings():
    def __init__(self, filename):
        self._filename = filename
        self._settings = DEFAULTS
        # check for file and load settings



    def write_json(self, filename, object):
        try:
            output_file = open(filename, "w", encoding="utf-8")
            output_file.write(json.dumps(object))
            output_file.close()
            return True
        except:
            print("Failed to open file")
            return False

    def write_settings(self):
        result = self.write_json(self._filename, self._settings)
        return result

    def read_json(self, filename):
        try:
           with open(filename, "r", encoding="utf-8") as input_file:
            return json.load(input_file)

        except:
            pass


    def get_brightness(self):
        return self._settings["brightness"]
    def set_brightness(self, brightness):
        if brightness < MIN_BRIGHTNESS:
            print("invalid brightness")
            exit(0)

    brightness = property(get_brightness, set_brightness, None)

if __name__ == "__main__":
    print("testing not yet implemented")
    my_setting = Settings(TEST_FILENAME)