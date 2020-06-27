#coding:UTF-8
import discord
from discord.ext import tasks
from datetime import datetime 

TOKEN = "NzI2NDE0NjY5Nzg2NjQ0NDkw.Xvc9Qw.31Vd8SPzhnAv70gG1KWZDQ93UWs" #トークン
CHANNEL_ID = 704288269998751854 #チャンネルID
# 接続に必要なオブジェクトを生成
client = discord.Client()

# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    if now == '23:11':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('おはよう')  

#ループ処理実行
loop.start()
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
