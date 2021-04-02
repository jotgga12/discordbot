import discord
import asyncio
from random import *
import time
import os

client=discord.Client()

token='ODIyNzI4NDQ4NTMwNDQ4NDA2.YFWfkw.h3iFTduPnhOvqiILellIUGfB6LE'


@client.event
async def on_ready():
    print(client.user.name)
    print('봇 작동중')
    game=discord.Game('!명령어 ')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    
    
    if message.content=="!눕스틱":
        await message.channel.send("단백질")
    if message.content=="!오늘뭐먹지":
        eat=randint(1,10)
        if eat==1:
            await message.channel.send("돈까스")
        elif eat==2:
            await message.channel.send("한식")
        elif eat==3:
            await message.channel.send("사료")
        elif eat==4:
            await message.channel.send("떡볶이")
        elif eat==5:
            await message.channel.send("라면")
        elif eat==6:
            await message.channel.send("짜장면")
        elif eat==7:
            await message.channel.send("우동")
        elif eat==8:
            await message.channel.send("쌀국수")
        elif eat==9:
            await message.channel.send("삼겹살")
        elif eat==10:
            await message.channel.send("샌드위치")

    if message.content=="!디스코드":
        await message.channel.send("https://discord.gg/e4H5uE2uKa")
    
        #대화
    if message.content=="곰탱아 안녕":
        await message.channel.send("ㅇ")
    if message.content=="곰탱아 ㅎㅇ":
        await message.channel.send("ㅇ")
    if message.content=="곰탱아 하이":
        await message.channel.send("ㅇ")
    if message.content=="곰탱아":
        await message.channel.send("뭐")
    if message.content=="곰탱아 뭐해":
        await message.channel.send("너 죽이는 생각해")
        time.sleep(0.9)
        await message.channel.send("ㅇㅇ")
    if message.content=="곰탱아 뭐해?":
        await message.channel.send("너 죽이는 생각해")
        time.sleep(0.9)
        await message.channel.send("ㅇㅇ")
    if message.content=="곰탱아 뭐함":
        await message.channel.send("너 죽이는 생각해")
        time.sleep(0.9)
        await message.channel.send("ㅇㅇ")
    if message.content=="곰탱아 뭐함?":
        await message.channel.send("너 죽이는 생각해")
        time.sleep(0.9)
        await message.channel.send("ㅇㅇ")
    if message.content=="곰탱아 머해":
        await message.channel.send("너 죽이는 생각해")
        time.sleep(0.9)
        await message.channel.send("ㅇㅇ")
    if message.content=="곰탱아 머해?":
        await message.channel.send("너 죽이는 생각해")
        time.sleep(0.9)
        await message.channel.send("ㅇㅇ")
    if message.content=="곰탱아 머함":
        await message.channel.send("너 죽이는 생각해")
        time.sleep(0.9)
        await message.channel.send("ㅇㅇ")
    if message.content=="곰탱아 머함?":
        await message.channel.send("너 죽이는 생각해")
        time.sleep(0.9)
        await message.channel.send("ㅇㅇ")
    if message.content=="곰탱아 사랑해":
        await message.channel.send("아 시발 역겨워 ㄲㅈ")

    if message.content=="곰탱아 욕해줘":
        await message.channel.send("ㅇ")
    
    if message.content=="곰탱아 나가":
        await message.channel.send("니가 나가")
    if message.content=="곰탱아 살려줘":
        await message.channel.send("?")
    if message.content=="곰탱아 꺼져":
        await message.channel.send("싫어 ")
   
            #대화 끝
    if message.content=="!초대하기":
        await message.channel.send("https://discord.com/oauth2/authorize?client_id=822728448530448406&permissions=3533904&scope=bot")
            
    if message.content=="!공식 서버":
        await message.channel.send("https://discord.gg/G779thjFrr")

    if message.content=="!러시안룰렛":
        rusia=randInt(1,2)
        await message.channel.send("러시안룰렛은 2분의1의 확률로 죽습니다 (베타)")

        if rusia==1:
            await message.channel.send("이걸 살았네")
        elif rusia==2:
            await message.channel.send("쥬금")

    if message.content=="!카운트다운 10":
        for i in range(1,11):
            await message.channel.send(i)
            time.sleep(1)
        await message.channel.send("끝")
    if message.content=="!카운트다운 5":
        for i in range(1,6):
            await message.channel.send(i)
            time.sleep(1)
        await message.channel.send("끝")

    if message.content=="!카운트다운 3":
        for i in range(1,4):
            await message.channel.send(i)
            time.sleep(1)
        await message.channel.send("끝")

    if message.content=="!카운트다운 100":
        for i in range(1,101):
            await message.channel.send(i)
            time.sleep(1)
        await message.channel.send("끝")

    if message.content=="!유튜브 더커":
        await message.channel.send("https://www.youtube.com/channel/UCOOGthjpdiBWycXPEk4Oarg")
    if message.content=="!유튜브 눕스틱":
        await message.channel.send("https://www.youtube.com/channel/UCoyaWaRPYKDvsQhN6Zh6I7Q")
    if message.content=="!유튜브 완깎귤":
        await message.channel.send("https://www.youtube.com/channel/UCeTKm1iAkgGj4lSQI7Oa9SA")
    if message.content=="!유튜브 블루자드":
        await message.channel.send("https://www.youtube.com/channel/UCN3Un8T8awA9MwxLoX5JyLQ") 
    if message.content=="!유튜브 갓수필":
        await message.channel.send("https://www.youtube.com/channel/UCpToKkt-RFVUhXdbRYvXrSA") 
    if message.content=="!유튜브 구름띠":
        await message.channel.send("https://www.youtube.com/channel/UCaDErDvioDEPxXp7oO7uksA") 
    if message.content=="!유튜브 도끼소년":
        await message.channel.send("https://www.youtube.com/channel/UCh-0oZjHR_M59_fA2a8CIqg") 
    if message.content=="!유튜브 톰킴":
        await message.channel.send("https://www.youtube.com/channel/UCYzTBq90larZ-veM5OJTZuw") 
    if message.content=="!유튜브 멍충오리":
        await message.channel.send("https://www.youtube.com/channel/UCmiHK1_s8kMol_0RUNYO1hA") 
    if message.content=="!유튜브 자라":
        await message.channel.send("https://www.youtube.com/channel/UCPPE1HjjzvUbYwIql7zla_w")

    if message.content=="!명령어":
        await message.channel.send("안녕하세요! 곰탱이봇은 현재 베타버전의 봇입니다")
        time.sleep(1)
        await message.channel.send("기본적인 명령어로는 !카운트다운 3,5,10,100")
        time.sleep(1)
        await message.channel.send("!러시안룰렛 이라는 기능,")
        time.sleep(1)
        await message.channel.send("!유튜브 {유튜버 이름}")
        time.sleep(0.3)
        await message.channel.send("유효한 유튜버: 더커, 눕스틱, 완깎귤, 블루자드, 갓수필, 구름띠, 도끼소년, 톰킴, 멍충오리, 자라")
        time.sleep(4)
        await message.channel.send("!오늘뭐먹지 (뭐먹을지 고민될때)")
        time.sleep(1)
        await message.channel.send("곰탱아 ~~ 라는 대화기능이 있지만 현재 베타버전으로 많이 못알아듣습니다 (유효한말: 뭐해, 나가, 꺼져, 욕해줘, ㅎㅇ, 사랑해)")
        time.sleep(1)
        await message.channel.send("곰탱이봇은 수요일 매일, 화,목 잠깐 켜집니다")
        time.sleep(1)
        await message.channel.send("이상 곰탱이봇이였습니다 감사합니다")

access_token=os.environ["BOT_TOKEN"]

client.run(access_token)

