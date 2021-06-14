import discord 

import asyncio

from discord.utils import get

from discord.ext import tasks

import datetime

import time

import random



token = 'token'

client = discord.Client()


@client.event

async def on_ready():

    print(f'{client.user.name}')

    print(f'{client.user.id}')

    print(f"Token : {token}")

    print("Login Success")





@client.event

async def on_message(message):

    if message.content == '!비약':

        await message.channel.send('https://maple.loona.world/')
  

    if message.content == '!얍':
        ch = client.get_channel(827593227770003487)
        commander = discord.utils.get(message.guild.roles, name="초심")
        await ch.send("{} 모두 여기 봐주세여~!<@{}> 님이 할말 있대여~!".format(commander.mention,message.author.id))
     
    
    if message.content == '!7':
        ch = client.get_channel(827593227770003487)
        commander = discord.utils.get(message.guild.roles, name="초심")
        await ch.send("{} 여러분 7시 플래그 준비하세여~!".format(commander.mention))

    
    if message.content == '!9':
        ch = client.get_channel(827593227770003487)
        commander = discord.utils.get(message.guild.roles, name="초심")
        await ch.send("{} 여러분 9시 플래그 준비하세여~!".format(commander.mention))

    if message.content == '!수로':
        ch = client.get_channel(827593227770003487)
        commander = discord.utils.get(message.guild.roles, name="초심")
        await ch.send("{} 수로 시작 전입니다 길드 관리본부에 모두 모여주세여~!".format(commander.mention))
    

    
    if message.content == '!우르스':
        ch = client.get_channel(827593227770003487)
        commander = discord.utils.get(message.guild.roles, name="초심")
        await ch.send("{} 8시30분 우르스 17채에서 만나여~!".format(commander.mention))

    if message.content == '!12':
        ch = client.get_channel(827593227770003487)
        commander = discord.utils.get(message.guild.roles, name="초심")
        await ch.send("{} 여러분 12시 플래그 준비하세여~!".format(commander.mention))    


    if message.content == '!마무리':
        ch = client.get_channel(827593227770003487)
        commander = discord.utils.get(message.guild.roles, name="초심")
        await ch.send("{} 일퀘, 일보, 황금마차, 몬파, 와르, 데일리기프트, 유니온코인, 유니온 가드닝, 마일리지, 기보, 메M 확인하세여~!".format(commander.mention))     


    
    if message.content == "!안녕":
            channel = message.channel

            msg = "<@{}> 안녕!".format(message.author.id)
            await channel.send(msg)
            return None
 
    
    if message.content == '!소개':

        await message.channel.send('안녕! 초심의 마스코트! 초심이~~~ 등장!')


    if message.content == '!사냥터':

        await message.channel.send('https://cdn.discordapp.com/attachments/827593352983478282/838700610969927710/unknown.png')


    if message.content == '!몬라조합':

        await message.channel.send('https://selflog.tistory.com/358')

    if message.content == '!시드':

        await message.channel.send('https://m.inven.co.kr/board/maple/2304/19954')
    

    if message.content == '!몬라농장':

        await message.channel.send('https://meso.kr/')

    if message.content == '!수요일':
        ch = client.get_channel(827593227770003487)
        await ch.send('오늘은 수요일 주간보스 랑 결정석 다 파셨는지 확인 하세여~!')    

    if message.content == '!점검':
        ch = client.get_channel(840261015349755904)
        await ch.send('초심이는 잠깐 자고 올께여~!')
        await ch.send('https://cdn.discordapp.com/attachments/837463787954241598/844253577785376768/78550e75-722a-47c8-933c-fb0fa3682feb.png')
    
    
    if message.content == '!점검끝':
        ch = client.get_channel(840261015349755904)
        await ch.send('초심이 일어 났어여~!')
        await ch.send('https://cdn.discordapp.com/attachments/837463787954241598/844340373270036510/1621132083091.jpg')
    


    if message.content == '!추옵':

        await message.channel.send('http://www.inven.co.kr/board/maple/2304/13744')

    if message.content == '!심볼':

        await message.channel.send('https://maplecal.com/symbol')    

    if message.content == '!초심아 노래해줘':

        await message.channel.send('라라라 랄 랄 라~ 라라라 랄 랄 라~')

    
    

    if message.content == '!몬라':

        await message.channel.send('https://docs.google.com/document/d/1oTXkCl0KUzDgcIoDP48B_ObFNPJo5yaq2o3NeSQCyA0/edit')    

    if message.content == '!무토':

        await message.channel.send('https://cdn.discordapp.com/attachments/837463787954241598/841993517588414474/1620817275567-0.jpg')
        await message.channel.send('https://cdn.discordapp.com/attachments/837463787954241598/841993517903511592/1620817275567-1.jpg')

    if message.content == '!코강':

        await message.channel.send('전직업 코강 정리 : http://www.inven.co.kr/board/maple/2304/26224')

        await message.channel.send('코강 영상 : https://www.youtube.com/watch?v=pMepdAZP_a4&t=3s')


    if message.content == '!결정석':

        await message.channel.send('https://cdn.discordapp.com/attachments/827593352983478282/837357051868086312/i14976412404.png')


    if message.content == '!기여도':

        await message.channel.send('https://cdn.discordapp.com/attachments/838773797909299221/838774591974801458/ECBAA1ECB298SSS.png')


    if message.content == '!도핑':

        await message.channel.send('https://cdn.discordapp.com/attachments/838773797909299221/838774419101974568/i15732639533.png')


    if message.content == '!주흔피버': 

        await message.channel.send('https://cdn.discordapp.com/attachments/838773797909299221/838774298616397884/9cc459aa73bcadcb.png')
    

    if message.content == '!경뿌':

        await message.channel.send('https://cdn.discordapp.com/attachments/838773797909299221/838774215644545042/08a957b81b551154.png')


    if message.content == '!도움말':

        embed = discord.Embed(title = '!도움말', description = '꿀팁 명령어를 알려 드려여~!', colour = 0xA30FE2)
        

        embed.add_field(name = '!사냥터', value = '유니온에 유용한 사냥터 꿀팁을 알려 드려여~!', inline=False)


        embed.add_field(name = '!비약', value = '비약 계산기 링크를 알려 드려여~!', inline=False)


        embed.add_field(name = '!기여도', value = '보스를 통해 얻는 길드 기여도를 알려 드려여~!', inline=False)


        embed.add_field(name = '!몬라조합', value = '몬스터 라이프 조합을 알려 드려여~!', inline=False)


        embed.add_field(name = '!코강', value = '코강관련 정보를 알려 드려여~!', inline=False)


        embed.add_field(name = '!결정석', value = '보스의 결정석 가격을 알려 드려여~!', inline=False)


        embed.add_field(name = '!도핑', value = '무릉도장과 보스를 위한 도핑을 알려 드려여~!', inline=False)


        embed.add_field(name = '!주흔피버', value = '일요일 주흔 피버시 확률을 알려 드려여~!', inline=False)


        embed.add_field(name = '!경뿌', value = '사냥할때 챙길 경험치 도핑을 알려 드려여~!', inline=False)

        embed.add_field(name = '!도박', value = '가야할지 멈춰야 할지 알려 드려여~!', inline=False)

        embed.add_field(name = '!얍', value = '모두를 부를수 있어여~!', inline=False)

        embed.add_field(name = '!몬라', value = '몬스터 라이프의 공략을 알려 드려여~!', inline=False)

        embed.add_field(name = '!무토', value = '무토의 레시피를 알려 드려여~!', inline=False)

        embed.add_field(name = '!몬라농장', value = '몬스터가 있는 농장 검색기를 알려 드려여~!', inline=False)

        embed.add_field(name = '!추옵', value = '무기의 추옵을 알려 드려여~!', inline=False)

        embed.add_field(name = '!시드', value = '더시드의 꿀팀을 알려 드려여~!', inline=False)

        embed.add_field(name = '!심볼', value = '심볼계산기를 알려 드려여~!', inline=False)

        await message.channel.send(embed = embed)


    if message.content == '!진화':
        ch = client.get_channel(840261015349755904)
        embed = discord.Embed(title = '초심이 업데이트', description = '!시드, !심볼 명령어가 추가되었어여! 도움말을 확인해 주세여~!', colour = 0xA30FE2)
        
        embed.add_field(name = '초심이 오류 수정', value = '완벽한 초심이! 오류가 없어여!', inline=False)
        
        await ch.send(embed = embed)


    if message.content == '!진화2':
        ch = client.get_channel(840261015349755904)
        embed = discord.Embed(title = '초심이 업데이트', description = '초심이가 진화해서 !초심아 명령어를 통해 더 많은 말을 할수 있게 됬어여~!', colour = 0xA30FE2)
        
    
        await ch.send(embed = embed)


    if message.content == '!도박':
        ran = random.randint(1, 2)
        if ran == 1:
            d = "가즈아아아아!!"
        if ran == 2:
            d = "멈춰!!!"
        await message.channel.send(d)

    if message.content == '!초심아':
        ran = random.randint(1, 5)
        if ran == 1:
            d = "네!"
        if ran == 2:
            d = "초심이 여기 있어여~!"
        if ran == 3:
            d = "초심이를 부르셨나요~?" 
        if ran == 4:
            d = "초심이는 쉬는중이에여~!"
        if ran == 5:
            d = "그만 불러여~!"       
           

        await message.channel.send(d)    


       


@tasks.loop(seconds=1)
async def every_hour_notice(self):
    if datetime.datetime.now().minute == 0 and datetime.datetime.now().second == 0:
    
        io = client.get_guild(837463787224956971), client.get_channel(837463804425666610)
        await io.send("시간 테스트 성공!")

            
        time.sleep(1)
        return



client.run('token')