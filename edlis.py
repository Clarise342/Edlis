#python 3.8.0
#coding: utf-8

import discord, sys
from discord.ext import tasks, commands

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
  
  @bot.command()
  async def exit(ctx):
    await ctx.message.edit(delete_after=5.0)
    await bot.logout()
    await sys.exit()
  
  @bot.command(name="reload")
  async def cogreload(ctx):
    await ctx.message.edit(delete_after=5.0)
    for c in extensions:
      try:
        bot.unload_extension(c)
      except:
        pass
      
    scs = []
    for c in extensions:
      try:
        bot.load_extension(c)
      except Exception as e:
        print(f"Error >> Could not load extension {c}")
        print(e)
      else:
        scs.append(c)
    await ctx.send(f"☑️ {len(extensions)} 個の内、{len(scs)} 個のコグのreloadが完了しました",delete_after=10.0)
    return print("reloadが完了しました")
  
  bot.run('ODEyMzE3MDA5ODQ5MjIxMTgw.YC-_Kw.lZrpdWqoks_J6jlh7m9-t92GX5E')
