import nextcord
from nextcord.ext import commands
from nextcord import Interaction
import nextcord as discord



    

class Subscriptions(nextcord.ui.View):

    def __init__(self):

        super().__init__(timeout=None)
        self.value = None
    
    

    @nextcord.ui.button(label="Subscribe", style=nextcord.ButtonStyle.red)
    async def subscribe(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Thank you for subscribing", ephemeral=False)
        self.value = True
        self.stop()

    @nextcord.ui.button(label="you should subscribe", style=nextcord.ButtonStyle.gray)
    async def shouldsubscribe(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Thank you for subscribing again", ephemeral=True)
        self.value = False
        self.stop()

class Dropdown(nextcord.ui.Select):
    def __init__(self):
        select_options=[
            nextcord.SelectOption(label="subscribe",description="subscribe to the chjannel"),
            nextcord.SelectOption(label="Dosubscribe",description="do subscribe to the chjannel"),
            nextcord.SelectOption(label="Mustsubscribe",description="must subscribe to the chjannel")
       
       
       
        ]
        super().__init__(placeholder="subscribe options",min_values=1,max_values=1,options=select_options)
    async def callback(self,interaction:Interaction):
        if self.values[0]=="subscribe":
            return await interaction.response.send_message("Thank you for subscribing")
        elif self.values[0]=="Dosubscribe":
            return await interaction.response.send_message("Thank you for do subscribing")
        if self.values[0]=="Mustsubscribe":
            return await interaction.response.send_message("Thank you for must subscribing")
            

class DropdownView(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(Dropdown())
class UI(commands.Cog):
    def __init__(self, client):
        self.client = client
    testServerId=1223345494353248317
    
        


    @nextcord.slash_command(name="testu",description="UI message",guild_ids=[testServerId])
    async def testu(self,interaction:Interaction):
        #todos comandos en minusculas
        await interaction.response.send_message("UI?")
        #testServerId = [1223345494353248317]  # Wrap the guild ID in a list
    
    
    @nextcord.slash_command(name="dropdown",description="dropdown test message",guild_ids=[testServerId])
    async def drop(self,interaction:Interaction):
        #todos comandos en minusculas
        view=DropdownView()
        await interaction.response.send_message("Do you want to subscribe?",view=view)
        #testServerId = [1223345494353248317]  # Wrap the guild ID in a list
    

    @commands.command()
    async def UI2(self, ctx):

        await ctx.send("Hello, I'm a UI")

    
    @nextcord.slash_command(name="button", description="button test", guild_ids=[testServerId])
    async def sub(self, interaction: Interaction):
        view = Subscriptions()
        await interaction.response.send_message("You have 2 options", view=view)
        await view.wait()

        if view.value is None:

            return
        
        elif view.value:

            print("yay you subscribed")

        else:

            print("yay you still subscribed")


def setup(client):
    client.add_cog(UI(client))
