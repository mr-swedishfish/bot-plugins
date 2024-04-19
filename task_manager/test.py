import discord
import os
import dotenv
from dotenv import load_dotenv

dotenv.load_dotenv()
token = str(os.getenv("TOKEN"))

load_dotenv()
bot = discord.Bot()

@bot.slash_command()
async def modal_slash(ctx: discord.ApplicationContext):
    """Shows an example of a modal dialog being invoked from a slash command."""
    modal = MyModal(title="Modal via Slash Command")
    await ctx.send_modal(modal)