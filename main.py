import discord
from discord.ext import commands
import os
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def setstatus(ctx, *, new_status: str):
    # Example usage: !setstatus CoastBrawl Finale
    await bot.change_presence(activity=discord.Game(name=new_status))
    await ctx.send(f"Status changed to: {new_status}")

# Starts the web server
keep_alive()

# Connects to Discord
bot.run(os.environ.get('DISCORD_TOKEN'))
