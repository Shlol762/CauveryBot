from cogs import Cog, CommandError, CommandOnCooldown,\
    CommandNotFound, AutoShardedBot


class Events(Cog):
    def __init__(self, bot: AutoShardedBot):
        self.bot = bot
        self.name = 'Events'

    @Cog.listener('on_ready')
    async def on_ready(self):
        print(f"{self.bot.user.name} is ready!")



def setup(bot: AutoShardedBot):
    bot.add_cog(Events(bot))
