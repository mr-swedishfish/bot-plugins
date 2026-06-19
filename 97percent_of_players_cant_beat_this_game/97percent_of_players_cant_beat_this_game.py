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
    "https://images-ext-1.discordapp.net/external/SbYmWpkJ1smzL2QUqP3o0nFb1URbXdk4XGJ71mw1zho/%3Fanimated%3Dtrue/https/cdn.discordapp.com/emojis/1463508619239624800.webp?animated=true&width=22&height=22",
    "https://images-ext-1.discordapp.net/external/1dAQGRY3GJUwG9zAGXESzCW9z7Yam8o1oKWfpZdj5wg/%3Fanimated%3Dtrue/https/cdn.discordapp.com/emojis/991192870507786320.webp?animated=true&width=141&height=85",
    "https://images-ext-1.discordapp.net/external/VcRrPcS-kGWPcLJf8n1g_x9uhl135Cq6Ee63h5MzvjI/%3Fanimated%3Dtrue/https/cdn.discordapp.com/emojis/1463510410035462404.webp?animated=true&width=22&height=22",
    "https://images-ext-1.discordapp.net/external/VxLLTfNchjWD07N_Jhsc93jhgoU6ucv8ao7bE-Vh3OM/%3Fanimated%3Dtrue/https/cdn.discordapp.com/emojis/1493513251856842822.webp?animated=true&width=141&height=141",
    "https://images-ext-1.discordapp.net/external/ikAjXJMJ_5ymXbw41ffhRzyY75pr3V6xcZWRdfdC9b8/https/cdn.discordapp.com/emojis/1450339910429970524.png?format=webp&quality=lossless&width=53&height=50",
    "https://images-ext-1.discordapp.net/external/xPsf3T57VZ6RnWrgJ4KWmR_qzXhZ8AsMKCyVbN_NE1E/%3Fanimated%3Dtrue/https/cdn.discordapp.com/emojis/1450335483933622272.webp?animated=true&width=110&height=110",
    "https://images-ext-1.discordapp.net/external/VCczQql38GA_ZLZmYFxPRv7izDmh173Nt5qpvBsmDgg/%3Fanimated%3Dtrue/https/cdn.discordapp.com/emojis/1463510365299015722.webp?animated=true&width=22&height=22",
    "https://images-ext-1.discordapp.net/external/pLRuYoTwcCXiabAV6XRMnb-Firmu3bCxCyUqxpiJJqg/%3Fanimated%3Dtrue/https/cdn.discordapp.com/emojis/1463509331252088979.webp?animated=true&width=22&height=22",
    "https://images-ext-1.discordapp.net/external/2467LZcm9Y5C_AhNC6YbEJsHQsjVYZnQhaKSdaZvDFo/%3Fanimated%3Dtrue/https/cdn.discordapp.com/emojis/1450340288450138346.webp?animated=true&width=83&height=83",
    "https://images-ext-1.discordapp.net/external/iGoz1YjaE2qRSmeL-_6UBKlJdxS57UDzQRD06wsVNUA/%3Fanimated%3Dtrue/https/cdn.discordapp.com/emojis/1450338249628450917.webp?animated=true&width=134&height=141",
    "https://images-ext-1.discordapp.net/external/Hp7Pimd_erCUUzfec596R3Ej_nTqgRqkzLCKmJBy9Hs/%3Fanimated%3Dtrue/https/cdn.discordapp.com/emojis/1463508135930105939.webp?animated=true&width=22&height=22",
    "https://images-ext-1.discordapp.net/external/14A9e01s_Wyzx246_Xjbw5iMOrZajuGUcIYJl5jhDvo/%3Fanimated%3Dtrue/https/cdn.discordapp.com/emojis/1463508218788581560.webp?animated=true&width=22&height=22"
]

EIGHT_BALL_TITLES = [
    'Meow Meow has thought about this...',
    'Meow Meow has decided...',
    'Meow Meow has consulted the other cats...',
    'Meow Meow has set aside some time to think about this...',
    'Meow Meow has concluded...',
    'Meow Meow has gathered some information...',
    'Meow Meow has inferred...'
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
            thumbnail = "https://images-ext-1.discordapp.net/external/9pnYoBxbUvsR2L3xPYJ1L36BC4cQZPPuHV-dt3xNIts/%3Fanimated%3Dtrue/https/cdn.discordapp.com/emojis/1463508538235293831.webp?animated=true&width=22&height=22"
            emote = discord.utils.get(ctx.guild.emojis, id=1214461577118490695)
            answer = random.choice(ans[2]["negative"])
        elif num < 6:
            thumbnail = "https://images-ext-1.discordapp.net/external/R2yBf1pcrjQ4WovRcbcPE_jMYfu2SYM_IOmzkZbQ1qI/%3Fanimated%3Dtrue/https/cdn.discordapp.com/emojis/1463508302129270829.webp?animated=true&width=22&height=22"
            emote = discord.utils.get(ctx.guild.emojis, id=1219369970916397106)
            answer = random.choice(ans[1]["neutral"])
        elif num < 10:
            thumbnail = "https://images-ext-1.discordapp.net/external/Dt78jksPgFwlXr3kqZzA28Y-y2IuwGCRw20uHwBizu0/%3Fanimated%3Dtrue/https/cdn.discordapp.com/emojis/1463508063993598120.webp?animated=true&width=22&height=22"
            emote = discord.utils.get(ctx.guild.emojis, id=1214461477906550854)
            answer = random.choice(ans[0]["positive"])
        else:  # Easter egg
            thumbnail = "https://s3.blankdvth.com/74b72448-f31f-4d85-a765-fa04bca84edd.jpg"
            emote = "🐛"
            answer = f"You've won, you've done the impossible. Contact the bot devs to see them become confused. (`{num}`)"

        embed = discord.Embed(
            title=f"Meow Meow is vibe checking...",
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
            title=f"The cat council has decided that...",
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
        """Ask Meow Meow a "Yes or No" question~"""

        num = random.randint(0, 9)

        with open(f'{DIR}/8ball.json') as f:
            ans = json.load(f)

        if num < 3:
            thumbnail = "https://images-ext-1.discordapp.net/external/YLnjSR0M2i7KsS0pNzRKzyz6jm19emuRIbIW5yHvqkI/%3Fanimated%3Dtrue/https/cdn.discordapp.com/emojis/1463509038313766944.webp?animated=true&width=22&height=22"
            emote = discord.utils.get(ctx.guild.emojis, id=1216443083605020732)
            answer = random.choice(ans[2]["negative"])
        elif num < 6:
            thumbnail = "https://images-ext-1.discordapp.net/external/R2yBf1pcrjQ4WovRcbcPE_jMYfu2SYM_IOmzkZbQ1qI/%3Fanimated%3Dtrue/https/cdn.discordapp.com/emojis/1463508302129270829.webp?animated=true&width=22&height=22"
            emote = discord.utils.get(ctx.guild.emojis, id=1214461527784951838)
            answer = random.choice(ans[1]["neutral"])
        elif num < 10:
            thumbnail = "https://images-ext-1.discordapp.net/external/XHOgS2VkA9nLjxElXJywZZi7AjfmWT4XH2WzO8ycrvo/%3Fanimated%3Dtrue/https/cdn.discordapp.com/emojis/1463508905945469090.webp?animated=true&width=22&height=22"
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
