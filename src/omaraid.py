#coding:UTF-8
import discord
import configparser
import json
import requests
from discord.ext import tasks
from datetime import datetime 

# コンフィグファイルの読み込み
inifile = configparser.ConfigParser()
inifile.read('./config.ini', 'UTF-8')
TOKEN = inifile.get('settings', 'token')
SPRED_URL = inifile.get('settings', 'sheet_url_elph')
CHANNEL_ID = int(inifile.get('settings', 'channel_id'))

# 接続に必要なオブジェクトを生成
client = discord.Client()

# スプレッドシート情報をget
response = requests.get(SPRED_URL)

# 任意のチャンネルで挨拶する非同期関数を定義
async def greet():
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('おまらいど　起動しました！')

# bot起動時に実行されるイベントハンドラを定義
@client.event
async def on_ready():
    await greet() # 挨拶する非同期関数を実行

client.run(TOKEN)