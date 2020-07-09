import discord

from discord.ext import commands
from utils.config import Config
from utils.mysql import *
config = Config()

class dev_only(commands.CommandError):
    pass

class owner_only(commands.CommandError):
    pass

class not_nsfw_channel(commands.CommandError):
    pass

class not_guild_owner(commands.CommandError):
    pass

class no_permission(commands.CommandError):
    pass

class terminal_dead(commands.CheckFailure):
    pass

#the terminal bridge, to work with squeed's terminal bot
def is_terminal_existent():
    def predicate(ctx):
        if ctx.guild.get_member(521023036812558356) is not None:
            return True
        else:
            raise terminal_dead("terminal isn't in this discord guild! This command will refuse to work unless terminal is added.")
    return commands.check(predicate)

def is_owner():
    def predicate(ctx):
        if ctx.author.id == int(config.owner_id):
            return True
        else:
            raise owner_only
    return commands.check(predicate)

def is_dev():
    terminaldevs = [365274392680333329, 372078453236957185, 147765181903011840]
    def predicate(ctx):
        if ctx.author.id in config.dev_ids or ctx.author.id == int(config.owner_id) or ctx.author.id in terminaldevs:
            return True
        else:
            raise dev_only
    return commands.check(predicate)

def is_nsfw_channel():
    def predicate(ctx):
        if ctx.channel.is_nsfw():
            return True
        else:
            raise not_nsfw_channel
    return commands.check(predicate)

def is_guild_owner():
    def predicate(ctx):
        if ctx.author.id == ctx.guild.owner_id:
            return True
        else:
            raise not_guild_owner
    return commands.check(predicate)

def server_mod_or_perms(**permissions):
    def predicate(ctx):
        mod_role_name = read_data_entry(ctx.guild.id, "mod-role")
        mod = discord.utils.get(ctx.author.roles, name=mod_role_name)
        if mod or permissions and all(getattr(ctx.channel.permissions_for(ctx.author), name, None) == value for name, value in permissions.items()):
            return True
        else:
            raise no_permission
    return commands.check(predicate)

def server_admin_or_perms(**permissions):
    def predicate(ctx):
        admin_role_name = read_data_entry(ctx.guild.id, "admin-role")
        admin = discord.utils.get(ctx.author.roles, name=admin_role_name)
        if admin or permissions and all(getattr(ctx.channel.permissions_for(ctx.author), name, None) == value for name, value in permissions.items()):
            return True
        else:
            raise no_permission
    return commands.check(predicate)

def has_permissions(**permissions):
    def predicate(ctx):
        if all(getattr(ctx.channel.permissions_for(ctx.author), name, None) == value for name, value in permissions.items()):
            return True
        else:
            raise no_permission
    return commands.check(predicate)

