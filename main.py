import os
import re

import discord
from discord.ext import commands
from asyncio import get_event_loop


if __name__ != "__main__":
    print(f"Warning! '{__name__}.py' is not importable!")
    exit()


with open("C:/Users/Shlok/bot_stuff/safe_docs/cauverytoken.txt", 'r') as f:
    token: str = f.read()


intents = discord.Intents.all()
bot = commands.AutoShardedBot('!', case_insensitive=True, intents=intents,
                              allowed_mentions=discord.AllowedMentions(everyone=False),
                              status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching,
                                                                                   name="over cauvery!"))


for cog in os.listdir("C:/Users/Shlok/CauveryBot/cogs"):
    if re.search(r"\.py", cog) and cog != '__init__.py':
        bot.load_extension(f'cogs.{cog[:-3]}')


loop = get_event_loop()
try:
    loop.run_until_complete(bot.start(token))
except (KeyboardInterrupt, RuntimeError):
    loop.run_until_complete(bot.close())
finally:
    loop.close()
