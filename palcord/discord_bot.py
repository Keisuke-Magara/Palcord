import discord
from discord.ext import commands

class DiscordNotifier(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        
    @commands.command()
    async def test(self, ctx):
        pass
    
    @commands.command()
    async def register(self, ctx):
        print(f"Request register ID={ctx}")
    
    @commands.command()
    async def ip(self, ctx):
        print(f"Request to show IP Addr")


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('my token goes here')
