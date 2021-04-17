#python 3.7.1
#coding: utf-8

import discord, asyncio
from discord.ext import commands

def embe(self, txts, leng, t_type_j):
  e = discord.Embed(title=f"EDSの{t_type_j}一覧 📒")
  text = "\n".join(txts)
  e.add_field(name=f"{t_type_j}数 : {leng}",value=text)
  e.set_author(name=f"To {ctx.author.display_name}",icon_url=ctx.author.avatar_url)
  e.set_footer(text="長さの関係上、ページを分割しています")
  return e

class GuildSystem(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot
       
  @commands.group(aliases=["g"])
  async def guild(self, ctx):
    if ctx.invoked_subcommand is None:
      return await ctx.send("サブコマンドが必要です\n詳しくは`e:guild commandshelp`をご確認ください",delete_after=5.0)
      
  @guild.command(aliases=["cmdl"])
  async def commandslist(self, ctx):
    fg = [
        "commandslist`(cmdl)`",
        "info",
        "icon",
        "roles`(rols)` [`ページ`]",
        "channels`(chns)` [`ページ`]",
        "emojis`(emjs)` [`ページ`]",
        "members`(mebs)` [`ページ`]",
        "`bans` [`ページ`]",
        "createinvite`(criv)` {`有効期間`} {`有効使用回数`}\n    [`理由`]",
        "changename`(chnm)` {`変更後の名称`} [`理由`]",
        "changeicon`(chic)` {`画像`} [`理由`]",
        "changeafkchannel`(chac)`\n    {`ボイスチャンネル名、ID`} [`理由`]",
        "changeafktime`(chat)` \n    {`タイムアウト時間`} [`理由`]",
        "changesystemchannel`(chsc)` \n    {`テキストチャンネル名、ID`} [`理由`]",
        "changenotification`(chnf)` {`通知レベル`} [`理由`]",
        "changeverification`(chvf)` {`認証レベル`} [`理由`]",
        "changefilter`(chft)` {`スキャンレベル`} [`理由`]"
    ]
    f = "・" + "\n・".join(fg)
    e = discord.Embed(title="Edlisのヘルプ ℹ️")
    e.add_field(name="★ サーバーコマンド一覧",value=f)
    e.set_author(name=f"To {ctx.author.display_name}",icon_url=ctx.author.avatar_url)
    e.set_footer(text="ヒント｜e:cmdhでコマンドの詳細を確認できます…")
    return await ctx.send(embed=e)
    
  @guild.command()
  async def info(self, ctx):
    e = discord.Embed(title="EDSの基本情報 📄")
    afc = ctx.guild.afk_channel.name if not ctx.guild.afk_channel == None else "なし"
    syc = ctx.guild.system_channel.name if not ctx.guild.system_channel == None else "なし"
    fdg = {
      "☆ 現在の名称":ctx.guild.name,
      "◆ EDSの爆誕日":ctx.guild.created_at.strftime("%Y年%m月%d日 %H時%M分"),
      "❖ EDSの所有者":ctx.guild.owner.display_name,
      "◇ AFK時間":str(ctx.guild.afk_timeout/5),
      "○ AFKチャンネル":afc,
      "□ システムチャンネル":syc
    }
    for f in fdg:
      e.add_field(name=f,value=fdg[f],inline=False)
    e.set_author(name=f"To {ctx.author.display_name}",icon_url=ctx.author.avatar_url)
    return await ctx.send(embed=e)
    
  @guild.command()
  async def icon(self, ctx):
    e = discord.Embed(title="EDSのアイコン 👤")
    e.set_image(url=ctx.guild.icon_url)
    e.set_author(name=f"To {ctx.author.display_name}",icon_url=ctx.author.avatar_url)
    return await ctx.send(embed=e)
    
  @guild.command(aliases=["rols"])
  async def roles(self, ctx, page:int=0):
    rls = ctx.guild.roles
    let = len(rls)
    vls = [x.name for x in rls]
    txs, ems = [], []
    for v in vls:
      txts.append("**@"+v+"**")
      if len(txts) == 10:
        e = embe(self,txs,let,"ロール")
        ems.append(e)
        txs = []
    if not len(txs) == 0:
      e = embe(self,txs,let,"ロール")
      ems.append(e)
    return await ctx.send(embed=ems[page])
    
  @guild.command(aliases=["chns"])
  async def channels(self, ctx, page:int=0):
    chs = ctx.guild.channels
    let = len(channels)
    vls = [x.name for x in chs]
    txs, ems = [], []
    for v in vls:
      txs.append("**#"+v+"**")
      if len(txs) == 10:
        e = embe(self,txs,let,"チャンネル")
        ems.append(e)
        txt = []
    if not len(txt) == 0:
      e = embe(self,txt,let,"チャンネル")
      ems.append(e)
    return await ctx.send(embed=ems[page])
    
  @guild.command(aliases=["mebs"])
  async def members(self, ctx, page:int=0):
    mbs = ctx.guild.members
    let = len(mbs)
    vls = [x.display_name for x in mbs]
    txs, ems = [], []
    for v in vls:
      txs.append("**@"+v+"**")
      if len(txs) == 10:
        e = embe(self,txs,let,"メンバー")
        ems.append(e)
        txs = []
    if not len(txs) == 0:
      e = embe(self,txs,let,"メンバー")
      ems.append(e)
    return await ctx.send(embed=ems[page])
    
  @guild.command(aliases=["emjs"])
  async def emojis(self, ctx, page:int=0):
    ejs = ctx.guild.emojis
    let = len(ejs)
    vls = [f"{x} ({x.name})" for x in ejs]
    txs, ems = [], []
    for v in vls:
      txs.append(v)
      if len(txs) == 10:
        e = embe(self,txs,let,"絵文字")
        ems.append(e)
        txs = []
    if not len(txs) == 0:
      e = embe(self,txs,let,"絵文字")
      ems.append(e)
    return await ctx.send(embed=ems[page])
    
  @guild.command()
  async def bans(self, ctx, page:int=0):
    bns = await ctx.guild.bans()
    let = len(bns)
    vls = [f"{x.user.name}**\n`理由: {x.reason}`" for x in bns]
    txs, ems = [], []
    for v in vls:
      txs.append("**@"+v)
      if len(txs) == 10:
        e = embe(self,txs,let,"BANされたメンバー")
        ems.append(e)
        txs = []
    if not len(txs) == 0:
      e = embe(self,txs,let,"BANされたメンバー")
      ems.append(e)
    return await ctx.send(embed=ems[page])
     
  @guild.command(aliases=["criv"])
  async def createinvite(self, ctx, validperiod:int, validtimes:int, reason=None):
    await ctx.message.edit(delete_after=5.0)
    vlp = validperiod * 60
    ch = ctx.guild.get_channel(733721209124028456)
    inv = await ch.create_invite(max_age=vlp, max_uses=validtimes, reason=reason)
    e = discord.Embed(title="☑️ 招待を作成しました")
    e.add_field(name="☆ 作成された招待のURL",value=f"[コピーはこちら]({inv.url})")
    e.set_author(name=f"To {ctx.author.display_name}",icon_url=ctx.author.avatar_url)
    validperiod = "無制限" if validperiod == 0 else f"{validperiod}分"
    validtimes = "無制限" if validtimes == 0 else f"{validtimes}回"
    e.set_footer(text=f"有効期限 : {validperiod}\n有効回数 : {validtimes}")
    return await ctx.send(embed=e)
    
  @guild.command(aliases=["chnm"])
  @commands.has_permissions(administrator=True)
  async def changename(self, ctx, aftername, reason=None):
    await ctx.message.edit(delete_after=5.0)
    e = discord.Embed(title="⚠️ 変更前に確認します")
    e.add_field(name="変更内容",value=f"```\n{ctx.guild.name} ⇢ {aftername}\n```")
    e.set_author(name="Edlis.Guild.Changename",icon_url=self.bot.user.avatar_url)
    e.set_footer(text="実行しますか？ Y or N")
    em = await ctx.send(embed=e)
    try:
      m = await self.bot.wait_for('message', timeout=20.0, check=lambda m: m.author == ctx.author and m.content in ["Y","N"])
      if m.content == "Y":
        await em.edit(delete_after=1.0)
        await m.edit(delete_after=1.0)
        await ctx.guild.edit(name=aftername, reason=reason)
        return await ctx.send(f"☑️ サーバーの名称を {aftername} に変更しました",delete_after=10.0)
      else:
        await em.edit(delete_after=1.0)
        return await ctx.send("☑️変更を破棄しました",delete_after=5.0)
    except asyncio.TimeoutError:
      await em.edit(delete_after=1.0)
      return await ctx.send("☑️ 20秒以内に応答が無かったため、変更を破棄しました",delete_after=5.0)
     
  @guild.command(aliases=["chic"])
  @commands.has_permissions(manage_guild=True)
  async def changeicon(self, ctx, reason=None):
    await ctx.message.edit(delete_after=5.0)
    if ctx.message.attachments == None:
      return await ctx.send("⚠️ 画像が必要です…",delete_after=5.0)
    image = await ctx.message.attachments[0].read()
    await ctx.guild.edit(icon=image, reason=reason)
    return await ctx.send("☑️ サーバーのアイコン画像を変更しました",delete_after=10.0)
    
  @guild.command(aliases=["chac"])
  @commands.has_permissions(manage_channels=True)
  async def changeafkchannel(self, ctx, channel:discord.VoiceChannel, reason=None):
    await ctx.message.edit(delete_after=5.0)
    await ctx.guild.edit(afk_channel=channel, reason=reason)
    return await ctx.send(f"☑️ AFKチャンネルを {channel.name} に変更しました",delete_after=10.0)
    
  @guild.command(aliases=["chat"])
  @commands.has_permissions(manage_channels=True)
  async def changeafktime(self, ctx, times:int, reason=None):
    await ctx.message.edit(delete_after=5.0)
    if times in [1,5,15,30,60]:
      await ctx.guild.edit(afk_timeout=times*60, reason=reason)
      return await ctx.send(f"☑️ AFKまでの時間を {times}分 に変更しました",delete_after=10.0)
    else:
      return await ctx.send(f"⚠️ `1分`、`5分`、`15分`、`30分`、`60分`から選んでください",delete_after=5.0)
    
  @guild.command(aliases=["chsc"])
  @commands.has_permissions(manage_channels=True)
  async def changesystemchannel(self, ctx, channel:discord.TextChannel, reason=None):
    await ctx.message.edit(delete_after=5.0)
    await ctx.guild.edit(system_channel=channel, reason=reason)
    return await ctx.send(f"☑️ システムチャンネルを {channel.name} に変更しました",delete_after=10.0)
    
  @guild.command(aliases=["chnf"])
  @commands.has_permissions(manage_guild=True)
  async def changenotification(self, ctx, nfctlevel:int, reason=None):
    await ctx.message.edit(delete_after=5.0)
    nfs = [discord.NotificationLevel.only_mentions,
           discord.NotificationLevel.all_messages]
    nfv = {discord.NotificationLevel.only_mentions:"メンションのみ通知",
           discord.NotificationLevel.all_messages:"全て通知"}
    dv, nv = nfv[ctx.guild.default_notifications], nfv[nfs[nfctlevel]]
    e = discord.Embed(title="⚠️ 変更前に確認します")
    e.add_field(name="変更内容",value=f"```\n{dv} --> {nv}\n```")
    e.set_author(name=ctx.author.display_name,icon_url=ctx.author.avatar_url)
    e.set_footer(text="変更しますか？ Y or N")
    em = await ctx.send(embed=e)
    try:
      m = await self.bot.wait_for('message', timeout=20.0, check=lambda m: m.author == ctx.author and m.content in ["Y","N"])
      await em.edit(delete_after=1.0)
      await m.edit(delete_after=1.0)
      if m.content == "Y":
        await ctx.guild.edit(default_notifications=nfs[nfctlevel])
        return await ctx.send(f"☑️ 標準の通知設定を {nfv[nfs[nfctlevel]]} に変更しました",delete_after=10.0)
      else:
        return await ctx.send("☑️ 変更を破棄しました",delete_after=5.0)
    except asyncio.TimeoutError:
      return await ctx.send("☑️ 20秒以内に応答がなかった為、変更を破棄しました",delete_after=5.0)
    
  @guild.command(aliases=["chvf"])
  @commands.has_permissions(administrator=True)
  async def changeverification(self, ctx, vfctlevel:int, reason=None):
    await ctx.message.edit(delete_after=5.0)
    vfs = [discord.VerificationLevel.none,
           discord.VerificationLevel.low,
           discord.VerificationLevel.medium,
           discord.VerificationLevel.high,
           discord.VerificationLevel.extreme]
    vfv = {discord.VerificationLevel.none:"認証無",
           discord.VerificationLevel.low:"認証有(低)",
           discord.VerificationLevel.medium:"認証有(中)",
           discord.VerificationLevel.high:"認証有(高)",
           discord.VerificationLevel.extreme:"認証有(最高)"}
    dv, nv = vfv[ctx.guild.verification_level], vfv[vfs[vfctlevel]]
    e = discord.Embed(title="⚠️ 変更前に確認します")
    e.add_field(name="変更内容",value=f"```\n{dv} --> {nv}\n```")
    e.set_author(name=ctx.author.display_name,icon_url=ctx.author.avatar_url)
    e.set_footer(text="変更しますか？ Y or N")
    em = await ctx.send(embed=e)
    try:
      m = await self.bot.wait_for('message', timeout=20.0, check=lambda m: m.author == ctx.author and m.content in ["Y","N"])
      await em.edit(delete_after=1.0)
      await m.edit(delete_after=1.0)
      if m.content == "Y":
        await ctx.guild.edit(verification_level=vfs[vfctlevel])
        return await ctx.send(f"☑️ 認証設定を {vfv[vfs[vfctlevel]]} に変更しました",delete_after=10.0)
      else:
        return await ctx.send("☑️ 変更を破棄しました",delete_after=5.0)
    except asyncio.TimeoutError:
      return await ctx.send("☑️ 20秒以内に応答がなかった為、変更を破棄しました",delete_after=5.0)
    
  @guild.command(aliases=["chft"])
  @commands.has_permissions(manage_guild=True)
  async def changefilter(self, ctx, ftlevel:int, reason=None):
    await ctx.message.edit(delete_after=5.0)
    ffs = [discord.ContentFilter.disabled,
           discord.ContentFilter.all_members]
    ffv = {discord.ContentFilter.disabled:"なし",
           discord.ContentFilter.all_members:"全てスキャン"}
    dv, nv = ffv[ctx.guild.explicit_content_filter], ffv[ffs[ftlevel]]
    e = discord.Embed(title="⚠️ 変更前に確認します")
    e.add_field(name="変更内容",value=f"```\n{dv} --> {nv}\n```")
    e.set_author(name=ctx.author.display_name,icon_url=ctx.author.avatar_url)
    e.set_footer(text="変更しますか？ Y or N")
    em = await ctx.send(embed=e)
    try:
      m = await self.bot.wait_for('message', timeout=20.0, check=lambda m: m.author == ctx.author and m.content in ["Y","N"])
      await em.edit(delete_after=1.0)
      await m.edit(delete_after=1.0)
      if m.content == "Y":
        await ctx.guild.edit(explicit_content_filter=ffs[ftlevel])
        return await ctx.send(f"☑️ フィルターを {ffv[ffs[ftlevel]]} に変更しました",delete_after=10.0)
      else:
        return await ctx.send("☑️ 変更を破棄しました",delete_after=5.0)
    except asyncio.TimeoutError:
      return await ctx.send("☑️ 20秒以内に応答がなかった為、変更を破棄しました",delete_after=5.0)
    
def setup(bot):
  bot.add_cog(GuildSystem(bot))
