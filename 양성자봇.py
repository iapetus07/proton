import discord
import asyncio
import os

client = discord.Client()

token = access_token

@client.event
async def on_ready():

    print(client.user.name)
    print('봇 시작됨')
    game = discord.Game("정무경의 뇌속에 있는 아이디어를 실현하는 중")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content == "!무경":
        await message.channel.send("저를 창조하신 천재적이시고 대단한 분이세요.")
    if message.content == "!무경이 지적수준":
        await message.channel.send("알버트 아인슈타인 이후의 최고의 지적수준을 가지고 계세요.")
    if message.content == "!흐음 양성자가 뭐지?":
        await message.channel.send("양성자, 영어로는 proton 이라고 해요. 중성자와 함께 원자핵을 구성하는 입자이며, 양의 전하를 가지고 있어요. 양성자의 전하량은 전자의 전하량과 비교했을 때 그 크기는 같으나 부호는 반대이고, 전자 질량의 약 1836배에 해당하는 질량을 지닌 입자에요.")
    if message.content == "!너 친구는?":
        await message.channel.send("중성자 봇입니다.(아직 만들지 않았습니다. 추후 추가될 예정)")
    if message.content == "!한":
        await message.channel.send("나영")
    if message.content == "!정보 무경":
        await message.channel.send("엄청난 천재 / 2008.08.26 생 그의 따까리로는 김기태를 두고 있다.")
    if message.content == "!무경이 장비":
        await message.channel.send("키보드 : 앱코 k8000, 마우스 : 레이저 VIPER ")
    if message.content == "!무경이 임베드":
        embed = discord.Embed(title="정무경", description="엄청난 천재", color=0x00ff00)
        embed.set_thumbnail(url="https://photos.google.com/photo/AF1QipO2ThSR2ckrU9m5yFtLyufRKBk1HvSqTflAPKkl")
        embed.set_footer(text="기본정보 : 2008.08.26생")
        await message.channel.send(embed=embed)
    if message.content == "!명령어":
        embed = discord.Embed(title="아래가 현재 사용가능한 명령어 목록입니다.", description="!를 치시고 사용하시길 바랍니다.-  무경, 무경이 지적수준, 흐음 양성자가 뭐지?, 너 친구는?, 정보 무경, 무경이 장비, 무경이 임베드")
        await message.channel.send(embed=embed) 
    if message.content == "!MGLD 임베드":
        embed = discord.Embed(title="MGLD", description="정무경과 신주원이 만든 크루")
        embed.set_thumbnail(url="https://photos.google.com/photo/AF1QipOAwbwl6mpkkUyQVYaCP2LK7KXMQFUkIEvtnOKE")
        await message.channel.send(embed=embed) 

access_token = os.environ["BOT_TOKEN"]     
client.run(token)
