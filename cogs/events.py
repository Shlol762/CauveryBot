from cogs import Cog, CommandError, CommandOnCooldown,\
    CommandNotFound, AutoShardedBot, Message, AuditLogAction,\
    AuditLogEntry, Member, Context, logger, DiscordException
from datetime import datetime, timezone
from pytz import timezone as tz


LOGS = {
    'core': 'C:/Users/Shlok/CauveryBot/logs/core-log',
    'shards': 'C:/Users/Shlok/CauveryBot/logs/shards',
    'del messages': 'C:/Users/Shlok/CauveryBot/logs/msgdel'
}
TIM_FMT = '%d %B %Y at %X:%f'


class Events(Cog):
    def __init__(self, bot: AutoShardedBot):
        self.bot = bot
        self.name = 'Events'
        self.shard: int = 0

    @Cog.listener('on_shard_connect')
    @logger
    async def on_shard_connect(self, id: int):
        with open(LOGS['shards'], 'a') as f:
            self.shard = id
            print(f"Connection to shard: {id} on {datetime.now().strftime(TIM_FMT)}", file=f)

    @Cog.listener('on_shard_disconnect')
    @logger
    async def on_shard_disconnect(self, id: int):
        with open(LOGS['shards'], 'a') as f:
            print(f"Disconnected shard : {id} on {datetime.now().strftime(TIM_FMT)}", file=f)

    @Cog.listener('on_shard_resumed')
    @logger
    async def on_shard_resumed(self, id: int):
        with open(LOGS['shards'], 'a') as f:
            self.shard = id
            print(f'WARNING! Shard continuity fail. {id} != {self.shard}', file=f) if id != self.shard else None
            print(f"Reconnection shard : {id} on {datetime.now().strftime(TIM_FMT)}", file=f)

    @Cog.listener('on_ready')
    async def on_ready(self):
        print(f"{self.bot.user.name} is ready!")

    @Cog.listener('on_message')
    async def on_message(self, message: Message):
        pass

    @Cog.listener('on_message_delete')
    @logger
    async def on_message_delete(self, message: Message):
        ctx: Context = await self.bot.get_context(message)
        time = datetime.now().strftime(TIM_FMT)
        with open(LOGS['del messages'], 'a') as f:
            print(f'Message {message.id}:\n\tAuthor  - {ctx.author.id}'
                  f'\n\tContent - {message.content}\n\tTime    - {time}',
                  file=f)

    @Cog.listener('on_command_error')
    @logger
    async def on_command_error(self, ctx: Context, error: CommandError):
        raise error

    @Cog.listener('on_error')
    @logger
    async def on_error(self, *args, **kwargs):
        for arg in args + kwargs:
            if isinstance(arg, DiscordException):
                raise arg


def setup(bot: AutoShardedBot):
    bot.add_cog(Events(bot))
