import os
import discord
from discord.ext import commands

# Pull token safely from environment variables
TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

if __name__ == "__main__":
    bot.run(MTU2MTAxNjIwOTk0NjgzNzE3Ng.GQX0Ha.cDFak4Byhacun_Mmyy7BvsmO4rRM07fudLI6NM)
