from email import message
import os
import json
from time import sleep
import discord
from discord.ext import commands

# load discord information
# Config file
repo_name = "WoWGuildChatToDiscordChannel"
cur_path = os.path.dirname(__file__)
repo_path = os.path.join((repo_name).join(cur_path.split(repo_name)[:-1]), repo_name)
config_path = os.path.join(repo_path, "src", "config")

with open(os.path.join(config_path,"config.json")) as f:
    config = json.load(f)

# Bot Config
bot = commands.Bot(command_prefix=">", description="This is a guild-chat bot", intents=discord.Intents.default())

# Format texts
# Set discord format for messages
text_format = """```diff
+ [{author}]: {message}
```"""

# Events
@bot.event
async def on_ready():
    print("before channel")
    channel = bot.get_channel(824027419965915157) # desarrollo
    print("after channel")
    print("before loop")

    while True:
        # reads txt
        # Identify new messages
        print("in loop")
        sleep(10)
        # Send each message into discord
        await channel.send(text_format.format(author="Aletss", message="Hello!!"))


# Run
bot.run(config["bot"]["token"])

