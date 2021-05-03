#coding: utf-8

import discord, random
from discord.ext import commands

class HobbySystem(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot 
    
  @commands.group(aliases=["h"])
  async def hobby(self, ctx):
    if ctx.invoked_subcommand is None:
      return await ctx.send("サブコマンドが必要です\n詳細は`e:hobby commandslist`をご確認ください")
  
  @hobby.command(aliases=["cmdl"])
  async def commandslist(self, ctx):
    e = discord.Embed(title="Edlisのヘルプℹ️")
    fh = [
      "say {`メッセージ`}",
      "omikuji",
      "randomint [`下限/上限`]"
    ]
    f = "\n".join(fh)
    e.add_field(name="★ ホビーコマンド一覧",value=f)
    e.set_footer(text="ヒント｜e:cmdhで詳細を確認できます")
    e.set_author(name=f"To {ctx.author.display_name}",icon_url=ctx.author.avatar_url)
    return await ctx.send(embed=e)
  
  @hobby.command()
  async def say(self, ctx, msg):
    await ctx.message.edit(delete_after=0.01)
    ch = self.bot.get_channel(819504951583572009)
    e = discord.Embed(title=msg)
    e.set_author(name=f"by {ctx.author.display_name}")
    await ctx.send(msg)
    return await ch.send(embed=e)
  
  @hobby.command(aliases=["omkj"])
  async def omikuji(self, ctx):
    r = random.randint(0,99)
    if r < 10: m = ["大吉","きっと、とても良いことが起こるでしょう！"]
    elif 10 <= r < 25: m = ["吉","もしかすると、良い1日になるかもしれません〜"]
    elif 25 <= r < 40: m = ["中吉","ちょっと良いことが起こるかも…？"]
    elif 40 <= r < 55: m = ["小吉","今日は大事も無く過ごせそうです"]
    elif 55 <= r < 75: m = ["末吉","特に何も起こらなさそうです"]
    elif 75 <= r < 90: m = ["凶","今日は注意しましょう…"]
    elif 90 <= r < 100: m = ["大凶","非常に不味いです………"]
    return await ctx.send(f"あなたの運勢は… ||{m[0]}||です！\n{m[1]}")
  
def setup(bot):
  bot.add_cog(HobbySystem(bot))
