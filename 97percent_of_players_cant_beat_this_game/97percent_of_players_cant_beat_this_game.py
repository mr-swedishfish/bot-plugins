import asyncio
import json
import random
from os.path import dirname, exists

import discord
from discord.ext import commands
from urlextract import URLExtract

from core import checks
from core.models import PermissionLevel

# List of commands here:
# ?magic8ball

DIR = dirname(__file__)
HETERO_ROLE = 1158884021460291594
BI_ROLE = 1158883963817971822
GAY_ROLE = 1158883765070856202
GAY_STICKERS = [
    "https://media.discordapp.net/attachments/1212916845921828895/1221913234802741418/Untitled298_20240301003453.png?ex=66144e61&is=6601d961&hm=ae05631c391dfa4f585837d77c5a123300dc80b1f21b883394551a47713b5b95&=&format=webp&quality=lossless&width=655&height=655",
    "https://media.discordapp.net/attachments/1212916845921828895/1221913234358141018/Untitled305_20240311221125.png?ex=66144e61&is=6601d961&hm=d276836a5b8b0fa8201042dfab47382f6a1156940d357edb595f9f501fe0cda2&=&format=webp&quality=lossless&width=655&height=655",
    "https://media.discordapp.net/attachments/1212916845921828895/1221913235465175160/Untitled298_20240304223727.png?ex=66144e61&is=6601d961&hm=73ea4fac045b95efac09cfc5dd8184727ded510008fc17291268601e7574e728&=&format=webp&quality=lossless&width=655&height=655",
    "https://media.discordapp.net/attachments/1212916845921828895/1221913235842924625/IMG_6547.png?ex=66144e61&is=6601d961&hm=f50f07e987fa5fe49eb8152df948b05003a4bf7c0836ddc37166120acfbd54b5&=&format=webp&quality=lossless&width=655&height=655",
    "https://media.discordapp.net/attachments/1212916845921828895/1221913236182667315/IMG_6548.png?ex=66144e61&is=6601d961&hm=e03750b3d7d42ab71ca0223fbeb8164fdfaf5c2afb8a92769b6b2f4af592f458&=&format=webp&quality=lossless&width=655&height=655",
    "https://media.discordapp.net/attachments/1212916845921828895/1221913740102992012/IMG_5753.png?ex=66144ed9&is=6601d9d9&hm=4ed2be52b96b89ea29c93d692876935240d7479da7b7047a286b11f5d5b196ee&=&format=webp&quality=lossless&width=655&height=655",
    "https://media.discordapp.net/attachments/1212916845921828895/1221914022404948098/Untitled326_20240325130926.png?ex=66144f1d&is=6601da1d&hm=4a664a9b6167bfed877aeaece64e630ed6fdd0c10b816a94270f9f5174ceedbf&=&format=webp&quality=lossless&width=450&height=450",
    "https://media.discordapp.net/attachments/1212916845921828895/1221913739478175754/IMG_5755.png?ex=66144ed9&is=6601d9d9&hm=ab8522b3901089dc54f04c17df52fbf672d2932e6948fe55c8d170ca093195e8&=&format=webp&quality=lossless&width=655&height=655",
    "https://media.discordapp.net/attachments/1212916845921828895/1221913740614832148/IMG_5756.png?ex=66144ed9&is=6601d9d9&hm=af8db425af79a16ebd6f23591dff118ffdef7874af3f2e79f947a2f694bdfed6&=&format=webp&quality=lossless&width=655&height=655"
]

EIGHT_BALL_TITLES = [
    'Jade has thought about this...',
    'Jade has decided...',
    'Jade has consulted the IPC...',
    'Jade has set aside some time to think about this...',
    'Jade has concluded...',
    'Jade has gathered some information...',
    'Jade has inferred...'
]

class HahaFunny(commands.Cog):
    """97% of players can't beat this game!!"""

    def __init__(self, bot):
        self.bot = bot

    # Odds for an outcome
    @checks.has_permissions(PermissionLevel.REGULAR)
    @commands.command(aliases=['odds', 'probability', 'prob'])
    async def outcome(self, ctx: commands.Context, *, text: str):
        """Measure the odds for a specific outcome!"""

        num = random.randrange(10001) / 100

        embed = discord.Embed(
            title=f"Jade has calculated the odds...",
            colour=discord.Colour.random()
        )
        embed.add_field(name='Event', value=text)
        embed.add_field(name="Probability", value=f"This event is **{num}%** likely.", inline=False)
        embed.set_thumbnail(url=random.choice(GAY_STICKERS))

        await ctx.send(embed=embed)

    # Vibe Check
    @checks.has_permissions(PermissionLevel.REGULAR)
    @commands.command(aliases=['vibe', 'check', 'vb', 'vc'])
    async def vibecheck(self, ctx: commands.Context, member: commands.MemberConverter = None):
        """Do you pass the vibe check?"""
        if member is None:
            member = ctx.author

        num = random.randint(0, 9)

        with open(f'{DIR}/vibecheck.json') as f:
            ans = json.load(f)

        if num < 3:
            thumbnail = "https://media.discordapp.net/attachments/1212916845921828895/1221914022404948098/Untitled326_20240325130926.png?ex=66144f1d&is=6601da1d&hm=4a664a9b6167bfed877aeaece64e630ed6fdd0c10b816a94270f9f5174ceedbf&=&format=webp&quality=lossless&width=450&height=450"
            emote = discord.utils.get(ctx.guild.emojis, id=1214461577118490695)
            answer = random.choice(ans[2]["negative"])
        elif num < 6:
            thumbnail = "https://media.discordapp.net/attachments/1212916845921828895/1221913235465175160/Untitled298_20240304223727.png?ex=66144e61&is=6601d961&hm=73ea4fac045b95efac09cfc5dd8184727ded510008fc17291268601e7574e728&=&format=webp&quality=lossless&width=655&height=655"
            emote = discord.utils.get(ctx.guild.emojis, id=1219369970916397106)
            answer = random.choice(ans[1]["neutral"])
        elif num < 10:
            thumbnail = "https://media.discordapp.net/attachments/1212916845921828895/1221913236182667315/IMG_6548.png?ex=66144e61&is=6601d961&hm=e03750b3d7d42ab71ca0223fbeb8164fdfaf5c2afb8a92769b6b2f4af592f458&=&format=webp&quality=lossless&width=655&height=655"
            emote = discord.utils.get(ctx.guild.emojis, id=1214461477906550854)
            answer = random.choice(ans[0]["positive"])
        else:  # Easter egg
            thumbnail = "https://s3.blankdvth.com/74b72448-f31f-4d85-a765-fa04bca84edd.jpg"
            emote = "🐛"
            answer = f"You've won, you've done the impossible. Contact the bot devs to see them become confused. (`{num}`)"

        embed = discord.Embed(
            title=f"Jade is vibe checking...",
            description=f"{emote} {member.display_name} {answer}",
            colour=discord.Colour.random()
        )
        embed.set_thumbnail(url=thumbnail)
        
        await ctx.send(embed=embed)
    
    # Gaydar
    @checks.has_permissions(PermissionLevel.REGULAR)
    @commands.command(aliases=['gae', 'gayrate', 'gaydar'])
    async def gay(self, ctx: commands.Context, member: commands.MemberConverter = None):
        """Why are you gae?"""
        if member is None:
            member = ctx.author

        num = random.randrange(10001) / 100

        embed = discord.Embed(
            title=f"The IPC has decided that...",
            description=f"{member.display_name} is **{num}%** gay.",
            colour=discord.Colour.random()
        )
        embed.set_thumbnail(url=random.choice(GAY_STICKERS))

        # funi footer if anyone gets either
        if num == 0:
            embed.set_footer(text=f'[{member.display_name} is now a Certified Hetero.]')
            role = discord.utils.get(ctx.guild.roles, id=HETERO_ROLE)
            await member.add_roles(role)
        elif num == 50:
            embed.set_footer(text=f'[{member.display_name} is now a Certified Bi.]')
            role = discord.utils.get(ctx.guild.roles, id=BI_ROLE)
            await member.add_roles(role)
        elif num == 100:
            embed.set_footer(text=f'[{member.display_name} is now a Certified Gay. BE WHO YOU ARE FOR YOUR PRIDE!!]')
            role = discord.utils.get(ctx.guild.roles, id=GAY_ROLE)
            await member.add_roles(role)
            
        await ctx.send(embed=embed)

    # Magic 8 Ball
    @checks.has_permissions(PermissionLevel.REGULAR)
    @commands.command(aliases=['8ball', 'ball'])
    async def magic8ball(self, ctx: commands.Context, *, text: str):
        """Ask Jade a "Yes or No" question~"""

        num = random.randint(0, 9)

        with open(f'{DIR}/8ball.json') as f:
            ans = json.load(f)

        if num < 3:
            thumbnail = "https://media.discordapp.net/attachments/1212916845921828895/1221913739478175754/IMG_5755.png?ex=66144ed9&is=6601d9d9&hm=ab8522b3901089dc54f04c17df52fbf672d2932e6948fe55c8d170ca093195e8&=&format=webp&quality=lossless&width=655&height=655"
            emote = discord.utils.get(ctx.guild.emojis, id=1216443083605020732)
            answer = random.choice(ans[2]["negative"])
        elif num < 6:
            thumbnail = "https://media.discordapp.net/attachments/1212916845921828895/1221913235465175160/Untitled298_20240304223727.png?ex=66144e61&is=6601d961&hm=73ea4fac045b95efac09cfc5dd8184727ded510008fc17291268601e7574e728&=&format=webp&quality=lossless&width=655&height=655"
            emote = discord.utils.get(ctx.guild.emojis, id=1214461527784951838)
            answer = random.choice(ans[1]["neutral"])
        elif num < 10:
            thumbnail = "https://media.discordapp.net/attachments/1212916845921828895/1221913740102992012/IMG_5753.png?ex=66144ed9&is=6601d9d9&hm=4ed2be52b96b89ea29c93d692876935240d7479da7b7047a286b11f5d5b196ee&=&format=webp&quality=lossless&width=655&height=655"
            emote = discord.utils.get(ctx.guild.emojis, id=1216133118067609660)
            answer = random.choice(ans[0]["positive"])
        else:  # Easter egg
            thumbnail = "https://s3.blankdvth.com/74b72448-f31f-4d85-a765-fa04bca84edd.jpg"
            emote = "🐛"
            answer = f"You've won, you've done the impossible. Contact the bot devs to see them become confused. (`{num}`)"

        embed = discord.Embed(
            title=random.choice(EIGHT_BALL_TITLES),
            colour=discord.Colour.random()
        )

        embed.add_field(name='Question', value=text)
        embed.set_thumbnail(url=thumbnail)
        embed.add_field(name="Answer", value=f"{emote} {answer}", inline=False)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(HahaFunny(bot))
