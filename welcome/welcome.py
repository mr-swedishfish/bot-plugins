import discord
from discord.ext import commands


CHANNEL_ID = 1191916301250203766


class Welcome(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener("on_member_join")
    async def welcome_on_member_join(self, member: discord.Member):
        guild = member.guild
        channel = self.bot.get_channel(CHANNEL_ID)
        if channel is not None:
            embed = discord.Embed(
                title=f"Welcome to Jade Mains, {member.name}!",
                description=f"Please read <#1191916301250203767> to verify and avoid any trouble, and <#1191916301250203768> to grab your roles.\n\n We wish you a pleasant stay; if you need help, DM <@1219772651216703498> to start a Modmail ticket!",
                colour=discord.Colour.from_rgb(237, 159, 236)
            )

            embed.set_thumbnail(url=member.display_avatar)
            embed.set_image(
                url='https://media.discordapp.net/attachments/1213247217792712764/1226382356248531005/Untitled315_20240327175233.png?ex=66249092&is=66121b92&hm=aff0032e92228b4996d4c558b916527905b67833901a02502a87ed9a600b1fa0&=&format=webp&quality=lossless&width=1440&height=654')
            embed.set_footer(text=f'Thanks to you, we now have {guild.member_count} members!',
                             icon_url='https://media.discordapp.net/attachments/1213247217792712764/1226378586945224745/JadeCash.png?ex=66248d10&is=66121810&hm=8cfd6469f23c201439908d8eaea14e8a663521701919ae7627ca6afb33ea42bf&=&format=webp&quality=lossless&width=636&height=655')

            await channel.send(content=member.mention, embed=embed)


async def setup(bot):
    await bot.add_cog(Welcome(bot))
