from discord.ui import Button, button, View, Item
from discord import ButtonStyle, Message, Interaction,\
    Embed
from discord.ext.commands import Context
import traceback, sys
from .errors import *


class BaseView(View):
    def __init__(self, ctx: Context, timeout: float = 180.0, **kwargs):
        super().__init__(timeout=timeout)
        self.ctx = ctx
        self.extras = kwargs
        self.message: Message = None
        self.args_check()

    def args_check(self):
        pass

    async def disable_all(self):
        for item in self.children:
            item.disabled = True
        await self.message.edit(view=self)

    async def on_timeout(self):
        await self.disable_all()

    async def interaction_check(self, interaction: Interaction) -> bool:
        return self.ctx.author == interaction.user

    async def kill(self):
        for item in self.children:
            if isinstance(item, Button):
                item.style = ButtonStyle.red
                item.label = 'Error!'
            else:
                item.placeholder = "Error! Contact Shlol#2501"
            item.disabled = True
        await self.message.edit(view=self)

    async def on_error(self, error: Exception, item: Item, interaction: Interaction):
        await self.kill()
        file = sys.stderr
        lines = f'\nIgnoring exception in view {self.__class__.__name__} for item \'{item.custom_id}\':\n'+ ''.join(traceback.format_exception(error.__class__, error, error.__traceback__))
        print(lines, file=file)
        await interaction.response.send_message(f"**Error!** Contact <@613044385910620190> or <@723396966540640300>\n```nim\n{lines}\n```", ephemeral=True)


class ErrorView(BaseView):
    def args_check(self):
        if not self.extras.get('embed'):
            raise MissingArgument(f'\'embed\' was not specified.')
        if not isinstance(self.extras['embed'], Embed):
            raise TypeError(f"'embed' must be of type 'Embed' and not '{self.extras['embed'].__class__.__name__}'")

    @button(label='View Error', custom_id='errorbtn', style=ButtonStyle.danger)
    async def errorbutton(self, _button: Button, interaction: Interaction):
        await interaction.response.send_message(f'Contact <@613044385910620190> or <@723396966540640300>', ephemeral=True,
                                                embed=self.extras['embed'])
