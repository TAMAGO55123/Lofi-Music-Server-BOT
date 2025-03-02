import discord
from discord.ext import commands
from discord import app_commands
from func.ready import bot_ready_print

class JoinCog(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        bot_ready_print("JoinCog")
    
    
	

async def setup(bot):
    await bot.add_cog(JoinCog(bot))