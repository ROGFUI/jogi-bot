Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import discord
>>> import asyncio
>>> 
>>> client = discord.Client()
>>> 
>>> @client.event
async def on_ready(): 
    print("디스코드 봇 로그인이 완료되었습니다.")
    print("디스코드봇 이름:" + client.user.name)
    print("디스코드봇 ID:" + str(client.user.id))
    print("디스코드봇 버전:" + str(discord.__version__))
    print('------')
    await client.change_presence(status=discord.Status.online, activity=discord.Game("로그가 개발자"))

    
>>> @client.event
async def on_message(message): 
    content = message.content 
    guild = message.guild 
    author = message.author 
    channel = message.channel 
    if content.startswith("!조기 온라인"): 
        await message.channel.send("온라인인지 오프라인인지 어케암 ㅋ") 
    if content == "!조기 하픽ping": 
        await message.channel.send("L!")
    if content == "!조기 노갈": 
        await message.channel.send("아폴로급인성!")
    if content == "!조기 로그": 
        await message.channel.send("개멍청이")
    if content == "!조기오프라인": 
        await message.channel.send("걍 보면될것이지")
    if content == "!조기 미스터 조": 
        await message.channel.send("아폴로의 인성 + 노갈!")
    if content == "!조기 배드워즈 팁": 
        await message.channel.send("걍 꼴아박아!")

        
>>> client.run('ODc0NTMzMTEwMTkxMDk5OTQ0.YRIWbQ.Ole_eFC3vD_F5o7-sBwIgBqEVE8')
디스코드 봇 로그인이 완료되었습니다.
디스코드봇 이름:조기봇
디스코드봇 ID:874533110191099944
디스코드봇 버전:1.7.3
------
