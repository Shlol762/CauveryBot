import re
from datetime import datetime
from cogs import Cog, command, AutoShardedBot, Context, Embed,\
    MemberConverter, Colour
import json


class Utility(Cog):
    def __init__(self, bot: AutoShardedBot):
        self.bot = bot
        self.name = 'Utility'

    @command(name='Remind', aliases=['rm'],
             usage='!remind|rm `<target(s)>`: `<text>`', help='Remind people in Cauvery about an event.')
    async def remind(self, ctx: Context, *, text: str):
        with open('C:/Users/Shlok/CauveryBot/json/people.json', 'r') as f:
            people: dict = json.load(f)
        if re.search(r'(<@!?[0-9]{18}>)+[ ]*:', text):
            targets = [await MemberConverter().convert(ctx, target) for target in text.split(':')[0].split()]
        elif text.startswith('everyone'):
            targets = [await MemberConverter().convert(ctx, target) for target in people.keys() if target.isdigit()]
        text = ':'.join(text.split(':')[1:])
        embed = Embed(title='Reminder!', description=text, colour=Colour.from_rgb(168, 14, 14),
                      timestamp=datetime.now()).set_footer(
            icon_url=ctx.author.avatar.url
        )
        [await member.send(embed=embed) for member in targets]

    @command(name='Announce', aliases=['an'],
             usage='!announce|an `<target(s)>`: `<text>`', help='Announce to people in Cauvery about something.')
    async def remind(self, ctx: Context, *, text: str):
        with open('C:/Users/Shlok/CauveryBot/json/people.json', 'r') as f:
            people: dict = json.load(f)
        if re.search(r'(<@!?[0-9]{18}>)+[ ]*:', text):
            targets = [await MemberConverter().convert(ctx, target) for target in text.split(':')[0].split()]
        elif text.startswith('everyone'):
            targets = [await MemberConverter().convert(ctx, target) for target in people.keys() if target.isdigit()]
        text = ':'.join(text.split(':')[1:])
        embed = Embed(title='Announcement!', description=text, colour=Colour.from_rgb(168, 14, 14),
                      timestamp=datetime.now()).set_footer(
            icon_url=ctx.author.avatar.url
        )
        [await member.send(embed=embed) for member in targets]


def setup(bot: AutoShardedBot):
    bot.add_cog(Utility(bot))
