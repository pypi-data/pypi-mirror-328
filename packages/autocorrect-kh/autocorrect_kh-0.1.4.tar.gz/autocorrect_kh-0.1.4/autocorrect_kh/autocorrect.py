import glob
import os, re, json, unicodedata
import regex, jellyfish, pkg_resources
from . import settings

# Words to exclude and target words.
words_exclude = {"ផ្ទះ", "ផ្លូវ"}
targets = {"ផ្ទះ", "ផ្លូវ", "ភូមិ"}

# Global dictionary variables
phum_dict = set()
khum_dict = set()
district_dict = set()
province_dict = set()

# Convert string to NFC form.
def normalize_text(text: str) -> str:
    return unicodedata.normalize("NFC", text)

# Load words from all txt files in a folder.
def load_autocorrect_dicts(folder_name):
    base_path = pkg_resources.resource_filename(__name__, f"data/{folder_name}")
    all_lines = []
    for file in os.listdir(base_path):
        if file.endswith(".txt"):
            with open(os.path.join(base_path, file), encoding="utf-8") as f:
                all_lines.extend(f.read().splitlines())
    return all_lines

# Load dictionary from a single txt file.
def load_autocorrect_dict_file(file_name):
    base_path = pkg_resources.resource_filename(__name__, f"data/{file_name}")
    with open(base_path, encoding="utf-8") as f:
        return f.read().splitlines()

# Automatically load all dictionaries when the module is imported
def load_all_dictionaries():
    global phum_dict, khum_dict, district_dict, province_dict

    phum_dict_paths = glob.glob(pkg_resources.resource_filename(__name__, f'data/{settings.PHUM_DICT_FOLDER}/*.txt'))
    khum_dict_paths = glob.glob(pkg_resources.resource_filename(__name__, f'data/{settings.KHUM_DICT_FOLDER}/*.txt'))
    
    # Load phum and khum dictionaries
    for dict_path in phum_dict_paths:
        phum_dict.update(load_autocorrect_dict_file(dict_path))

    for dict_path in khum_dict_paths:
        khum_dict.update(load_autocorrect_dict_file(dict_path))

    # Load district and province dictionaries
    district_dict_path = pkg_resources.resource_filename(__name__, f'data/{settings.DISTRICT_DICT_PATH}')
    province_dict_path = pkg_resources.resource_filename(__name__, f'data/{settings.PROVINCE_DICT_PATH}')
    
    district_dict.update(load_autocorrect_dict_file(district_dict_path))
    province_dict.update(load_autocorrect_dict_file(province_dict_path))

# Call the load_all_dictionaries function automatically when the package is imported
load_all_dictionaries()

# Correct a word using Damerau-Levenshtein distance.
def autocorrect_word(word: str, word_set: set, max_ratio: float = 0.4, max_typo_distance: int = None) -> list:
    word = normalize_text(word)
    if word in word_set:
        return [word]
    max_typo_distance = max(3, int(len(word)*0.4)) if max_typo_distance is None else max_typo_distance
    best_candidate, best_ratio = None, float("inf")
    for correct in word_set:
        d = jellyfish.damerau_levenshtein_distance(word, correct)
        ratio = d/max(len(word), len(correct))
        if d <= max_typo_distance or ratio <= max_ratio:
            if ratio < best_ratio:
                best_ratio, best_candidate = ratio, correct
    if any("០" <= ch <= "៩" for ch in word) and not (best_candidate and any("០" <= ch <= "៩" for ch in best_candidate)):
        return [word]
    return [word] if best_candidate is None or best_ratio > 0.20 else [best_candidate]

# Check if word is numeric.
def is_number(word: str) -> bool:
    return re.sub(r"[\u200B-\u200D\uFEFF]", "", word).strip().isdigit()

# Merge target words with following alphanumeric token.
def merge_tokens(part: str) -> str:
    tokens, merged, i = part.split(), [], 0
    while i < len(tokens):
        if tokens[i] in targets and i+1 < len(tokens) and re.search(r"[A-Za-z0-9]", tokens[i+1]):
            merged.append(tokens[i] + tokens[i+1])
            i += 2
        else:
            merged.append(tokens[i])
            i += 1
    return " ".join(merged)

# Autocorrect individual word in a text part.
def autocorrect_word_in_part(word, dictionary):
    word = normalize_text(word)
    if is_number(word) or word in words_exclude:
        return word
    if word.startswith("ផ្ល"):
        m = re.search(r"\d", word)
        if m:
            return "ផ្លូវ" + word[m.start():]
    for t in targets:
        if word.startswith(t):
            rem = word[len(t):]
            return t if t=="ភូមិ" and not rem.strip() else t + (autocorrect_word(rem, dictionary)[0] if t=="ភូមិ" else rem)
    clusters = regex.findall(r"\X", word)
    best_target, best_n, best_distance = None, 0, float("inf")
    for t in targets:
        t_clusters = regex.findall(r"\X", t)
        if len(clusters) < len(t_clusters): continue
        d = jellyfish.damerau_levenshtein_distance("".join(clusters[:len(t_clusters)]), t)
        if d < best_distance:
            best_distance, best_target, best_n = d, t, len(t_clusters)
    if best_target and best_distance <= 1:
        rem = "".join(clusters[best_n:])
        if best_target=="ភូមិ":
            res = autocorrect_word(rem, dictionary)
            return best_target if not rem.strip() else best_target + (res[0] if res else rem)
        if best_target=="ផ្ទះ" and rem.startswith("ទ"):
            rem = rem[1:]
        return best_target + rem
    return word if word in dictionary else (autocorrect_word(word, dictionary)[0] or word)

# Autocorrect each token in a text part.
def autocorrect_address_1(part, dictionary):
    return " ".join(autocorrect_word_in_part(w, settings.PHUM_DICT_FOLDER) for w in merge_tokens(part).split())

# Autocorrect address_2 components based on token index.
def autocorrect_address_2(address_2_text, khum_dict, district_dict, province_dict):
    parts = address_2_text.split()
    if parts and len(parts) >= 2 and parts[1].isdigit():
        commune = parts[0] + parts[1]
        district = parts[2] if len(parts) > 2 else ""
        province = " ".join(parts[3:]) if len(parts) > 3 else ""
    elif len(parts) >= 4:
        commune, district, *prov = parts
        province = " ".join(prov)
    elif len(parts) == 3:
        commune, district, province = parts
    else:
        commune = parts[0] if parts else ""
        district = province = ""
    corr_commune = autocorrect_word(commune, settings.KHUM_DICT_FOLDER, max_ratio=0.6)[0]
    corr_district = autocorrect_word(district, settings.DISTRICT_DICT_PATH, max_ratio=0.6)[0] if district else ""
    corr_province = autocorrect_word(province, settings.PROVINCE_DICT_PATH, max_ratio=0.6)[0] if province else ""
    return " ".join(filter(None, [corr_commune, corr_district, corr_province]))
