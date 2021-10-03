#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#==============================================================================
# Created on Tue Aug  1 21:00:09 2017
#
# @author: phypoh
#==============================================================================

import os
import discord
from discord.ext import commands


bot = commands.Bot(command_prefix='!',
                   owner_id=102704301956149248)

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def hi(ctx):
    """Say hi to Nephie!"""
    await ctx.send("Hello, I'm Nephilim! My creator likes to call me Nephie.")

@bot.command(name='reload', hidden=True)
@commands.is_owner()
async def _reload(ctx):
    """Reloads the timeCog."""
    try:
        bot.unload_extension("timeCog")
        bot.load_extension("timeCog")
        await ctx.send("timeCog has been reloaded!")
    except Exception as e:
        await ctx.send('ERROR: {} - {}'.format(type(e).__name__, e))


@bot.command(name='load', hidden=True)
@commands.is_owner()
async def _load(ctx):
    """Reloads the timeCog."""
    try:
        bot.load_extension("timeCog")
        await ctx.send("timeCog has been loaded!")
    except Exception as e:
        await ctx.send('ERROR: {} - {}'.format(type(e).__name__, e))

@bot.command(name='unload', hidden=True)
@commands.is_owner()
async def _unload(ctx):
    """Reloads the timeCog."""
    try:
        bot.unload_extension("timeCog")
        await ctx.send("timeCog has been unloaded!")
    except Exception as e:
        await ctx.send('ERROR: {} - {}'.format(type(e).__name__, e))

@bot.event
async def on_command_error(ctx,error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all required arguments')
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send('Command does not exist')


try:
    bot.load_extension("timeCog")
    print("timeCog has loaded!")
except Exception as e:
    print('ERROR: {} - {}'.format(type(e).__name__, e))

bot.run(os.getenv('BOT_TOKEN'))

