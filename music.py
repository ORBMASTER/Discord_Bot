from nextcord.ext import commands

class music(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def bye(self, ctx):
        await ctx.send("bye bot!")

def setup(client):
    client.add_cog(music(client))
