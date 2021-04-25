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
  
  
class Target(commands.Converter):
  async def convert(self, ctx, argument):
    try:
      arg = int(argument)
    except:
      if "<" and ">" in argument:
        arg = int(argument.strip("<@&>"))
        res = discord.utils.find(lambda r: r.id == arg, ctx.guild.roles)
        if res == None:
          res = discord.utils.find(lambda m: m.id == arg, ctx.guild.members)
      else:
        arg = argument
        res = discord.utils.find(lambda r: r.name == arg, ctx.guild.roles)
        if res == None: res = discord.utils.find(lambda m: m.name == arg, ctx.guild.members)
        if res == None: res = discord.utils.find(lambda m: m.display_name == arg, ctx.guild.members)
    else:
      res = discord.utils.find(lambda r: r.id == arg, ctx.guild.roles)
      if res == None:
        res = discord.utils.find(lambda m: m.id == arg, ctx.guild.members)
    return res

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
  @commands.has_permissions(manage_channels=True)
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
  async def changepermission(self, ctx, c:AChannel, t, opt, p, r=None):
    await ctx.message.edit(delete_after=5.0)
    o = True if opt == "add" else False
    dp = c.overwrites
    print(dp)
    prm = p.split(",")
    for p in prm:
      if p == "03": dp.update(manage_permissions=o)
      elif p == "04": dp.update(manage_channels=o)
      elif p == "20": dp.update(view_channel=o)
      if type(c) == discord.TextChannel:
        if p == "05": dp.update(manage_messages=o)
        elif p == "08": dp.update(manage_webhooks=o)
        elif p == "17": dp.update(mention_everyone=o)
        elif p == "19": dp.update(create_instant_invite=o)
        elif p == "21": dp.update(read_messages=o)
        elif p == "22": dp.update(read_message_history=o)
        elif p == "23": dp.update(send_messages=o)
        elif p == "24": dp.update(send_tts_messages=o)
        elif p == "25": dp.update(attach_files=o)
        elif p == "26": dp.update(embed_links=o)
        elif p == "27": dp.update(add_reactions=o)
        elif p == "28": dp.update(use_external_emojis=o)
        else: pass
      elif type(c) == discord.VoiceChannel:
        if p == "13": dp.update(mute_members=o)
        elif p == "14": dp.update(deafen_members=o)
        elif p == "15": dp.update(move_members=o)
        elif p == "16": dp.update(priority_speaker=o)
        elif p == "29": dp.update(connect=o)
        elif p == "30": dp.update(speak=o)
        elif p == "31": dp.update(stream=o)
        elif p == "32": dp.update(use_voice_activation=o)
        else: pass
    await c.edit(overwrites=dp, reason=None)
    return await ctx.send(f"☑️ チャンネル '{c.name}' の権限を変更しました",delete_after=10.0)

  @channel.command(aliases=["arcv"])
  async def archive(self, ctx, c:AChannel, r=None):
    await ctx.message.edit(delete_after=5.0)
    cc = ctx.guild.get_channel(769864008890580992)
    await c.edit(category=cc, position=0, reason=r)
    return await ctx.send(f"☑️ チャンネル '{c.name}' をアーカイブへ移動しました",delete_after=10.0)
  
  @channel.command(aliases=["pblc"])
  async def public(self, ctx, c:AChannel, r=None):
    await ctx.message.edit(delete_after=5.0)
    
    

def setup(bot):
  bot.add_cog(ChannelSystem(bot))
