import discord
from discord.ext import commands, tasks
from discord import app_commands
from os import getenv, listdir
from dotenv import load_dotenv
import asyncio
import aiohttp
load_dotenv()

now_status = 0

@tasks.loop(seconds=20)
async def status():
    global now_status

    if now_status == 0:
        data1 = discord.Activity(type=discord.ActivityType.playing, name="BGM & 24/7")
        now_status = 1
    elif now_status == 1:
        data1 = discord.Activity(type=discord.ActivityType.listening, name="Music Custom Status")
        now_status =0

    await bot.change_presence(activity=data1)

async def main(bot:commands.Bot):

    @bot.event
    async def on_ready():
        print(f'\033[32m| {bot.user}としてログインしました。\033[0m')
        status.start()
        try:
            synced = await bot.tree.sync()
            print(f'\033[32m| {len(synced)}個のコマンドを同期しました。\033[0m')
        except Exception as e:
            print(f"\033[30m| コマンドの同期でエラーが発生しました。\n{e}\033[0m")

    # for cog in listdir("cogs"):
    #     if cog.endswith(".py"):
    #         await bot.load_extension(f"cogs.{cog[:-3]}")

    # @bot.event
    # async def on_member_join(member:discord.Member):
    #     embeds=[
    #         discord.Embed(
    #             title="Welcome to Server!",
    #             description=f"""Hello <@{member.id}> !\nWe can listen 24/7 Music in This Server!\nAnd There is Custom Playlist!\nIn <#1345574641736876062> ,\nApply for Your Favourite Songs to Custom Playlist!\n\nPlease Read <#1345223384157392926> ,\nAnd Verify <#1345231502593622066> !""",
    #             colour=0xffff00
    #         ),
    #         discord.Embed(
    #             title="サーバーへようこそ！",
    #             description=f"""ようこそ <@{member.id}> !\nこのサーバーでは24時間365日好きなジャンルのBGMを聴くことができます！\nそしてカスタムプレイリストもあります！\n<#1345574641736876062>で\nあなたが好きな曲を登録してください！\n\n<#1345223384157392926> を読んで、\n<#1345231502593622066> で認証してください！""",
    #             colour=0xffff00
    #         )
    #     ]
    #     embeds[0].set_author(name="EN")
    #     embeds[1].set_author(name="JP")
    #     print(embeds)
    #     await bot.get_channel(1345231520507363370).send(embeds=embeds)

    # Bot Start
    await bot.start(getenv("BOT_TOKEN"))

if __name__ == "__main__":
    intents = discord.Intents.default()
    intents.message_content = True
    intents.guilds = True

    bot = commands.Bot(command_prefix="lm!", intents=intents)
    asyncio.run(main(bot))