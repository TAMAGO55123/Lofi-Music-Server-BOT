import discord
from discord.ext import commands
from discord import app_commands
from func.ready import bot_ready_print
import re

class StatusCog(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        bot_ready_print("StatusCog")
        

    @commands.Cog.listener()
    async def on_message(self, message:discord.Message):
        content = message.content
        content_embeds = message.embeds
        first_embed = content_embeds[0]
        channel = message.channel
        channel_id = channel.id
        member = message.author
        member_id = member.id

        if(channel_id == 1345224236930699324):
            if(member_id == 1034361158901178419):
                a = re.search(r'\[(.*)\]',first_embed.description)
                b = a.group()[1:-1]
                print(b)
                voice = self.bot.get_channel(1345224236930699324)
                print(voice.voice_states)
                



	

async def setup(bot):
    await bot.add_cog(StatusCog(bot))