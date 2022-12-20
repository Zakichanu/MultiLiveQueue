import discord
from discord import app_commands
from dotenv import load_dotenv
import os
from ranking.RankingCommands import Rank
from matchmaking.QueueCommands import Queue
from user.UserCommands import User

load_dotenv()

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    tree.add_command(Queue())
    tree.add_command(User())
    tree.add_command(Rank())
    await tree.sync()
    print("Bot is ready!")

client.run(os.getenv('TOKEN'))