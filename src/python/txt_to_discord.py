import luadata
import os
import json
from time import sleep
import discord
from discord.ext import commands
from datetime import datetime
import shutil


# load discord information
# Config file
repo_name = "WoWGuildChatToDiscordChannel"
cur_path = os.path.dirname(__file__)
repo_path = os.path.join((repo_name).join(cur_path.split(repo_name)[:-1]), repo_name)
config_path = os.path.join(repo_path, "src", "config")

temp_folder = os.path.join(repo_path, "temp")
last_timestamp_path = os.path.join(temp_folder, "last_timestamp.txt")

discord_channel = 1026212397045788682 # "#🟩guild_chat"
# discord_channel = 1026212884402946088 # "#🟧raid_chat"

with open(os.path.join(config_path,"config.json")) as f:
    config = json.load(f)

# Bot Config
bot = commands.Bot(command_prefix=">", description="This is a guild-chat bot", intents=discord.Intents.default())

# Format texts
# Set discord format for messages
text_format = """```diff
+ [{time}][{author}]: {message}
```"""

# Events
@bot.event
async def on_ready():
    channel = bot.get_channel(discord_channel) # desarrollo

    while True:
        # Creates a copy of original file into tmp path every minute
        sleep(60)
        elephant_file_original = config["elephant_addon"]["saved_variables_path"]
        elephant_file_copy = os.path.join(temp_folder, "elephant_lua_copy.lua")
        shutil.copy(elephant_file_original, elephant_file_copy)
            
        # reads txt
        data = luadata.read(elephant_file_copy, encoding="utf-8")
        with open(last_timestamp_path, "r") as f:
            last_timestamp = int(f.read())

        # Identify new messages
        for char_dict_key in data["char"]:
            char_dict = data["char"][char_dict_key]
            for log_key in char_dict["logs"]:
                log_dict = char_dict["logs"][log_key]
                if log_dict["name"] == "Hermandad":
                    guild_log = log_dict["logs"]
                    break
        
        print("in loop")
        for msg in guild_log:
            if len(msg.keys()) < 4 or ("type" in msg and msg["type"] != "GUILD"): 
                continue
            msg_character_name = msg["arg2"]
            msg_time = datetime.utcfromtimestamp(msg["time"]).strftime('%Y-%m-%d %H:%M:%S')
            msg_text = msg["arg1"]
            
            if last_timestamp >= msg["time"]:
                continue
            else:
                last_timestamp = msg["time"]
                with open(last_timestamp_path, "w") as f:
                    f.write(str(last_timestamp))


            print(
                text_format.format(
                    time=msg_time
                    , author=msg_character_name
                    , message=msg_text
                    )
                )
            
            await channel.send(
                text_format.format(
                    time=msg_time
                    , author=msg_character_name
                    , message=msg_text)
            )
            sleep(10)

        # Send each message into discord
        # await channel.send(text_format.format(author="Aletss", message="Hello!!"))


# Run
bot.run(config["bot"]["token"])

