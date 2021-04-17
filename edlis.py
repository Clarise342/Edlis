#python 3.8.0
#coding: utf-8

import discord, sys, os
from discord.ext import tasks, commands

token = os.environ["TOKEN"]
intents = discord.Intents.default()
intents.members = True

extensions = [
  "Edlis.general",
  "Edlis.member",
  "Edlis.guild",
  "Edlis.role",
  "Edlis.channel"
]

class Edlis(commands.Bot):
  
  def __init__(self, command_prefix):
    super().__init__(command_prefix, intents=intents)
    
    for c in extensions:
      try:
        self.load_extension(c)
      except Exception as e:
        print(f"Error >> Could not load extension {c}")
        print(e)
      
  async def on_ready(self):
    return print("Edlisさんは起床しました！")
  
    
if __name__ == "__main__":
  bot = Edlis(command_prefix="e:")
  
  bot.run(token)
