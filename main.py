from config import prefix
from config import token
import keep_alive
import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import time
import random
import os
intents = discord.Intents(messages=True, guilds=True, members=True)
# Imports the needed libs.

client = commands.Bot(command_prefix=prefix, intents=intents)
client.remove_command("help")

@client.event
async def on_ready():
    print ("Lets get goin")
@client.event
async def on_server_join(server):
    print ("Joining {0}".format(server.name))

####PING COMMAND####
@client.command(pass_context=True)
async def Ping(ctx):
    await ctx.message.delete()
    member = ctx.message.author
    channel = ctx.message.channel
    t1 = time.perf_counter()
    await channel.trigger_typing()
    t2 = time.perf_counter()
    embed=discord.Embed(title="Pinged", description='Ping: {}'.format(round((t2-t1)*1000)), color=0x2874A6)
    await member.send(embed=embed)
    print ("Action completed: Server ping")
#############################

####INFO COMMAND####
@client.command(pass_context=True)
async def Info(ctx, member: discord.Member=None):
    await ctx.message.delete()
    member = ctx.message.author
    channel = ctx.message.channel
    if member is None:
        pass
    else:
        await channel.send("**The user's name is: {}**".format(member.name) + "\n**The user's ID is: {}**".format(member.id) + "\n**The user's current status is: {}**".format(member.status) + "\n**The user's highest role is: {}**".format(member.top_role) + "\n**The user joined at: {}**".format(member.joined_at))
    print ("Action completed: User Info")
#############################

keep_alive.keep_alive()
client.run(token)
