# Autocorrect for Khmer National ID Addresses (`autocorrect_kh`)

This Python script (`autocorrect.py`) provides an autocorrection tool for Khmer addresses on Cambodian National ID cards. It processes addresses in two parts—`address_1` (house, road, village) and `address_2` (commune, district, province)—using dictionary-based correction and custom rules tailored to Khmer script.

![Khmer Address Correction Example](sample.png)

## Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Key Functions](#key-functions)

## Features
- Khmer Address Correction: Fixes typos and misspellings in Khmer addresses.
- Two-Part Processing: Splits addresses into `address_1` (ផ្ទះ, ផ្លូវ, ភូមិ) and `address_2` (ឃុំ, district, province).
- Dictionary Support: Loads correction dictionaries from text files or folders.
- Custom Logic: Handles unique Khmer terms like ផ្ទះ (house) and ផ្លូវ (road) with specific rules.
- Unicode Normalization: Ensures consistent Khmer text processing.

## Requirements
- Python 3.x
- Required packages:
    - `jellyfish` (for Damerau-Levenshtein distance)
    - `regex` (for advanced pattern matching)
    - `unicodedata` (included in Python standard library)
    - `pkg_resources` (included with `setuptools`)


## Installation

Install the library via `pip`:

```bash
pip install autocorrect_kh jellyfish regex
```

Or Install from source

```bash
git clone https://github.com/monykappa/autocorrect-kh.git
```

## Usage

```bash
from autocorrect import autocorrect_address_1, autocorrect_address_2, phum_dict, khum_dict, district_dict, province_dict

# Example of misspelled address
address_1 = "ផ្ទ៤១បេ ផ្លុវ៤៤៤ ភុមិ២"
address_2 = "សង្កាត់ទលទពូងទី ២ ខណ្ឌចំករមន ភ្នំពញ"

# Correct the address
corrected_address_1 = autocorrect_address_1(address_1, phum_dict)
corrected_address_2 = autocorrect_address_2(address_2, khum_dict, district_dict, province_dict)

print(corrected_address_1)  # Output: ផ្ទះ៤១បេ ផ្លូវ៤៤៤ ភូមិ២
print(corrected_address_2)  # Output: សង្កាត់ទួលទំពូងទី២ ខណ្ឌចំការមន ភ្នំពេញ
```

# How It Works
## Address Breakdown
Khmer National ID addresses are split into:

1. `address_1:` Contains ផ្ទះ (house), ផ្លូវ (road), and ភូមិ (village/phum).
2. `address_2`: Contains ឃុំ/សង្កាត់ (commune/khum), district, and province.

## Correction Flow
### Address 1: House, Road, Village
- ផ្ទះ (House) and ផ្លូវ (Road):
    - Corrected using hardcoded rules (not from dictionaries) due to their unique patterns, often followed by numbers or identifiers.
    - Examples:
        - `ផ្ទ១១៣` → `ផ្ទះ១១៣` 
        - `ផ្លូរបេតុង` → `ផ្លូវបេតុង` 
- ភូមិ (Village/Phum):
    - First checks and corrects the prefix ភូមិ (e.g., `ភុមិ` → `ភូមិ`).
    - Then corrects the village name after ភូមិ using the phum_dict (loaded from data/phum/).
    - Note: The phum dictionary excludes the word ភូមិ because it’s inconsistently present on ID cards.
    - Example:
        - Input: `ភុមិស្វយព្រៃ`
        - Step 1: `ភុមិ` → `ភូមិ`
        - Step 2: `ស្វយព្រៃ` → `ស្វាយព្រៃ` (using phum_dict)
        - Output: `ភូមិស្វាយព្រៃ`
### Address 2: Commune, District, Province
- Corrected directly using dictionaries (khum_dict, district_dict, province_dict) loaded from data/khum/, data/district.txt, and data/province.txt.
- No prefix-specific rules; full names are matched and corrected.
- Example:
    - Input: `ឃុំស្វាយ ស្រុកកំពង់ ខេត្តកំពត`
    - Output: `ឃុំស្វាយ ស្រុកកំពង់ចាឮ ខេត្តកំពត` (corrected using dictionaries)

# Key Functions
- `normalize_text(text)`: Normalizes Khmer Unicode to NFC for consistent processing.
- `load_resource_text(resource_path)`: Loads raw text from a package resource file.
- `load_autocorrect_dict_from_resource(resource_path)`: Loads a dictionary from a single text file (e.g., `district.txt`).
- `load_autocorrect_dicts_from_resource(folder_resource)`: Loads dictionaries from all `.txt` files in a folder (e.g., `data/phum/`).
- `autocorrect_word(word, word_set)`: Corrects a word using Damerau-Levenshtein distance.
- `autocorrect_address_1(part, dictionary)`: Corrects `address_1` with custom rules.
- `autocorrect_address_2(address_2_text, khum_dict, district_dict, province_dict)`: Corrects `address_2 `components.