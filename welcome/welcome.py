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
                url='https://media.discordapp.net/attachments/1223541148815982613/1226381920112480346/image.png?ex=6624902a&is=66121b2a&hm=c397086d5027b4028df7482297c5f4d81fbb64c26286bd754735fdfc4eaf7474&=&format=webp&quality=lossless&width=1035&height=655')
            embed.set_footer(text=f'Thanks to you, we now have {guild.member_count} members!',
                             icon_url='https://media.discordapp.net/attachments/1213247217792712764/1226378586945224745/JadeCash.png?ex=66248d10&is=66121810&hm=8cfd6469f23c201439908d8eaea14e8a663521701919ae7627ca6afb33ea42bf&=&format=webp&quality=lossless&width=636&height=655')

            await channel.send(content=member.mention, embed=embed)


async def setup(bot):
    await bot.add_cog(Welcome(bot))
