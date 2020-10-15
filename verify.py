import discord
from discord.ext import commands
import os
import asyncio
import random
import urllib
from captcha.image import ImageCaptcha
from bs4 import BeautifulSoup
from urllib.request import Request
from urllib import parse
import bs4
import time
import 


client = discord.Client()

@client.event
async def on_ready():
    print('봇이 로그인 하였습니다.')
    print(' ')
    print('닉네임 : {}'.format(client.user.name))
    print('아이디 : {}'.format(client.user.id))

@client.event
async def on_ready():
    print('봇이 로그인 하였습니다.')
    print(' ')
    print('닉네임 : {}'.format(client.user.name))
    print('아이디 : {}'.format(client.user.id))
    while True:
        user = len(client.users)
        server = len(client.guilds)
        messages = ["인증 하는법 : .인증 ", "현재 봇 상태 : 1단계 [ 관리자 수시 점검 ] " , " 봇에 에러가 날 시 저희가 다 책임집니다 ! " , str(user) + "분이  인증을 완료하심 ", str(server) + "분이 인증을 끝 까지 못 하심."]
        for (m) in range(5):
            await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(name=messages[(m)], type=discord.ActivityType.watching))
            await asyncio.sleep(4)
 
    if message.content == ".인증":
        Image_captcha = ImageCaptcha()
        msg = ""
        a = ""
        for i in range(6):
            a += str(random.randint(0, 9))

        name = "Captcha.png"
        Image_captcha.write(a, name)

        await message.channel.send(file=discord.File(name))
        embed = discord.Embed(title=" 고객님 안녕하세요 ! 🎈 ", description = message.author.mention + ", 위에 있는 인증코드를 10초내에 입력해주세요. 아 규칙은 꼭 확인 하셨겠죠?", timestamp=message.created_at,
        colour=discord.Colour.blurple()
    )
        embed.set_footer(text="WELCOME TO QNT ", icon_url="https://media.discordapp.net/attachments/766098691962437672/766099536694345738/QNT.png?width=833&height=469")
        await message.channel.send(embed=embed)

        def check(msg):
            return msg.author == message.author and msg.channel == message.channel

        try:
            msg = await client.wait_for("message", timeout=10, check=check)
        except:
            embed = discord.Embed(title="으아 아쉬워요  !", description = message.author.mention + " 인증시간을 초과하셨어요. 아쉽네요 :( ", timestamp=message.created_at,
            colour=discord.Colour.orange()
    )
            embed.set_footer(text="인증초과로 실패 😫", icon_url="https://media.discordapp.net/attachments/766098691962437672/766099536694345738/QNT.png?width=833&height=469")
            await message.channel.send(embed=embed)

        if msg.content == a:
            embed = discord.Embed(title="성공 하셨습니다 !", description = message.author.mention + " 캡챠코드를 정확하게 입력하셨네요 하지만 여기서 인증이 끝이 아닙니다 채널이 더 생겼을거예요 확인해보시겠어요 ? ", timestamp=message.created_at,
            colour=discord.Colour.green()
    )
            embed.set_footer(text="✅", icon_url="https://media.discordapp.net/attachments/766098691962437672/766099536694345738/QNT.png?width=833&height=469")
            await message.channel.send(embed=embed)
            role = discord.utils.get(message.author.guild.roles, name='USER')
            await message.author.add_roles(role)
        
        else:
            embed = discord.Embed(title=" 아쉽지만 틀리셨어요 ", description = message.author.mention + ",코드에 문제가 없는지 다시 확인해봐요 !! ", timestamp=message.created_at,
            colour=discord.Colour.red()
    )
            embed.set_footer(text="Space BOT#2204", icon_url="https://media.discordapp.net/attachments/766098691962437672/766099536694345738/QNT.png?width=833&height=469")
            await message.channel.send(embed=embed)
            
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
