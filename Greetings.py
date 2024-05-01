
import nextcord as discord
import nextcord

from nextcord.ext import commands
import requests
import json  # Add json import

class Greetings(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        # Set the bot presence using the discord namespace
        await self.client.change_presence(
            status=discord.Status.idle,
            activity=discord.Streaming(
                name='Injustice Gods Among Us',
                url='https://www.twitch.tv/directory/category/injustice-gods-among-us'
            )
        )
        print("The bot is ready")
        print("--------------------")
    
    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hello, I'm a bot!")

    @commands.command()
    async def killwhale(self, ctx):
        await ctx.send("whales shall be killed")

    @commands.command()
    async def bestplayer(self, ctx):
        await ctx.send("ORBMASTER")

    @commands.command()
    async def killflash(self, ctx):
        await ctx.send("https://tenor.com/view/yamcha-yamcha-death-pose-yamcha-dead-yamcha-on-the-ground-yamcha-sleeping-gif-15816799")

    @commands.command()
    async def frog(self, ctx):
        await ctx.send("You have turned into a frog")

    @commands.command()
    async def babywhale(self, ctx):
        await ctx.send("https://tenor.com/view/whale-cute-blow-water-close-eyes-swimming-gif-16556295")

    @commands.command()
    async def amen(self, ctx):
        await ctx.send("https://www.youtube.com/watch?v=LrfCSv0g8iE&list=RDLrfCSv0g8iE&start_radio=1")

    @commands.command()
    async def deadwhale(self, ctx):
        await ctx.send("https://tenor.com/view/ohwhale-sploosh-hazardwhale-whalehazard-burst-gif-13702657")

    @commands.command()
    async def joke(self, ctx):
        jokeurl = "https://joke3.p.rapidapi.com/v1/joke"

        headers = {
            "X-RapidAPI-Key": "your-api-key-here",
            "X-RapidAPI-Host": "joke3.p.rapidapi.com"
        }

        response = requests.get(jokeurl, headers=headers)

        if response.status_code == 200:
            data = response.json()  # Parse JSON response
            await ctx.send(data['content'])
        else:
            await ctx.send("Couldn't fetch a joke at the moment. Please try again later.")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        jokeurl = "https://joke3.p.rapidapi.com/v1/joke"

        headers = {
            "X-RapidAPI-Key": "your-api-key-here",
            "X-RapidAPI-Host": "joke3.p.rapidapi.com"
        }

        response = requests.get(jokeurl, headers=headers)

        if response.status_code == 200:
            data = response.json()  # Parse JSON response
            channel = self.client.get_channel(1223345494353248320)  # Use self.client
            await channel.send(f"Hello {member.name}!")
            await channel.send(data['content'])
        else:
            print("Couldn't fetch a joke at the moment.")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.client.get_channel(1223345494353248320)  # Use self.client
        await channel.send(f"Goodbye {member.name}!")
        print("--------------------")
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction,user):
        channel=reaction.message.channel
        await channel.send(user.name+" added: "+reaction.emoji)

    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction,user):
        channel=reaction.message.channel
        await channel.send(user.name+" removed: "+reaction.emoji)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author==self.client.user:
            return
        if ("happy") in message.content:
            #emoji="👌 "
            emoji = "\U0001F44C"
            
            await message.add_reaction(emoji)

        


def setup(client):
    client.add_cog(Greetings(client))
