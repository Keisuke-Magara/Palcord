from __future__ import annotations
from pathlib import Path


def yaml2ini(yaml_file_path: str | Path, ini_file_path: str | Path):
    with open(yaml_file_path, mode="r", encoding="UTF-8") as file:
        