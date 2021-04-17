#python 3.9.2
#coding: utf-8

import discord
from discord.ext import commands

class RoleSystem(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot
    
  @commands.group(aliases=["r"])
  async def role(self, ctx):
    if ctx.invoked_subcommand is None:
      return await ctx.send("⚠️ サブコマンドが必要です",delete_after=5.0)
      
  @role.command(aliases=["cmdl"])
  async def commandslist(self, ctx):
    fr = [
      "commandslist`(cmdl)`",
      "info {`ロール名、ID`}",
      "permissions`(prms)` {`ロール名、ID`}",
      "members`(mebs)` {`ロール名、ID`}",
      "create`(crat)` {`ロール名`} [`権限値`] [`理由`]",
      "delete`(dlet)` {`ロール名、ID`} [`理由`]",
      "move {`ロール名、ID`} {`ターゲット`} [`理由`]",
      "changename`(chnm)` {`ロール名、ID`}\n{`変更後の名称`} [`理由`]",
      "changepermissions`(chpr)` {`ロール名、ID`}\n{`オプション`} {`権限値`} [`理由`]"
    ]
    f = "・" + "\n・".join(fr)
    e = discord.Embed(title="Edlisのヘルプ ℹ️")
    e.add_field(name="★ ロールコマンド一覧",value=f)
    e.set_author(name=f"To {ctx.author.display_name}",icon_url=ctx.author.avatar_url)
    e.set_footer(text="ヒント｜e:cmdhでコマンドの詳細を確認できます…")
    return await ctx.send(embed=e)
    
  @role.command()
  async def info(self, ctx, r:discord.Role):
    e = discord.Embed(title="ロールの基本情報 📄")
    fd = {
      "☆ ロール名":r.name,
      "◆ ロールID":f"`{r.id}`",
      "❖ サーバー内位置":f"`{r.position}`",
      "◇ 作成された日時":f"`{r.created_at.strftime('%Y年%m月 %H時%M分%S秒')}`"
    }
    for f in fd:
      e.add_field(name=f,value=fd[f],inline=False)
    e.set_author(name=f"To {ctx.author.display_name}",icon_url=ctx.author.avatar_url)
    return await ctx.send(embed=e)
    
  @role.command(aliases=["prms"])
  async def permissions(self, ctx, r:discord.Role, page:int=1):
    prs = [x[0] for x in r.permissions if x[1] == True]
    perms_dict = {
      'add_reactions':        "27: `リアクションを追加`",
      'administrator':        "00: `管理者`",
      'attach_files':         "25: `ファイルを添付`",
      'ban_members':          "11: `メンバーをBAN`",
      'change_nickname':      "18: `ニックネームを変更`",
      'connect':              "29: `ボイスチャンネルに接続`",
      'create_instant_invite':"19: `招待を作成`",
      'deafen_members':       "14: `メンバーをスピーカーミュート`",
      'embed_links':          "26: `埋め込みリンク`",
      'external_emojis':      "28: `外部の絵文字を使用`",
      'kick_members':         "12: `メンバーをKick`",
      'manage_channels':      "04: `チャンネルを管理`",
      'manage_emojis':        "06: `絵文字を管理`",
      'manage_guild':         "01: `サーバーを管理`",
      'manage_messages':      "05: `メッセージを管理`",
      'manage_nicknames':     "07: `ニックネームを管理`",
      'manage_permissions':   "03: `権限を管理`",
      'manage_roles':         "02: `役職を管理`",
      'manage_webhooks':      "08: `ウェブフックを管理`",
      'mention_everyone':     "17: `@everyoneにメンション`",
      'move_members':         "15: `メンバーを移動`",
      'mute_members':         "13: `メンバーをミュート`",
      'priority_speaker':     "16: `優先スピーカー`",
      'read_message_history': "22: `メッセージ履歴を読む`",
      'read_messages':        "21: `メッセージを読む`",
      'send_messages':        "23: `メッセージを送信`",
      'send_tts_messages':    "24: `TTSメッセージを送信`",
      'speak':                "30: `ボイスチャンネルで発言`",
      'stream':               "31: `ボイスチャンネルで配信`",
      'use_external_emojis':  "28: `外部の絵文字を使用`",
      'use_voice_activation': "32: `音声検出を使用`",
      'view_audit_log':       "09: `監査ログを表示`",
      'view_channel':         "20: `チャンネルを見る`",
      'view_guild_insights':  "10: `サーバーインサイトを見る`"
    }
    ps, es, prv = [], [], sorted([perms_dict[x] for x in prs])
    for p in prv:
      ps.append(p)
      if len(ps) == 10:
        v = "\n".join(ps)
        e = discord.Embed(title=f"{r.name}の所持する権限一覧 📒")
        e.add_field(name=f"権限数 : {len(prs)}",value=v)
        es.append(e)
        ps = []
    if len(ps) > 0:
      v = "\n".join(ps)
      e = discord.Embed(title=f"{r.name}の所持する権限一覧 📒")
      e.add_field(name=f"権限数 : {len(prs)}",value=v)
      es.append(e)
    e = es[page-1]
    e.set_author(name=f"To {ctx.author.display_name}",icon_url=ctx.author.avatar_url)
    return await ctx.send(embed=e)
    
  @role.command(aliases=["mebs"])
  async def members(self, ctx, r:discord.Role, page:int=1):
    ms, es, mbs = [], [], [m.display_name for m in r.members]
    for m in mbs:
      ms.append(m)
      if len(ms) == 10:
        v = "@" + "\n@".join(ms)
        e = discord.Embed(title=f"{r.name}を所持するメンバー一覧 📒")
        e.add_field(name=f"メンバー数 : {len(mbs)}",value=v)
        es.append(e)
        ms = []
    if len(ms) > 0:
      v = "@" + "\n@".join(ms)
      e = discord.Embed(title=f"{r.name}を所持するメンバー一覧 📒")
      e.add_field(name=f"メンバー数 : {len(mbs)}",value=v)
      es.append(e)
    e = es[page-1]
    e.set_author(name=f"To {ctx.author.display_name}",icon_url=ctx.author.avatar_url)
    return await ctx.send(embed=e)
    
  @role.command(aliases=["crat"])
  @commands.has_permissions(manage_roles=True)
  async def create(self, ctx, name, prms=None, reason=None):
    await ctx.message.edit(delete_after=5.0)
    if prms==None:
      r = await ctx.guild.create_role(name=name, reason=reason)
    else:
      dp = discord.Permissions()
      pl = prms.split(",")
      for p in pl:
        if p == "00": dp.update(administrator=True)
        elif p == "01": dp.update(manage_guild=True)
        elif p == "02": dp.update(manage_roles=True)
        elif p == "03": dp.update(manage_permissions=True)
        elif p == "04": dp.update(manage_channels=True)
        elif p == "05": dp.update(manage_messages=True)
        elif p == "06": dp.update(manage_emojis=True)
        elif p == "07": dp.update(manage_nicknames=True)
        elif p == "08": dp.update(manage_webhooks=True)
        elif p == "09": dp.update(view_audit_log=True)
        elif p == "10": dp.update(view_guild_insights=True)
        elif p == "11": dp.update(ban_members=True)
        elif p == "12": dp.update(kick_members=True)
        elif p == "13": dp.update(mute_members=True)
        elif p == "14": dp.update(deafen_members=True)
        elif p == "15": dp.update(move_members=True)
        elif p == "16": dp.update(priority_speaker=True)
        elif p == "17": dp.update(mention_everyone=True)
        elif p == "18": dp.update(change_nickname=True)
        elif p == "19": dp.update(create_instant_invite=True)
        elif p == "20": dp.update(view_channel=True)
        elif p == "21": dp.update(read_messages=True)
        elif p == "22": dp.update(read_message_history=True)
        elif p == "23": dp.update(send_messages=True)
        elif p == "24": dp.update(send_tts_messages=True)
        elif p == "25": dp.update(attach_files=True)
        elif p == "26": dp.update(embed_links=True)
        elif p == "27": dp.update(add_reactions=True)
        elif p == "28": dp.update(use_external_emojis=True)
        elif p == "29": dp.update(connect=True)
        elif p == "30": dp.update(speak=True)
        elif p == "31": dp.update(stream=True)
        elif p == "32": dp.update(use_voice_activation=True)
        else: pass
      r = await ctx.guild.create_role(name=name, permissions=dp, reason=reason)
    return await ctx.send(f"☑️ ロール '{r.name}' を作成しました`(id: {r.id})`")
  
  @role.command(aliases=["dlet"])
  @commands.has_permissions(manage_roles=True)
  async def delete(self, ctx, r:discord.Role, reason=None):
    await ctx.message.edit(delete_after=5.0)
    await r.delete(reason=reason)
    return await ctx.send(f"☑️ ロール '{r.name}' を削除しました",delete_after=10.0)
  
  @role.command()
  @commands.has_permissions(manage_roles=True)
  async def move(self, ctx, r:discord.Role, t:int, reason=None):
    await ctx.message.edit(delete_after=5.0)
    if len(str(t)) <= 3:
      await r.edit(position=t)
    else:
      tr = ctx.guild.get_role(t)
      t = tr.position
      await r.edit(position=t-1)
    return await ctx.send(f"☑️ {r.name} の位置を変更しました",delete_after=10.0)
  
  @role.command(aliases=["chnm"])
  @commands.has_permissions(manage_roles=True)
  async def changename(self, ctx, r:discord.Role, name, reason=None):
    await ctx.message.edit(delete_after=5.0)
    on = r.name
    await r.edit(name=name, reason=reason)
    return await ctx.send(f"☑️ ロール '{on}' の名称を '{name}' に変更しました",delete_after=10.0)
    
  @role.command(aliases=["chpr"])
  @commands.has_permissions(manage_roles=True)
  async def changepermissions(self, ctx, r:discord.Role, o, prms, reason=None):
    await ctx.message.edit(delete_after=5.0)
    od = {"add":True,"remove":False}
    if o not in od:
      return await ctx.send("⚠️ `オプション`は`add`または`remove`で指定してください")
    o = od[o]
    dp = r.permissions
    pl = prms.split(",")
    for p in pl:
      if p == "00": dp.update(administrator=o)
      elif p == "01": dp.update(manage_guild=o)
      elif p == "02": dp.update(manage_roles=o)
      elif p == "03": dp.update(manage_permissions=o)
      elif p == "04": dp.update(manage_channels=o)
      elif p == "05": dp.update(manage_messages=o)
      elif p == "06": dp.update(manage_emojis=o)
      elif p == "07": dp.update(manage_nicknames=o)
      elif p == "08": dp.update(manage_webhooks=o)
      elif p == "09": dp.update(view_audit_log=o)
      elif p == "10": dp.update(view_guild_insights=o)
      elif p == "11": dp.update(ban_members=o)
      elif p == "12": dp.update(kick_members=o)
      elif p == "13": dp.update(mute_members=o)
      elif p == "14": dp.update(deafen_members=o)
      elif p == "15": dp.update(move_members=o)
      elif p == "16": dp.update(priority_speaker=o)
      elif p == "17": dp.update(mention_everyone=o)
      elif p == "18": dp.update(change_nickname=o)
      elif p == "19": dp.update(create_instant_invite=o)
      elif p == "20": dp.update(view_channel=o)
      elif p == "21": dp.update(read_messages=o)
      elif p == "22": dp.update(read_message_history=o)
      elif p == "23": dp.update(send_messages=o)
      elif p == "24": dp.update(send_tts_messages=o)
      elif p == "25": dp.update(attach_files=o)
      elif p == "26": dp.update(embed_links=o)
      elif p == "27": dp.update(add_reactions=o)
      elif p == "28": dp.update(use_external_emojis=o)
      elif p == "29": dp.update(connect=o)
      elif p == "30": dp.update(speak=o)
      elif p == "31": dp.update(stream=o)
      elif p == "32": dp.update(use_voice_activation=o)
      else: pass
    await r.edit(permissions=dp, reason=reason)
    return await ctx.send(f"☑️ ロール '{r.name}' の権限設定を変更しました",delete_after=10.0)
  
  
def setup(bot):
  bot.add_cog(RoleSystem(bot))
