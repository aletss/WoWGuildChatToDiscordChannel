This project pretends to send guild chat from world of warcraft into a discord channel.

# How to use
1. Use addon [Elephant](https://www.wowace.com/projects/elephant)
2. Configure discord channel (you need admin acces to your server)
2. Update `./src/config/config`
3. Run python script

# How it works
It's separated into 2 sections
1. Lua code (we use [Elephant](https://www.wowace.com/projects/elephant) addon for this)  
Writes a txt to update guild messages while logged into the game
2. Python script  
Script that runs permanently sending new messages into discord channel assigned

![alt text](./images/Addon%20guild%20chat%20into%20discord.png)
