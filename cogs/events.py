from cogs import Cog, CommandError, CommandOnCooldown,\
    CommandNotFound, AutoShardedBot
from datetime import datetime


LOGS = {
    'shards': 'C:/Users/Shlok/CauveryBot/logs/shards'
}


class Events(Cog):
    def __init__(self, bot: AutoShardedBot):
        self.bot = bot
        self.name = 'Events'
        self.shard: int = 0

    @Cog.listener('on_shard_connect')
    async def on_shard_connect(self, id: int):
        with open(LOGS['shards'], 'a') as f:
            self.shard = id
            print(f"Connection to shard: {id} at {datetime.now().strftime('%d %B %Y at %X:%f')}", file=f)

    @Cog.listener('on_shard_disconnect')
    async def on_shard_disconnect(self, id: int):
        with open(LOGS['shards'], 'a') as f:
            print(f"Disconnected shard : {id} on {datetime.now().strftime('%d %B %Y at %X:%f')}", file=f)

    @Cog.listener('on_shard_resumed')
    async def on_shard_resumed(self, id: int):
        with open(LOGS['shards'], 'a') as f:
            self.shard = id
            print(f'WARNING! Shard continuity fail. {id} != {self.shard}', file=f) if id != self.shard else None
            print(f"Reconnection shard : {id} at {datetime.now().strftime('%d %B %Y at %X:%f')}", file=f)

    @Cog.listener('on_ready')
    async def on_ready(self):
        print(f"{self.bot.user.name} is ready!")



def setup(bot: AutoShardedBot):
    bot.add_cog(Events(bot))
