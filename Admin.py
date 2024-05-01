
from nextcord.ext import commands
from nextcord.ext.commands import has_permissions, MissingPermissions
import nextcord

class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

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
