import asyncio
import json
import random
from os.path import dirname, exists

import discord
from discord.ext import commands
from urlextract import URLExtract

from core import checks
from core.models import PermissionLevel

DIR = dirname(__file__)
POOP_STICKERS = [
    "https://media.discordapp.net/attachments/1106785083379171372/1157133462331985961/20230928_174023.png?ex=65178003&is=65162e83&hm=dc1d01d630f54b13f7bea3dc29be717a279dd46929041dd34745880963379621&",
    "https://media.discordapp.net/attachments/1106785083379171372/1156858924838965268/Untitled570_20230928144333.png?ex=65168055&is=65152ed5&hm=257aeb2eb1d4596009f0ef092adf2e8573242cfae51116e0685545bfa322b87d&=&width=703&height=655",
    "https://media.discordapp.net/attachments/1106793246748848199/1156482829098692649/20230926_233455.png?ex=65152210&is=6513d090&hm=0a5126e8622729f3baa2b31b69dcfef12c9e4d0808e9c09ab9febb46692489bb&=&width=655&height=655",
    "https://media.discordapp.net/attachments/1106793246748848199/1156482828868014100/20230926_230548.png?ex=65152210&is=6513d090&hm=3d90ac3e06e7c44fbb399bf9d06a7634d88940a51d533e086c44cb21c6775077&=&width=334&height=333",
    "https://media.discordapp.net/attachments/1106785083379171372/1156341810042515486/20230926_013519.png?ex=65149ebb&is=65134d3b&hm=330623a1c4b273c609e548740ca66145e5d0365735b3bfbf76348454492b6e4a&=&width=655&height=655",
    "https://media.discordapp.net/attachments/1106785083379171372/1156341810315149395/20230926_013109.png?ex=65149ebb&is=65134d3b&hm=b30994a003ffd066581127220f869c6d90ad41810e86034e0117df45a4748500&=&width=655&height=655",
    "https://media.discordapp.net/attachments/1106785083379171372/1156341810868793505/20230926_002553.png?ex=65149ebb&is=65134d3b&hm=71997888a7a9399fc9443d2b454c55aaa409d95b8bfeb9c83f90017265284d64&=&width=655&height=655",
    "https://cdn.discordapp.com/attachments/1117346551644295239/1158876241093464264/ruan_mei_nerd.png?ex=651dd71a&is=651c859a&hm=06c83048f9ec6c405cd1c5ebf169214cf4db9b9e655d6711854ee1003febd15d&",
    "https://cdn.discordapp.com/attachments/1117346551644295239/1158876240736956526/ruanmeifingerheart.png?ex=651dd71a&is=651c859a&hm=0a506f0784a73f21d142dfa4dcf747854a1b00fdaa378d2db70a6359fb074b15&",
    "https://cdn.discordapp.com/attachments/1117346551644295239/1158876415614255194/ruanmei_bugcat_nod.gif?ex=651dd744&is=651c85c4&hm=c7e78157961d9421ec7d9445b6c23d3c16832b732673e5b51fded27929691949&",
    "https://cdn.discordapp.com/attachments/1117346551644295239/1158876605804986389/ruanmeijoy1.png?ex=651dd771&is=651c85f1&hm=d2b89fc3e7b7b5a426a67b6c54e30d357db69e1e0ee98fe47359e79e3935c33a&",
    "https://cdn.discordapp.com/attachments/1117346551644295239/1158876917269803088/20230926_230006.png?ex=651dd7bb&is=651c863b&hm=8768cd09a5fd98b9105293645c12a6f1e121e0ae9e9e0223108537ee8bda8806&",
    "https://cdn.discordapp.com/attachments/1117346551644295239/1158876917609537556/ruan_mei_eyebrow_raise.png?ex=651dd7bc&is=651c863c&hm=29ad9b9f9bd18ca6cba98f5b79ed564ef489f9beefe8764d94b2b3206188e23b&",
    "https://cdn.discordapp.com/attachments/1117346551644295239/1158876917836042290/20230926_012018.gif?ex=651dd7bc&is=651c863c&hm=9bbace8884217e3c582c89d5e5f61496baced80d0c462790f82bbb64c65d2d95&",
    "https://cdn.discordapp.com/attachments/1117346551644295239/1158877082860912661/ruanmeidead.png?ex=651dd7e3&is=651c8663&hm=3690617f2abd9143677c348a9c947d1cc6f0d4b1393296fac131c4df86e5e14d&",
    "https://cdn.discordapp.com/attachments/1117346551644295239/1158877083657846824/ruanpackwatch.png?ex=651dd7e3&is=651c8663&hm=876634884d7a439207bafbc26916a03f6b1c1b68d029a94b57168463ddda3208&",
    "https://cdn.discordapp.com/emojis/1153489300051202198.png",
    "https://cdn.discordapp.com/emojis/1155737942506078278.png",
    "https://cdn.discordapp.com/emojis/1155740644040519690.png",
    "https://media.discordapp.net/attachments/1178573924548743198/1178573924896882688/ruan_mei_skill_issue_1.png?ex=660a4b80&is=65f7d680&hm=9e579ca330a3b0719e3fd96d1fa76b47b8bd86d4a845584f1765c1b75b4cd51d&=&format=webp&quality=lossless&width=655&height=655",
    "https://media.discordapp.net/attachments/1178573924548743198/1178574207249035295/IMG_9858.jpg?ex=660a4bc3&is=65f7d6c3&hm=fcd0092bceb6ad37d13f653c071f208f82c9bd24e2cbd5794538a2810c3ee0ee&=&format=webp&width=625&height=625",
    "https://media.discordapp.net/attachments/1178573924548743198/1178574207542644796/cries.png?ex=660a4bc3&is=65f7d6c3&hm=7c9e3089d3ca4816b0c980b85a6ce1a6241ff492a2392a4500f21b938331a350&=&format=webp&quality=lossless&width=655&height=655",
    "https://media.discordapp.net/attachments/887963616182145044/1220612598693892147/Ruan_Mei_Eating.png?ex=660f9311&is=65fd1e11&hm=54191eac7ecd4ebec7a3b840c8af78771b8ab3f8879b5e5fd447b3a36edf8a17&=&format=webp&quality=lossless&width=354&height=354",
    "https://media.discordapp.net/attachments/887963616182145044/1220612598966259732/Ruan_Mei_Curious.png?ex=660f9311&is=65fd1e11&hm=babd7156b248876d37cfaaadc99acf35139df7d24c53fa63311a497e4802652a&=&format=webp&quality=lossless&width=349&height=349",
    "https://media.discordapp.net/attachments/887963616182145044/1220612599348203603/Ruan_Mei_Unamused.png?ex=660f9311&is=65fd1e11&hm=d5fe2e173b902a85a0ed98815110581419b594145c50095fee8d9265f0e8e3ab&=&format=webp&quality=lossless&width=349&height=349",
    "https://media.discordapp.net/attachments/887963616182145044/1220612598693892147/Ruan_Mei_Eating.png?ex=660f9311&is=65fd1e11&hm=54191eac7ecd4ebec7a3b840c8af78771b8ab3f8879b5e5fd447b3a36edf8a17&=&format=webp&quality=lossless&width=354&height=354",
    "https://media.discordapp.net/attachments/887963616182145044/1220612436609208370/Ruan_Mei_Sigh.png?ex=660f92ea&is=65fd1dea&hm=bc6a0c75c5db11b01217d87201b251d9c3d057b640a33fd0e9d6ee28b0c3a597&=&format=webp&quality=lossless&width=367&height=367",
    "https://media.discordapp.net/attachments/887963616182145044/1220612435069763614/Ruan_Mei_Love.png?ex=660f92ea&is=65fd1dea&hm=e56c7aca85a65d055431c51583c3a6e8b0bd63fcf60612815f1ecb9132443399&=&format=webp&quality=lossless&width=655&height=655",
    "https://media.discordapp.net/attachments/887963616182145044/1220612435485134888/Ruan_Mei_Think.png?ex=660f92ea&is=65fd1dea&hm=8f754899dcc4a28fc281ed59c68bde5b28eede2535adf5cb8c7db212e1def520&=&format=webp&quality=lossless&width=655&height=655",
    "https://media.discordapp.net/attachments/887963616182145044/1220612436139311124/Ruan_Mei_Yawn.png?ex=660f92ea&is=65fd1dea&hm=e7f143eff843e15bfb3953fae21b0923b1674e0cbf77f299f470b858adb61faa&=&format=webp&quality=lossless&width=655&height=655"
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
            title=f"Ruan Mei has calculated the probability...",
            colour=discord.Colour.random()
        )
        embed.add_field(name='Event', value=text)
        embed.add_field(name="Probability", value=f"This event is **{num}%** likely.", inline=False)
        embed.set_thumbnail(url=random.choice(POOP_STICKERS))

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
            emote = discord.utils.get(ctx.guild.emojis, id=1209013690922303528)
            answer = random.choice(ans[2]["negative"])
        elif num < 6:
            thumbnail = "https://media.discordapp.net/attachments/887963616182145044/1220476220123123764/Robin_Sip.png?ex=660f140e&is=65fc9f0e&hm=3975149e69d87585ca86672641f6a19e28d60d1d9b20721ba6c04c112cbcc20d&=&format=webp&quality=lossless&width=655&height=655"
            emote = discord.utils.get(ctx.guild.emojis, id=1185286958713409677)
            answer = random.choice(ans[1]["neutral"])
        elif num < 10:
            thumbnail = "https://media.discordapp.net/attachments/887963616182145044/1220476218562969682/Robin_Heart.png?ex=660f140d&is=65fc9f0d&hm=dff58447ff06e7feec447b2718ba33eab3f45ae173299bf54ec6e0e93376b79f&=&format=webp&quality=lossless&width=480&height=480"
            emote = discord.utils.get(ctx.guild.emojis, id=1160566321306673233)
            answer = random.choice(ans[0]["positive"])
        else:  # Easter egg
            thumbnail = "https://s3.blankdvth.com/74b72448-f31f-4d85-a765-fa04bca84edd.jpg"
            emote = "🐛"
            answer = f"You've won, you've done the impossible. Contact the bot devs to see them become confused. (`{num}`)"

        embed = discord.Embed(
            title=f"Ruan Mei is vibe checking...",
            description=f"{emote} {member.display_name} {answer}",
            colour=discord.Colour.random()
        )
        embed.set_thumbnail(url=thumbnail)
        
        await ctx.send(embed=embed)
    
async def setup(bot):
    await bot.add_cog(HahaFunny(bot))
