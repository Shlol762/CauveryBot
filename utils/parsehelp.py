import json
from discord.ext.commands import Command


def parse_help(command: Command) -> str:
    with open("C:/Users/Shlok/CauveryBot/json/help.json", "r") as f:
        help_: dict = json.load(f)
    return ''.join(help_[command.name.lower()])
