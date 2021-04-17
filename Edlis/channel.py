#python 3.9.2
#coding: utf-8

import discord
from discord.ext import commands

class AChannel(commands.Converter):
  async def convert(self, ctx, argument):
    try:
      arg = int(argument)
    except:
      if "<" and ">" in argument:
        arg = int(argument.strip("<#>"))
        res = discord.utils.find(lambda c: c.id == arg, ctx.guild.channels)
      else:
        arg = argument
        res = discord.utils.find(lambda c: c.name == arg, ctx.guild.channels)
    else:
      res = discord.utils.find(lambda c: c.id == arg, ctx.guild.channels)
    return res
    
    
class Position(commands.Converter):
  async def convert(self, ctx, argument):
    try:
      arg = int(argument)
    except:
      if "<" and ">" in argument:
        arg = int(argument.strip("<#>"))
        res = discord.utils.find(lambda c: c.id == arg, ctx.guild.channels)
        pos = res.position
      else:
        arg = argument
        res = discord.utils.find(lambda c: c.name == arg, ctx.guild.channels)
        pos = res.position
    else:
      if len(arg) >= 3:
        res = discord.utils.find(lambda c: c.id == arg, ctx.guild.channels)
        pos = res.position
      else: pos = arg
    return pos


class ChannelSystem(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot
    
  @commands.group(aliases=["c"])
  async def channel(self, ctx):
    if ctx.invoked_subcommand is None:
      return await ctx.send("サブコマンドが必要です\n詳しくは`e:channel commandslist`をご確認ください",delete_after=5.0)
      
  @channel.command(aliases=["cmdl"])
  async def commandslist(self, ctx):
    fg = [
        "commandslist`(cmdl)`",
        "info {`チャンネル名、ID`}",
        "create`(crat)` {`チャンネル名`} {`タイプ`}\n    [`カテゴリー名、ID`] [`理由`]",
        "delete`(delt)` {`チャンネル名、ID`} [`理由`]",
        "move {`チャンネル名、ID`} {`ターゲット`} [`理由`]",
        "clone`(clon)` {`チャンネル名、ID`} [`理由`]",
        "changename`(chnm)` {`チャンネル名、ID`}\n    {`変更後の名称`} [`理由`]",
        "changepermission`(chpr)` {`チャンネル名、ID`}\n    {`ターゲット`} {`オプション`} {`権限値`} [`理由`]",
        "archive`(arcv)` {`チャンネル名、ID`} [`理由`]",
        "public`(pblc)` {`チャンネル名、ID`} [`理由`]",
        "private`(prvt)` {`チャンネル名、ID`} [`理由`]"
    ]
    f = "・" + "\n・".join(fg)
    e = discord.Embed(title="Edlisのヘルプ ℹ️")
    e.add_field(name="★ チャンネルコマンド一覧",value=f)
    e.set_author(name=f"To {ctx.author.display_name}",icon_url=ctx.author.avatar_url)
    e.set_footer(text="ヒント｜e:cmdhでコマンドの詳細を確認できます…")
    return await ctx.send(embed=e)
    
  @channel.command()
  async def info(self, ctx, c:AChannel):
    e = discord.Embed(title="チャンネルの基本情報 📄")
    fc = {
      "☆ チャンネル名":c.name,
      "❖ チャンネルID":f"`{c.id}`",
      "◆ 位置カテゴリ":f"`{c.category.name} `",
      "◇ チャンネル作成日":f'`{c.created_at.strftime("%Y年%m月%d日 %H時%M分%S秒")}`'
    }
    for f in fc:
      e.add_field(name=f,value=fc[f])
    e.set_author(name=f"To {ctx.author.display_name}",icon_url=ctx.author.avatar_url)
    return await ctx.send(embed=e)
    
  @channel.command(aliases=["crat"])
  @commands.has_permissions(manage_channels)
  async def create(self, ctx, n, t, c:discord.CategoryChannel=None, r=None):
    await ctx.message.edit(delete_after=5.0)
    if c == None:
      if t == "-t":
        ch = await ctx.guild.create_text_channel(name=n, reason=r)
      elif t == "-v":
        ch = await ctx.guild.create_voice_channel(name=n, reason=r)
      else:
        return await ctx.send(f"⚠️ `タイプ`は`-t`または`-v`で指定してください",delete_after=5.0)
      return await ctx.send(f"☑️ チャンネル '{ch.name}' を作成しました`(id: {ch.id})`")
    else:
      if t == "-t":
        ch = await c.create_text_channel(name=n, reason=r)
      elif t == "-v":
        ch = await c.create_voice_channel(name=n, reason=r)
      else:
        return await ctx.send(f"⚠️ `タイプ`は`-t`または`-v`で指定してください",delete_after=5.0)
      return await ctx.send(f"☑️ チャンネル '{ch.name}' をカテゴリ '{c.name}' に作成しました`(id: {ch.id})`")
    
  @channel.command(aliases=["delt"])
  @commands.has_permissions(manage_channels=True)
  async def delete(self, ctx, c:AChannel, r=None):
    await ctx.message.edit(delete_after=5.0)
    await c.delete(reason=r)
    return await ctx.send(f"☑️ チャンネル '{c.name}' を削除しました",delete_after=5.0)
    
  @channel.command()
  @commands.has_permissions(manage_channels=True)
  async def move(self, ctx, c:AChannel, p:Position, r=None):
    await ctx.message.edit(delete_after=5.0)
    await c.edit(position=p+1, reason=r)
    return await ctx.send(f"☑️ チャンネル '{c.name}' の位置を変更しました`(位置: {p})`",delete_after=10.0)
  
  @channel.command(aliases=["clon"])
  @commands.has_permissions(manage_channels=True)
  async def clone(self, ctx, c:AChannel, p:Position=None, r=None):
    await ctx.message.edit(delete_after=5.0)
    ch = await c.clone(reason=r)
    if not p == None:
      await ch.edit(position=p)
    return await ctx.send(f"☑️ チャンネル '{c.name}' を複製しました`(位置: {ch.position})`",delete_after=10.0)
  
  @channel.command(aliases=["chnm"])
  @commands.has_permissions(manage_channels=True)
  async def changename(self, ctx, c:AChannel, an, r=None):
    await ctx.message.edit(delete_after=5.0)
    n = c.name
    await c.edit(name=an,reason=r)
    return await ctx.send(f"☑️ チャンネル '{n}' の名称を '{an}' に変更しました",delete_after=10.0)
    
  @channel.command(aliases=["chpr"])
  @commands.has_permissions(manage_guild=True)
  async def changepermission(self, ctx, c:AChannel, o, p, r=None):
    await ctx.message.edit(delete_after=5.0)


def setup(bot):
  bot.add_cog(ChannelSystem(bot))