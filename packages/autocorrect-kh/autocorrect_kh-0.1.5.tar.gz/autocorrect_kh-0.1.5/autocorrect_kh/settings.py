import os

# Get the absolute path to the root project directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Adjust paths to point to the correct location
PHUM_DICT_FOLDER = os.path.join(BASE_DIR, "data", "phum")
KHUM_DICT_FOLDER = os.path.join(BASE_DIR, "data", "khum")
DISTRICT_DICT_PATH = os.path.join(BASE_DIR, "data", "district.txt")
PROVINCE_DICT_PATH = os.path.join(BASE_DIR, "data", "province.txt")
