from discord import *
from typing import Callable, Union, Coroutine
from functools import wraps
import re, inspect
from datetime import datetime


LOGS = {
    'core': 'C:/Users/Shlok/CauveryBot/logs/core-log'
}
FILES = {
    'on_message_delete': '/logs/msgdel',
    'on_shard_connect': '/logs/shards',
    'on_shard_disconnect': '/logs/shards',
    'on_shard_resumed': '/logs/shards',
    'on_command_error': '/logs/command-error',
    'on_error': '/logs/error'
}


def log_entry_parser() -> int:
    with open(LOGS['core'], 'r') as f:
        match = hex(int(re.search(r"\[#([a-f0-9]{4})]", f.readlines()[-1]).group(1), base=16))
    return match


def logger(func: Union[Callable, Coroutine]):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        name = func.__name__
        with open(LOGS['core'], 'a') as f:
            print(f'Log Entry [#{hex(int(log_entry_parser(), base=16)+1).removeprefix("0x"):0>4}]: '
                  f'Event -> {name.replace("_", " ").title():<19}| '
                  f'Time -> {datetime.now().strftime("%d %B %Y at %X:%f")}| '
                  f'File -> {FILES[name]}', file=f)
        await func(*args, **kwargs)

    return wrapper
