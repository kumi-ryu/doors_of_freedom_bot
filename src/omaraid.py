#coding:UTF-8
import discord
import configparser
from discord.ext import tasks
from datetime import datetime 

# コンフィグファイルの読み込み
inifile = configparser.ConfigParser()
inifile.read('./config.ini', 'UTF-8')
token = inifile.get('settings', 'token')
channel_id = 809021475422994532

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    if now == '00:00' or now == '6:00' or now == '12:00' or now == '18:00':
        channel = client.get_channel(channel_id)
        await channel.send('!oma raid')  

#ループ処理実行
loop.start()
# Botの起動とDiscordサーバーへの接続
client.run(token)