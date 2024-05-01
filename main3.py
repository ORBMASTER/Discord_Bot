import nextcord
from nextcord import Interaction
from nextcord.ext import commands
from apikeys import *
import os
# Set up the bot
client = commands.Bot(command_prefix='!', intents=nextcord.Intents.all())
cogs_folder = './cogs'
# Load the greetings cog
for filename in os.listdir(cogs_folder):
    if filename.endswith('.py') and filename != '__init__.py':
        # Construct the cog path in the form of "cogs.<filename without extension>"
        cog_path = f'cogs.{filename[:-3]}'
        # Load the cog
        client.load_extension(cog_path)

# Add other initialization code as needed

# Run the bot with your token
testServerId=1223345494353248317
@client.slash_command(name="test",description="introduction to slash commands",guild_ids=[testServerId])
async def test(interaction:Interaction):
    await interaction.response.send_message("hello surbscribe bitch")

client.run(DISCORD_BOT_TOKEN)
