import discord
import asyncio
import os

client = discord.Client()

token = "Nzk5NTk5MDQ3NzYwODA1ODk4.YAF6pA.nooR-CBArADpnEUsuCo4011LtHU"

@client.event
async def on_ready():

    print(client.user.name) 
    print('봇이 성공적으로 실행됨')
    game = discord.Game('봇이 놀러다니는중~')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
     if message.content == "1로꾸":
         await message.channel.send("저를 만드신 잘생긴 갓 창조주님!")
     
     if message.content == "1도움":
        await message.channel.send("저는 여러분과 소통하는 소통봇 로꾸봇이에요!")

     if message.content == "1안녕":
        await message.channel.send("인사 잘~한다!")

     if message.content == "1디스코드":
        await message.channel.send("https://discord.gg/knzYdMG9NC")

     if message.content == "1나잘생김":
        await message.channel.send("ㅋ")

     if message.content == "1나예쁘지":
        await message.channel.send("아뉘!")

     if message.content == "1끝말잇기":
        await message.channel.send("그런건 크시랑 하세요;;")

     if message.content == "1니얼굴":
        await message.channel.send("겁나잘생김")

     if message.content == "1잼민이":
        await message.channel.send("응 너")

     if message.content == "1로꾸님너무잘생겼고사랑해요":
        await message.channel.send("당신은 이스터에그권을 받았습니다 로꾸는 목소리를 들려줄겁니다")
     
     if message.content == "1하픽":
        await message.channel.send("망~~~~~게에에에ㅔ에ㅔ에에에에ㅔ엠")
    
     if message.content == "1신고":
        await message.channel.send("봇에대한 문제와 추가요청은 @추가 라고 말씀해주세요")
     
     if message.content == "@추가": 
        embed = discord.Embed(title="추가할 메세지는 무엇인가요?", description="추가할메세지와 추가했을때 반응을 아기(4살)#7899로 문의해주세요", color=0x00ff00)
        embed.add_field(name="헉헉덜덜 오늘도 코딩인가", value="살..려..줘",inline=True)
        embed.set_footer(text="사용자분들의 피드백은 봇개발에 큰힘이됩니다!")
        await message.channel.send(embed=embed)

     if message.content == "1퐈이브꿀꿀이": 
        embed = discord.Embed(title="퐈이브는 저희팀 수령동지입니다", description="그는 야생동물-멧돼지(꿀꿀이)입니다", color=0x00ff00)
        embed.set_footer(text="정말못생겼다!!")
        await message.channel.send(embed=embed)

     if message.content == "1타카기":
        embed = discord.Embed(title="타카기짱사랑행", description="타카기타카기(https://www.youtube.com/watch?v=9s-7a4_NjAo)", color=0x00ff00)   
        embed.set_footer(text="헤헤헤헤헤헤헤")
        await message.channel.send(embed=embed)
     


    
    

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)    

  
