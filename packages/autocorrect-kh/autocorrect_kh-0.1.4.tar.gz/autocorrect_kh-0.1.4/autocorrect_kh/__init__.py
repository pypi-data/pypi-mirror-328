# File: autocorrect_kh/__init__.py
from .autocorrect import (
    normalize_text,
    load_autocorrect_dicts,
    load_autocorrect_dict_file,
    autocorrect_word_in_part,
    autocorrect_address_1,
    autocorrect_address_2,
)
from .settings import PHUM_DICT_FOLDER, KHUM_DICT_FOLDER, DISTRICT_DICT_PATH, PROVINCE_DICT_PATH

# Load dictionaries globally for the user
phum_dict = load_autocorrect_dict_file(PHUM_DICT_FOLDER)
khum_dict = load_autocorrect_dict_file(KHUM_DICT_FOLDER)
district_dict = load_autocorrect_dict_file(DISTRICT_DICT_PATH)
province_dict = load_autocorrect_dict_file(PROVINCE_DICT_PATH)