import os
from pathlib import Path
from yaml import safe_load
import discord_bot

VERSION = 1.0
CONFIG_FILE_PATH = "../PalcordConfig.yaml"

def load_config(config_file: str):
    yaml_doc = safe_load(config_file)

if __name__ == "__main__":
    os.chdir(Path(__file__).parent)
    print(f"Palcord v{VERSION}")
    print(f"Loading config file...", end="    ")
    load_config(CONFIG_FILE_PATH)
    print(f"OK")
    print(f"Launching Discord BOT...", end="    ")
    bot = discord_bot.DiscordNotifier()
    print("OK")
    