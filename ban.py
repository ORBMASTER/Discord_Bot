
import nextcord as discord
from nextcord.ext import commands

class Ban(commands.Cog):
    def __init__(self, client):
        self.client = client
    
@commands.Cog.listener()
async def on_message(self, message):
        # Check if the message content is "hi" and handle it
    if message.content == "hi":
        await message.delete()
        await message.channel.send("Don't send that again.")
        await message.channel.send("https://tenor.com/view/yamcha-yamcha-death-pose-yamcha-dead-yamcha-on-the-ground-yamcha-sleeping-gif-15816799")

        # Process commands manually if the message doesn't start with the prefix
    await self.client.process_commands(message)


    


def setup(client):
    client.add_cog(Ban(client))
