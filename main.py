import discord
from discord.ext import commands
from asyncio import get_event_loop


if __name__ != "__main__":
    print(f"Warning! '{__name__}.py' is not importable!")
    exit()


with open("C:/Users/Shlok/bot_stuff/safe_docs/cauverytoken.txt", 'r') as f:
    token: str = f.read()


bot = commands.AutoShardedBot('!', case_insensitive=True)


loop = get_event_loop()
try:
    loop.run_until_complete(bot.start(token))
except (KeyboardInterrupt, RuntimeError):
    loop.run_until_complete(bot.close())
finally:
    loop.close()
