import os
import re
from pathlib import Path

import requests
import yaml

PALCORD_CONFIG_FILE_PATH = "../PalcordConfig.yaml"


def get_palcord_config(file_path: str, encoding="UTF-8"):
    fixed_file_path = Path(file_path).expanduser().resolve()
    with open(file=fixed_file_path, mode="r", encoding=encoding) as file:
        yaml_doc = yaml.safe_load(file)
    return yaml_doc


os.chdir(Path(__file__).parent)
palcord_config = get_palcord_config(PALCORD_CONFIG_FILE_PATH)
os.chdir(Path(PALCORD_CONFIG_FILE_PATH).expanduser().resolve().parent)


def resolve_path(path: str):
    cwd = os.getcwd()
    os.chdir(Path(PALCORD_CONFIG_FILE_PATH).expanduser().resolve().parent)
    resolved_path = Path(path).expanduser().resolve()
    os.chdir(cwd)
    return resolved_path


def get_ini_config(erase_extra_quot_marks=True, file_encoding="UTF-8"):
    file_path = Path(palcord_config["PalWorldSettings-ini-Path"]).expanduser().resolve()
    with open(file=file_path, mode="r", encoding=file_encoding) as file:
        text = file.read()
    text = text.strip()
    text = re.sub(r"^\s*;.*\n", "", text, flags=re.MULTILINE)  # Delete comment out line
    text = re.search(r"OptionSettings=\((.*)\)\n?", text).group(1)
    config_dict = {}
    for key_value in re.split(r"\s*,\s*", text):
        key, value = re.split(r"\s*=\s*", key_value)
        if erase_extra_quot_marks:
            if re.findall("^'.*'$", value) or re.findall('^".*"$', value):
                value = re.sub("^[\"']", "", value)
                value = re.sub("[\"']$", "", value)
        config_dict[key] = value
    return config_dict


def get_global_ip():
    response = requests.get("http://checkip.dyndns.com/").text
    response = re.sub(r"<[^>]+>", "", response)  # Delete HTML tags
    response = re.sub(r".*: ", "", response)  # Extract IP addr
    response = response.strip()
    return response
