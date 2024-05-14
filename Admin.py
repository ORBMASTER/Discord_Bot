
from nextcord.ext import commands
from nextcord.ext.commands import has_permissions, MissingPermissions
import nextcord
from nextcord import Interaction

testServerId=1223345494353248317
class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client
    testServerId=1223345494353248317
    @nextcord.slash_command(name="admintesting",description="introduction to slash commands",guild_ids=[testServerId])
    async def admintesting(self,interaction:Interaction):
        await interaction.response.send_message("admin")

        


    @commands.command(pass_context=True)
    @commands.has_permissions(manage_roles=True)
    async def addRole(self, ctx, user: nextcord.Member, *, role: nextcord.Role):
        if role in user.roles:
            await ctx.send("Role already added.")
        else:
            await user.add_roles(role)
            await ctx.send("Role added.")

    @addRole.error
    async def add_role_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have permission to use this command.")

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_roles=True)
    async def removeRole(self, ctx, user: nextcord.Member, *, role: nextcord.Role):
        if role not in user.roles:
            await ctx.send("Role is not assigned to the user.")
        else:
            await user.remove_roles(role)
            await ctx.send("Role removed from the user.")

    @removeRole.error
    async def remove_role_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have permission to use this command.")

def setup(client):
    client.add_cog(Admin(client))
