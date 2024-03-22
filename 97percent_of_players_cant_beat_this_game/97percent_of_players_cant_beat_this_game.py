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
NONBOZO_ROLE = 1158884021460291594
HALFBOZO_ROLE = 1158883963817971822
BOZO_ROLE = 1158883765070856202
BOZO_STICKERS = [
    "https://media.discordapp.net/attachments/887963616182145044/1220476218101600336/935D7DC6-3CD4-4F14-BAD9-91E2DD8C3CA3.png?ex=660f140d&is=65fc9f0d&hm=120406e1e1bcf5fee87cbaa584f6b77abf911176b5744e8e9f7e0619eeb9d5af&=&format=webp&quality=lossless&width=655&height=655",
    "https://media.discordapp.net/attachments/887963616182145044/1220476218562969682/Robin_Heart.png?ex=660f140d&is=65fc9f0d&hm=dff58447ff06e7feec447b2718ba33eab3f45ae173299bf54ec6e0e93376b79f&=&format=webp&quality=lossless&width=480&height=480",
    "https://media.discordapp.net/attachments/887963616182145044/1220476219355697192/Robin_peek.png?ex=660f140e&is=65fc9f0e&hm=891362027443010a448a39459ec9264534afa661debdcc666f2113ab4d8dc05a&=&format=webp&quality=lossless&width=655&height=655",
    "https://media.discordapp.net/attachments/887963616182145044/1220476220123123764/Robin_Sip.png?ex=660f140e&is=65fc9f0e&hm=3975149e69d87585ca86672641f6a19e28d60d1d9b20721ba6c04c112cbcc20d&=&format=webp&quality=lossless&width=655&height=655",
    "https://media.discordapp.net/attachments/887963616182145044/1220476220500738158/robin_pout_sparkles.png?ex=660f140e&is=65fc9f0e&hm=40f051fe3f652555466e90e5132543ffdbff7b78ae7abd0f8f8f9fca9813e298&=&format=webp&quality=lossless&width=655&height=655",
    "https://media.discordapp.net/attachments/887963616182145044/1220476243762479124/robin_faint.png?ex=660f1413&is=65fc9f13&hm=5fd9f527a306361e3396ceb68c9a7a5a2cb7aa36f67daea605f45177edde5438&=&format=webp&quality=lossless&width=655&height=655",
    "https://media.discordapp.net/attachments/887963616182145044/1220476217464062052/C32D8906-9290-4CE9-B1F9-AB1A8049B569.png?ex=660f140d&is=65fc9f0d&hm=5bff1c836008805adffbab1018d1caf71638d137daf206970a83fdcf281aee96&=&format=webp&quality=lossless&width=655&height=655",
    "https://media.discordapp.net/attachments/1184968900660703333/1217097457909895258/robin_wave.png?ex=660c03d6&is=65f98ed6&hm=1bf77296262159a42acbf357eed6cb860ef110586e015bc4897a554bf5875ca7&=&format=webp&quality=lossless&width=655&height=655"
]

EIGHT_BALL_TITLES = [
    'Robin has thought about this...',
    'Robin has decided...',
    'Robin has consulted Xipe...',
    'Robin has set aside some time to think about this...',
    'Robin has concluded...',
    'Robin has gathered some information...',
    'Robin has inferred...'
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
            title=f"Robin has measured the odds...",
            colour=discord.Colour.random()
        )
        embed.add_field(name='Event', value=text)
        embed.add_field(name="Probability", value=f"This event is **{num}%** likely.", inline=False)
        embed.set_thumbnail(url=random.choice(BOZO_STICKERS))

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
            thumbnail = "https://media.discordapp.net/attachments/887963616182145044/1220476243762479124/robin_faint.png?ex=660f1413&is=65fc9f13&hm=5fd9f527a306361e3396ceb68c9a7a5a2cb7aa36f67daea605f45177edde5438&=&format=webp&quality=lossless&width=655&height=655"
            emote = discord.utils.get(ctx.guild.emojis, id=1211059820698796052)
            answer = random.choice(ans[2]["negative"])
        elif num < 6:
            thumbnail = "https://media.discordapp.net/attachments/887963616182145044/1220476220123123764/Robin_Sip.png?ex=660f140e&is=65fc9f0e&hm=3975149e69d87585ca86672641f6a19e28d60d1d9b20721ba6c04c112cbcc20d&=&format=webp&quality=lossless&width=655&height=655"
            emote = discord.utils.get(ctx.guild.emojis, id=1201386255049564200)
            answer = random.choice(ans[1]["neutral"])
        elif num < 10:
            thumbnail = "https://media.discordapp.net/attachments/887963616182145044/1220476218562969682/Robin_Heart.png?ex=660f140d&is=65fc9f0d&hm=dff58447ff06e7feec447b2718ba33eab3f45ae173299bf54ec6e0e93376b79f&=&format=webp&quality=lossless&width=480&height=480"
            emote = discord.utils.get(ctx.guild.emojis, id=1211077629499805788)
            answer = random.choice(ans[0]["positive"])
        else:  # Easter egg
            thumbnail = "https://s3.blankdvth.com/74b72448-f31f-4d85-a765-fa04bca84edd.jpg"
            emote = "🐛"
            answer = f"You've won, you've done the impossible. Contact the bot devs to see them become confused. (`{num}`)"

        embed = discord.Embed(
            title=f"Robin is vibe checking...",
            description=f"value={emote} {member.display_name} {answer}",
            colour=discord.Colour.random()
        )
        
        await ctx.send(embed=embed)
    
    # Bozo Meter
    @checks.has_permissions(PermissionLevel.REGULAR)
    @commands.command(aliases=['bozometer', 'bozorate'])
    async def bozo(self, ctx: commands.Context, member: commands.MemberConverter = None):
        """Are you a bozo?"""
        if member is None:
            member = ctx.author

        num = random.randrange(10001) / 100

        embed = discord.Embed(
            title=f"The Family has decided that...",
            description=f"{member.display_name} is **{num}%** bozo.",
            colour=discord.Colour.random()
        )
        embed.set_thumbnail(url=random.choice(BOZO_STICKERS))

        # funi footer if anyone gets either
        if num == 0:
            embed.set_footer(text=f'[{member.display_name} is now a Certified Non-Bozo]')
            role = discord.utils.get(ctx.guild.roles, id=NONBOZO_ROLE)
            await member.add_roles(role)
        elif num == 50:
            embed.set_footer(text=f'[{member.display_name} is now a Certified Half Bozo]')
            role = discord.utils.get(ctx.guild.roles, id=HALFBOZO_ROLE)
            await member.add_roles(role)
        elif num == 100:
            embed.set_footer(text=f'[{member.display_name} is now a Certified Bozo. LAUGH AT THIS USER!!]')
            role = discord.utils.get(ctx.guild.roles, id=BOZO_ROLE)
            await member.add_roles(role)
            
        await ctx.send(embed=embed)

    # Magic 8 Ball
    @checks.has_permissions(PermissionLevel.REGULAR)
    @commands.command(aliases=['8ball', 'ball'])
    async def magic8ball(self, ctx: commands.Context, *, text: str):
        """Ask Robin a "Yes or No" question~"""

        num = random.randint(0, 9)

        with open(f'{DIR}/8ball.json') as f:
            ans = json.load(f)

        if num < 3:
            thumbnail = "https://media.discordapp.net/attachments/887963616182145044/1220476243762479124/robin_faint.png?ex=660f1413&is=65fc9f13&hm=5fd9f527a306361e3396ceb68c9a7a5a2cb7aa36f67daea605f45177edde5438&=&format=webp&quality=lossless&width=655&height=655"
            emote = discord.utils.get(ctx.guild.emojis, id=1211059820698796052)
            answer = random.choice(ans[2]["negative"])
        elif num < 6:
            thumbnail = "https://media.discordapp.net/attachments/887963616182145044/1220476219355697192/Robin_peek.png?ex=660f140e&is=65fc9f0e&hm=891362027443010a448a39459ec9264534afa661debdcc666f2113ab4d8dc05a&=&format=webp&quality=lossless&width=655&height=655"
            emote = discord.utils.get(ctx.guild.emojis, id=1193067844066344991)
            answer = random.choice(ans[1]["neutral"])
        elif num < 10:
            thumbnail = "https://media.discordapp.net/attachments/887963616182145044/1220476218101600336/935D7DC6-3CD4-4F14-BAD9-91E2DD8C3CA3.png?ex=660f140d&is=65fc9f0d&hm=120406e1e1bcf5fee87cbaa584f6b77abf911176b5744e8e9f7e0619eeb9d5af&=&format=webp&quality=lossless&width=655&height=655"
            emote = discord.utils.get(ctx.guild.emojis, id=1200472301611778172)
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
