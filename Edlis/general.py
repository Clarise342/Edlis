#python 3.9.0
#coding: utf-8

import discord
from discord.ext import commands, tasks
from datetime import datetime

class GeneralSystem(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot
    self.bot.remove_command("help")
    self.startstime = datetime.now()
    self.vaid = 0
    self.activity.start()
    self.cl = {
      "er":0xFFC20E
    }
    
  @commands.command(aliases=["help","cmdl"])
  async def commandslist(self, ctx):
    cmds = [
      "help`(cmdl)`", "commandhelp`(cmdh)` {`コマンド名`} [`実装記号`]",
      "announce`(anus)` {`内容`}", "permissionslist`(prml)`",
      "member`(m)` {`コマンド`}", "guild`(g)` {`コマンド`}",
      "role`(r)` {`コマンド`}"
    ]
    cmds_f = "・" + "\n・".join(cmds)
    e = discord.Embed(title="Edlisのヘルプ ℹ️")
    e.add_field(name="★ 一般コマンド一覧",value=cmds_f)
    e.add_field(name="◇ 開発者",value="Clarice#0920`(536506865883021323)`")
    e.add_field(name="○ その他情報",value="`使用言語 :` Python\n`使用ライブラリ :` discord.py")
    e.add_field(name="⚠️ 導入について",value="`EdlisはEDS専用BOTの為、他のサーバーへの導入を許可していません`")
    e.set_author(name=f"To {ctx.author.display_name}",icon_url=ctx.author.avatar_url)
    e.set_footer(text="ヒント｜e:cmdhでコマンドの詳細を確認できます…")
    return await ctx.send(embed=e)
   
  @commands.command(aliases=["anuc"])
  @commands.has_any_role(770880174820163624, 711201258081615912, 723177654362177586)
  async def announce(self, ctx, value):
    await ctx.message.edit(delete_after=1.0)
    e = discord.Embed(title=value)
    e.set_author(name=f"📢 {ctx.author.display_name}よりアナウンス！")
    e.set_thumbnail(url=ctx.author.avatar_url)
    ch = ctx.guild.get_channel(716137636296654889)
    await ch.send(embed=e)
    
  @commands.command(aliases=["prml"])
  async def permissionslist(self, ctx, page:int=1):
    pl = {
      "28": "`リアクションを追加`(○テ)",
      "00": "`管理者`(△ー)",
      "26": "`ファイルを添付`(○テ)",
      "11": "`メンバーをBAN`(△ー)",
      "18": "`ニックネームを変更`(△ー)",
      "30": "`ボイスチャンネルに接続`(○ボ)",
      "19": "`招待を作成`(○全)",
      '14': "`メンバーをスピーカーミュート`(○ボ)",
      "27": "`埋め込みリンク`(○テ)",
      '29': "`外部の絵文字を使用`(○テ)",
      '12': "`メンバーをKick`(△ー)",
      "04": "`チャンネルを管理`(○全)",
      '06': "`絵文字を管理`(△ー)",
      '01': "`サーバーを管理`(△ー)",
      '05': "`メッセージを管理`(○テ)",
      '07': "`ニックネームを管理`(△ー)",
      '03': "`権限を管理`(▽全)",
      '02': "`役職を管理`(△ー)",
      '08': "`ウェブフックを管理`(○テ)",
      '17': "`@everyoneにメンション`(○テ)",
      '15': "`メンバーを移動`(○ボ)",
      '13': "`メンバーをミュート`(○ボ)",
      '16': "`優先スピーカー`(○ボ)",
      '22': "`メッセージ履歴を読む`(○テ)",
      '21': "`メッセージを読む`(○テ)",
      '23': "`メッセージを送信`(○テ)",
      '24': "`TTSメッセージを送信`(○テ)",
      '25': "`スラッシュコマンドを使用`(○テ)",
      '31': "`ボイスチャンネルで発言`(○ボ)",
      '32': "`ボイスチャンネルで配信`(○ボ)",
      '28': "`外部の絵文字を使用`(○テ)",
      '33': "`音声検出を使用`(○ボ)",
      '09': "`監査ログを表示`(△ー)",
      '20': "`チャンネルを見る`(○全)",
      '10': "`サーバーインサイトを見る`(△ー)",
      '34': "`リクエストトゥスピーク`(▽ス)"
    }
    psl, el, e = sorted(pl), [], discord.Embed(title=f"権限と指定値(権限値)のリスト (全 {len(pl)} 種)")
    for l in psl:
      e.add_field(name=l, value=pl[l], inline=False)
      if len(e.fields) == 8:
        e.add_field(name="注釈",value="○:ロールとチャンネルに適用可\n"
                    "△:ロールにのみ適用可\n"
                    "▽:チャンネルにのみ適用可\n"
                    "テ:テキストチャンネルに適用可\n"
                    "ボ:ボイスチャンネルに適用可\n"
                    "全:どちらのチャンネルでも適用可\n"
                    "ス:ステージチャンネルに適用可")
        e.set_footer(text=f"権限値は権限を付与・剥奪する際に使用します\n現在表示しているページは {len(el)+1} ページです")
        e.set_author(name=f"To {ctx.author.display_name}",icon_url=ctx.author.avatar_url)
        el.append(e)
        e = discord.Embed(title=f"権限と指定値(権限値)のリスト (全 {len(pl)} 種)")
    if len(el) * 8 < len(psl):
      e.add_field(name="注釈",value="○:ロールとチャンネルに適用可\n"
                    "△:ロールにのみ適用可\n"
                    "▽:チャンネルにのみ適用可\n"
                    "テ:テキストチャンネルに適用可\n"
                    "ボ:ボイスチャンネルに適用可\n"
                    "全:どちらのチャンネルでも適用可\n"
                    "ス:ステージチャンネルに適用可")
      e.set_footer(text=f"権限値は権限を付与・剥奪する際に使用します\n現在表示しているページは {len(el)+1} ページです")
      e.set_author(name=f"To {ctx.author.display_name}",icon_url=ctx.author.avatar_url)
      el.append(e)
    return await ctx.send(embed=el[page-1])
      
    
  @tasks.loop(seconds=60)
  async def activity(self):
    lt = self.bot.latency
    if lt == float("inf"):
      val = "Edlisです！ - 現在のBOTレイテンシは ???ms です"
    else:
      val = f"Edlisです！ - 現在のBOTレイテンシは {round(self.bot.latency*1000)}ms です"
    msgs = [
      f"Edlisです！ - c:help(cmdlで簡略) でコマンド一覧を確認できますよ！",
      f"Edlisです！ - 現在開発中です！(連絡は Clarice まで…)",
      val
    ]
    await self.bot.change_presence(activity=discord.Game(msgs[self.vaid], start=self.startstime))
    if self.vaid < 2:
      self.vaid += 1
    else:
      self.vaid = 0
      
  @activity.before_loop
  async def before_activity(self):
    await self.bot.wait_until_ready()
    
  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):
    await ctx.message.edit(delete_after=5.0)
    e, te = None, type(error)
    if te == discord.ext.commands.CommandNotFound:
      e = discord.Embed(title="⚠️ コマンド名に誤りがあるようです",color=self.cl["er"])
      e.add_field(name="💡 ヒント",value="`e:help`や`e:{c} cmdh`を確認しましょう！")
      
    elif te == discord.ext.commands.MemberNotFound:
      e = discord.Embed(title="⚠️ メンバーが見つかりませんでした",color=self.cl["er"])
      e.add_field(name="💡 ヒント",value="メンバー名やIDを再確認しましょう！")
      
    elif te == discord.ext.commands.ChannelNotFound:
      e = discord.Embed(title="⚠️ チャンネルが見つかりませんでした",color=self.cl["er"])
      e.add_field(name="💡 ヒント",value="チャンネル名やIDを再確認しましょう！")
      
    elif te == discord.ext.commands.RoleNotFound:
      e = discord.Embed(title="⚠️ ロールが見つかりませんでした",color=self.cl["er"])
      e.add_field(name="💡 ヒント",value="ロール名やIDを再確認しましょう！")
      
    elif te == discord.ext.commands.TooManyArguments:
      e = discord.Embed(title="⚠️ 必要以上に要素を与えられたようです",color=self.cl["er"])
      e.add_field(name="💡 ヒント",value="`e:help`や`e:{c} cmdh`を確認しましょう！")
      
    elif te == discord.ext.commands.MissingRequiredArgument:
      e = discord.Embed(title="⚠️ 要素が不足しているようです",color=self.cl["er"])
      e.add_field(name="💡 ヒント",value="`e:help`や`e:{c} cmdh`を確認しましょう！")
    
    elif te == discord.ext.commands.MissingPermissions:
      e = discord.Embed(title="⚠️ あなたの権限が不足しているようです",color=self.cl["er"])
      prms = "・" + "\n・".join(te.missing_perms)
      e.add_field(name="不足している権限",value=prms)
      e.add_field(name="💡 ヒント",value="あなたの持つ権限を確認しましょう\n誰かに代行してもらうのも手ですよ！")
    
    elif te == discord.ext.commands.errors.MissingAnyRole:
      e = discord.Embed(title="⚠️ 特定のロールを所持していないようです",color=self.cl["er"])
      try: r = "・@" + "\n・@".join([ctx.guild.get_role(x).name for x in error.missing_roles])
      except: r = "\n".join([str(x) for x in error.missing_roles])
      e.add_field(name="要求されたロール*¹",value=r)
      e.add_field(name="💡 ヒント",value="あなたの持つロールを確認しましょう\n誰かに代行してもらうのも手ですよ！")
      e.set_footer(text="*1 要求されたロールの内、1つ以上を所持していればよい")
    
    elif te == discord.ext.commands.CommandInvokeError:
      to = type(error.original)
      if to == IndexError:
        e = discord.Embed(title="⚠️ そのページは存在していないようです",color=self.cl["er"])
        e.add_field(name="💡 ヒント",value="`e:commandhelp`でページ数を確認しましょう\n分からない場合はページを指定せずに実行しましょう！")
    
      if to == discord.errors.Forbidden:
        et = error.original.text
        if et == "Missing Permissions":
          e = discord.Embed(title="⚠️ Edlisの権限が不足しているようです",color=self.cl["er"])
          e.add_field(name="💡 ヒント",value="Edlisの権限を確認してください\nまた、Edlis以上の権限を持つメンバーを対象に実行することが不可能な場合があります")
    
    if e != None:
      e.set_author(name=f"To {ctx.author.display_name} (Error)",icon_url=ctx.author.avatar_url)
      await ctx.send(embed=e,delete_after=10.0)
    else:
      await ctx.send("エラーが発生したみたいですよ！",delete_after=5.0)
      print("\n" + str(type(error)).strip("<class ''>"))
      print(error.args[0])
    ch = self.bot.get_channel(819785085649682452)
    return await ch.send(f"{datetime.now().strftime('%Y年%m月%d日 %H時%M分%S秒')}\n`発生サーバー`: {ctx.guild.name}\n`発生チャンネル`: {ctx.channel.name}\n`メッセージ`: {ctx.message.content}")
    
    
def setup(bot):
  bot.add_cog(GeneralSystem(bot))
