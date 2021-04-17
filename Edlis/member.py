#python 3.7.1
#coding: utf-8

import discord, asyncio
from discord.ext import commands
from datetime import datetime



class MemberSystem(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot
    self.cl = {
      "er":0xFFC20E
    }
    self.overroles = [
      785137663123914763,
      741638298027556955,
      776785215087050784,
      787169630409195591,
      801109518711783444,
      795277929000730644,
      741637203045908480,
      723177654362177586,
      711201258081615912,
      770880174820163624
    ]
    
    
  @commands.group(aliases=["m"])
  async def member(self, ctx):
    if ctx.invoked_subcommand is None:
      return await ctx.send("サブコマンドが必要です\n詳細は`e:member commandshelp`をご確認ください",delete_after=10.0)
    
  @member.command(aliases=["cmdl"])
  async def commandslist(self, ctx, page:int=1):
    e = discord.Embed(title="Edlisのヘルプ ℹ️")
    fc = [
      [
        "commandslist`(cmdl)` [`ページ`]",
        "info [`メンバー名・ID`]",
        "avatar`(avtr)` [`メンバー名・ID`]",
        "roles`(rols)` [`メンバー名・ID`]",
        "accessibles`(aces)` [`メンバー名・ID`]",
        "permissions`(prms)` [`メンバー名・ID`]",
        "changenick`(chnk)` {`変更後の名前`}\n    [`メンバー名・ID`]",
        "vcmute`(vcmt)` {`メンバー名・ID`}",
        "vcspeakermute`(vsmt)` {`メンバー名・ID`}",
        "vcmove`(vcmv)` {`チャンネル名・ID`}\n    {`メンバー名またはID`}",
        "vcunmute`(vumt)` {`メンバー名・ID`}",
        "vcunspeakermute`(vusm)` {`メンバー名・ID`}",
        "addrole`(adrl)` {`役職名・ID`} [`メンバー名・ID`]\n    [`理由`]"
      ],
      [
        "removerole`(rmrl)` {`役職名・ID`}\n     [`メンバー名・ID`] [`理由`]",
        "mute {`メンバー名・ID`} [`理由`]",
        "warn {`メンバー名・ID`} {`警告レベル`} [`理由`]",
        "kick {`メンバー名・ID`} [`理由`]",
        "ban {`メンバー名・ID`} [`メッセージ削除日数`]\n    [`理由`]",
        "unmute`(unmt)` {`メンバー名・ID`} [`理由`]",
        "unwarn`(unwn)` {`メンバー名・ID`} [`理由`]",
        "unban`(unbn)` {`ユーザーID`} [`理由`]",
        "vip {`メンバー名・ID`} {`VIPレベル`} [`理由`]",
        "admin`(admn)` {`メンバー名・ID`} {`権限レベル`}\n    [`理由`]",
        "unvip`(uvip)` {`メンバー名・ID`} [`理由`]",
        "unadmin`(uadm)` {`メンバー名・ID`} [`理由`]"
      ]
    ]
    v = "・" + "\n・".join(fc[page-1])
    e.add_field(name=f"★ メンバーコマンド一覧 (`{page}/2 ページ`)",value=v)
    e.set_author(name=f"To {ctx.author.display_name}",icon_url=ctx.author.avatar_url)
    e.set_footer(text="ヒント｜e:cmdhでコマンドの詳細を確認できます…")
    return await ctx.send(embed=e)
      
  @member.command()
  async def info(self, ctx, member:discord.Member=None):
    if member == None: member = ctx.author
    e = discord.Embed(title="メンバーの基本情報 📄")
    bb = {False:"このメンバーはBotではありません",True:"このメンバーはBotです"}[member.bot]
    fdm = {
      "❖ メンバー名":member.display_name,
      "◆ メンバーID":f"`{member.id}`",
      "○ BOT":f"`{bb}`",
      "☆ 最高役職":f"{member.top_role.name}`({member.top_role.id})`",
      "◇ アカウント作成":f'`{member.created_at.strftime("%Y年 %m月%d日 %H時%M分")}`',
      "□ サーバーへの参加":f'`{member.joined_at.strftime("%Y年 %m月%d日 %H時%M分")}`'
    }
    for f in fdm:
      e.add_field(name=f,value=fdm[f])
    e.set_thumbnail(url=member.avatar_url)
    e.set_author(name=f"To {ctx.author.display_name}",icon_url=ctx.author.avatar_url)
    return await ctx.send(embed=e)
    
  @member.command(aliases=["avtr"])
  async def avatar(self, ctx, member:discord.Member=None):
    if member == None: member = ctx.author
    e = discord.Embed(title="メンバーのアバター画像 👤")
    e.set_image(url=member.avatar_url)
    e.set_author(name=f"To {ctx.author.display_name}",icon_url=ctx.author.avatar_url)
    return await ctx.send(embed=e)
    
  @member.command(aliases=["rols"])
  async def roles(self, ctx, page:int=1 ,member:discord.Member=None):
    if member == None: member = ctx.author
    roles = list(reversed(member.roles))
    rs, es, roles_n = [], [], list(map(lambda x: x.name, roles))
    for r in roles_n:
      rs.append(r)
      if len(rs) == 10:
        e = discord.Embed(title=f"{member.display_name}さんのロール一覧 📒")
        v = "**@" + "**\n**@".join(rs) + "**"
        e.add_field(name=f"❖ ロール数 : {len(roles)}",value=v)
        es.append(e)
        rs = []
    if len(rs) > 0:
      e = discord.Embed(title=f"{member.display_name}さんのロール一覧 📒")
      v = "**@" + "**\n**@".join(rs) + "**"
      e.add_field(name=f"❖ ロール数 : {len(roles)}",value=v)
      es.append(e)
    e = es[page-1]
    e.set_author(name=f"To {ctx.author.display_name}",icon_url=ctx.author.avatar_url)
    return await ctx.send(embed=e)
    
  @member.command(aliases=["aces"])
  async def accessibles(self, ctx, page:int=1, member:discord.Member=None):
    if member == None: member = ctx.author
    ss, es, aces = [], [], []
    for ch in ctx.guild.text_channels:
      if member.id in [x.id for x in ch.members]:
        aces.append(ch.name)
    for a in aces:
      ss.append(a)
      if len(ss) == 10:
        e = discord.Embed(title=f"{member.display_name}さんの接続可能なチャンネル一覧 📒")
        v = "#" + "\n#".join(ss)
        e.add_field(name=f"❖ チャンネル数 : {len(aces)}",value=v)
        es.append(e)
        ss = []
    if len(ss) > 0:
      e = discord.Embed(title=f"{member.display_name}さんの接続可能なチャンネル一覧 📒")
      v = "#" + "\n#".join(ss)
      e.add_field(name=f"❖ チャンネル数 : {len(aces)}",value=v)
      es.append(e)
    e = es[page-1]
    e.set_author(name=f"To {ctx.author.display_name}",icon_url=ctx.author.avatar_url)
    return await ctx.send(embed=e)
    
  @member.command(aliases=["prms"])
  async def permissions(self, ctx, page:int=1, member:discord.Member=None):
    if member == None: member = ctx.author
    ps, es, perms = [], [], member.guild_permissions
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
    permst = list(filter(lambda x: x[1] == True, perms))
    permsm = list(map(lambda x: perms_dict[x[0]], permst))
    permss = list(sorted(permsm))
    for p in permss:
      ps.append(p)
      if len(ps) == 10:
        e = discord.Embed(title=f"{member.display_name}の所持する権限一覧 📒")
        v = "\n".join(ps)
        e.add_field(name=f"❖ 権限数 : {len(permss)}",value=v)
        es.append(e)
        ps = []
    if len(ps) > 0:
      e = discord.Embed(title=f"{member.display_name}の所持する権限一覧 📒")
      v = "\n".join(ps)
      e.add_field(name=f"❖ 権限数 : {len(permss)}",value=v)
      es.append(e)
    e = es[page-1]
    e.set_author(name=f"To {ctx.author.display_name}",icon_url=ctx.author.avatar_url)
    return await ctx.send(embed=e)
    
  @member.command(aliases=["chnk"])
  async def changenick(self, ctx, name, member:discord.Member=None):
    await ctx.message.edit(delete_after=5.0)
    if member == None:
      member = ctx.author
      if ('change_nickname', True) not in ctx.author.guild_permissions:
        return await ctx.send("ニックネームを変更する権限が無いようです",delete_after=5.0)
    else:
      if ('manage_nicknames', True) not in ctx.author.guild_permissions:
        return await ctx.send("ニックネームを変更する権限が無いようです",delete_after=5.0)
    before = member.display_name
    await member.edit(nick=name)
    return await ctx.send(f"{member.name} さんのニックネームを '{before}' から '{name}' に変更しました",delete_after=10.0)
    
  @member.command(aliases=["vcmt"])
  @commands.has_permissions(mute_members=True)
  async def vcmute(self, ctx, member:discord.Member):
    await ctx.message.edit(delete_after=5.0)
    await member.edit(mute=True)
    return await ctx.send(f"{member.display_name} さんをサーバーミュートしました",delete_after=10.0)
    
  @member.command(aliases=["vsmt"])
  @commands.has_permissions(deafen_members=True)
  async def vcspeakermute(self, ctx, member:discord.Member):
    await ctx.message.edit(delete_after=5.0)
    await member.edit(deafen=True)
    return await ctx.send(f"{member.display_name} さんのスピーカーをサーバーミュートしました",delete_after=10.0)
    
  @member.command(aliases=["vcmv"])
  @commands.has_permissions(move_members=True)
  async def vcmove(self, ctx, channel:discord.VoiceChannel, member:discord.Member):
    await ctx.message.edit(delete_after=5.0)
    await member.move_to(channel)
    return await ctx.send(f"{member.display_name} さんを {channel.name} に移動しました",delete_after=10.0)
   
  @member.command(aliases=["vumt"])
  @commands.has_permissions(mute_members=True)
  async def vcunmute(self, ctx, member:discord.Member):
    await ctx.message.edit(delete_after=5.0)
    await member.edit(mute=False)
    return await ctx.send(f"{member.display_name} さんのミュートを解除しました",delete_after=10.0)
    
  @member.command(aliases=["vusm"])
  @commands.has_permissions(deafen_members=True)
  async def vcunspeakermute(self, ctx, member:discord.Member):
    await ctx.message.edit(delete_after=5.0)
    await member.edit(deafen=False)
    return await ctx.send(f"{member.display_name} さんのスピーカーミュートを解除しました",delete_after=10.0)
   
  @member.command(aliases=["adrl"])
  @commands.has_permissions(manage_roles=True)
  async def addrole(self, ctx, role:discord.Role, member:discord.Member=None, reason=None):
    await ctx.message.edit(delete_after=5.0)
    if member == None: member = ctx.author
    if role.id in self.overroles:
      e = discord.Embed(title="⚠️ 高階・VIP・警告役職は別途コマンドを使用してください")
      e.add_field(name="💡 ヒント",value="以下のコマンドを使用しましょう！\n・`e:m warn`: 警告ロールを付与します\n・`e:m vip`: VIPロールを付与します\n・`e:m admin`: 高階ロールを付与します")
      e.set_author(name=f"To {ctx.author.display_name}",icon_url=ctx.author.avatar_url)
      return await ctx.send(embed=e,delete_after=5.0)
    await member.add_roles(role)
    return await ctx.send(f"{member.display_name} さんにロール '{role.name}' を付与しました",delete_after=10.0)
          
  @member.command(aliases=["rmrl"])
  @commands.has_permissions(manage_roles=True)
  async def removerole(self, ctx, role:discord.Role, member:discord.Member=None, reason=None):
    await ctx.message.edit(delete_after=5.0)
    if member == None: member = ctx.author
    if role.id in self.overroles:
      e = discord.Embed(title="⚠️ 高階・VIP・警告役職は別途コマンドを使用してください")
      e.add_field(name="💡 ヒント",value="以下のコマンドを使用しましょう！\n・`e:m unwarn`: 警告ロールを剥奪します\n・`e:m unvip`: VIPロールを剥奪します\n・`e:m unadmin`: 高階ロールを付与します")
      e.set_author(name=f"To {ctx.author.display_name}",icon_url=ctx.author.avatar_url)
      return await ctx.send(embed=e,delete_after=5.0)
    await member.remove_roles(role)
    return await ctx.send(f"{member.display_name} さんから役職 '{role.name}' を剥奪しました",delete_after=10.0)
          
  @member.command()
  @commands.has_permissions(manage_roles=True)
  async def mute(self, ctx, member:discord.Member, reason=None):
    await ctx.message.edit(delete_after=5.0)
    if 785137663123914763 in [x.id for x in member.roles]:
      return await ctx.send("⚠️ 既にミュート処分を受けているようですよ",delete_after=5.0)
    role = ctx.guild.get_role(785137663123914763)
    await member.add_roles(role)
    return await ctx.send(f"☑️ {member.display_name} さんに第5級処分 'ミュート' を行いました",delete_after=10.0)
    
  @member.command()
  @commands.has_permissions(manage_roles=True)
  async def warn(self, ctx, member:discord.Member, warninglevel:int, reason=None):
    await ctx.message.edit(delete_after=5.0)
    wns = self.overroles[1:5]
    wnr = ctx.guild.get_role(wns[warninglevel])
    trs = [x.id for x in member.roles]
    mrs = [x for x in trs if x in wns]
    if len(mrs) == 1:
      rmr = ctx.guild.get_role(mrs[0])
      if wnr.id == rmr:
        return await ctx.send("🚫 前回と同じ処分はできません！",delete_after=5.0)
      await member.remove_roles(rmr)
    await member.add_roles(wnr)
    wnl = [
      "第4級処分 '**初等注意**'",
      "第3級処分 '**一次警告**'",
      "第2級処分 '**二次警告**'",
      "第1級処分 '**三次警告**'"
    ]
    return await ctx.send(f"☑️ {member.display_name} さんに{wnl[warninglevel]} を行いました",delete_after=10.0)
    
  @member.command()
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, member:discord.Member, reason=None):
    await ctx.message.edit(delete_after=5.0)
    await member.kick(reason=reason)
    return await ctx.send(f"☑️ {member.display_name} さんに特級処分 '追放' を行いました",delete_after=10.0)
    
  @member.command()
  @commands.has_permissions(ban_members=True)
  async def ban(self, ctx, member:discord.Member, deletedays=0, reason=None):
    await ctx.message.edit(delete_after=5.0)
    await member.ban(reason=reason, delete_message_days=deletedays)
    return await ctx.send(f"☑️ {member.display_name} さんに特級処分 '永久追放' を行いました",delete_after=10.0)
    
  @member.command(aliases=["unmt"])
  @commands.has_permissions(manage_roles=True)
  async def unmute(self, ctx, member:discord.Member, reason=None):
    await ctx.message.edit(delete_after=5.0)
    if 785137663123914763 not in [x.id for x in member.roles]:
      return await ctx.send("⚠️ まだミュート処分を受けていないようですよ",delete_after=5.0)
    role = ctx.guild.get_role(785137663123914763)
    await member.remove_roles(role)
    return await ctx.send(f"☑️ {member.display_name} さんのミュート処分を解除しました",delete_after=10.0)
    
  @member.command(aliases=["unwn"])
  @commands.has_permissions(manage_roles=True)
  async def unwarn(self, ctx, member:discord.Member, reason=None):
    await ctx.message.edit(delete_after=5.0)
    rls = [x.id for x in member.roles]
    wns = [x for x in rls if x in self.overroles[1:5]]
    if len(wns) == 0:
      return await ctx.send("⚠️ まだ警告処分を受けていないようです",delete_after=5.0)
    role = ctx.guild.get_role(wns[0])
    await member.remove_roles(role)
    return await ctx.send(f"☑️ {member.display_name} さんの警告処分を解除しました",delete_after=10.0)
    
  @member.command(aliases=["unbn"])
  @commands.has_permissions(ban_members=True)
  async def unban(self, ctx, userid, reason=None):
    await ctx.message.edit(delete_after=5.0)
    user = await self.bot.fetch_user(userid)
    await ctx.guild.unban(user, reason=reason)
    return await ctx.send(f"☑️ {user.name} さんのBan処分を解除しました",delete_after=10.0)
    
  @member.command()
  @commands.has_permissions(manage_guild=True)
  async def vip(self, ctx, member:discord.Member, viplevel:int, reason=None):
    await ctx.message.edit(delete_after=5.0)
    vps = self.overroles[5:7]
    vrl = ctx.guild.get_role(vps[viplevel])
    rls = [x.id for x in member.roles]
    mrs = [x for x in rls if x in vps]
    vs = ["銀のVIP","金のVIP"]
    e = discord.Embed(title="⚠️ 認定前に確認します")
    e.add_field(name="認定内容",value=f"```\n{member.display_name} <-- {vs[viplevel]}\n```")
    e.set_author(name=f"To {ctx.author.display_name}",icon_url=ctx.author.avatar_url)
    e.set_footer(text="認定しますか？ Y or N")
    em = await ctx.send(embed=e)
    try:
      m = await self.bot.wait_for('message', timeout=20.0, check=lambda m: m.author == ctx.author and m.content in ["Y","N"])
      await em.edit(delete_after=1.0)
      await m.edit(delete_after=1.0)
      if m.content == "Y":
        if len(mrs) == 1:
          if mrs[0] == vrl.id:
            return await ctx.send("🚫 前回と同じ認定はできません！",delete_after=5.0)
          rmr = ctx.guild.get_role(mrs[0])
          await member.remove_roles(rmr)
        await member.add_roles(vrl)
        return await ctx.send(f"☑️ {member.display_name} さんを '{vs[viplevel]}' に認定しました！",delete_after=10.0)
      else:
        return await ctx.send("☑️ 認定を破棄しました",delete_after=5.0)
    except asyncio.TimeoutError:
      return await ctx.send("☑️ 20秒以内に応答がなかった為、認定を破棄しました",delete_after=5.0)
          
  @member.command(aliases=["admn"])
  @commands.has_permissions(administrator=True)
  async def admin(self, ctx, member:discord.Member, adminlevel:int, reason=None):
    await ctx.message.edit(delete_after=5.0)
    ads = self.overroles[7:9]
    arl = ctx.guild.get_role(ads[adminlevel])
    rls = [x.id for x in member.roles]
    mrs = [x for x in rls if x in ads]
    ads = ["権限者","管理者"]
    e = discord.Embed(title="⚠️ 任命前に確認します")
    e.add_field(name="任命内容",value=f"```\n{member.display_name} <-- {ads[adminlevel]}\n```")
    e.set_author(name=f"To {ctx.author.display_name}",icon_url=ctx.author.avatar_url)
    e.set_footer(text="任命しますか？ Y or N")
    em = await ctx.send(embed=e)
    try:
      m = await self.bot.wait_for('message', timeout=20.0, check=lambda m: m.author == ctx.author and m.content in ["Y","N"])
      await em.edit(delete_after=1.0)
      await m.edit(delete_after=1.0)
      if m.content == "Y":
        if len(mrs) == 1:
          if mrs[0] == arl.id:
            return await ctx.send("🚫 前回と同じ任命はできません！",delete_after=5.0)
          rmr = ctx.guild.get_role(mrs[0])
          await member.remove_roles(rmr)
        await member.add_roles(arl)
        return await ctx.send(f"☑️ {member.display_name} さんを '{ads[adminlevel]}' に任命しました！",delete_after=10.0)
      else:
        return await ctx.send("☑️ 任命を破棄しました",delete_after=5.0)
    except asyncio.TimeoutError:
      return await ctx.send("☑️ 20秒以内に応答がなかった為、認定を破棄しました",delete_after=5.0)
    
  @member.command(aliases=["uvip"])
  @commands.has_permissions(manage_guild=True)
  async def unvip(self, ctx, member:discord.Member, reason=None):
    await ctx.message.edit(delete_after=5.0)
    vps = self.overroles[5:7]
    rls = [x.id for x in member.roles]
    mrs = [x for x in rls if x in vps]
    e = discord.Embed(title="⚠️ 剥奪前に確認します")
    e.add_field(name="剥奪内容",value=f"```\n{member.display_name} --> VIP\n```")
    e.set_author(name=f"To {ctx.author.display_name}",icon_url=ctx.author.avatar_url)
    e.set_footer(text="剥奪しますか？ Y or N")
    em = await ctx.send(embed=e)
    try:
      m = await self.bot.wait_for('message', timeout=20.0, check=lambda m: m.author == ctx.author and m.content in ["Y","N"])
      await em.edit(delete_after=1.0)
      await m.edit(delete_after=1.0)
      if m.content == "Y":
        if len(mrs) == 0:
          return await ctx.send("🚫 VIPに認定されていないようです！",delete_after=5.0)
        rmr = ctx.guild.get_role(mrs[0])
        await member.remove_roles(rmr)
        return await ctx.send(f"☑️{member.display_name} さんから VIP権限 を剥奪しました",delete_after=10.0)
      else:
        return await ctx.send("☑️ 剥奪を破棄しました",delete_after=5.0)
    except asyncio.TimeoutError:
      return await ctx.send("☑️ 20秒以内に応答がなかった為、剥奪を破棄しました",delete_after=5.0)
    
  @member.command(aliases=["uadm"])
  @commands.has_permissions(administrator=True)
  async def unadmin(self, ctx, member:discord.Member, reason=None):
    await ctx.message.edit(delete_after=5.0)
    ads = self.overroles[7:9]
    rls = [x.id for x in member.roles]
    mrs = [x for x in rls if x in ads]
    e = discord.Embed(title="⚠️ 剥奪前に確認します")
    e.add_field(name="剥奪内容",value=f"```\n{member.display_name} --> 高階権限\n```")
    e.set_author(name=f"To {ctx.author.display_name}",icon_url=ctx.author.avatar_url)
    e.set_footer(text="剥奪しますか？ Y or N")
    em = await ctx.send(embed=e)
    try:
      m = await self.bot.wait_for('message', timeout=20.0, check=lambda m: m.author == ctx.author and m.content in ["Y","N"])
      await em.edit(delete_after=1.0)
      await m.edit(delete_after=1.0)
      if m.content == "Y":
        if len(mrs) == 0:
          return await ctx.send("🚫 権限者・管理者に任命されていないようです！",delete_after=5.0)
        rmr = ctx.guild.get_role(mrs[0])
        await member.remove_roles(rmr)
        return await ctx.send(f"☑️ {member.display_name} さんから 高階権限 を剥奪しました",delete_after=10.0)
      else:
        return await ctx.send("☑️ 認定を破棄しました",delete_after=5.0)
    except asyncio.TimeoutError:
      return await ctx.send("☑️ 20秒以内に応答がなかった為、認定を破棄しました",delete_after=5.0)         
          
def setup(bot):
  bot.add_cog(MemberSystem(bot))
