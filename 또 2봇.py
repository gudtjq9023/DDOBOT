import discord, asyncio, datetime, pytz, dhooks

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))   

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('안녕 또봇'):
        await message.channel.send('안녕!')
    
    if message.content.startswith('현찌마'):
        await message.channel.send('현도 찌찌 마그넷!')

    if message.content.startswith('도배'):
        for i in range(5):
            await message.channel.send('현찌마')

    if message.content == "출석": # 메세지 감지
        await message.channel.send ("{} | {}, Hello".format(message.author, message.author.mention))
        await message.author.send ("{} | {}, User, Hello".format(message.author, message.author.mention))
        
    if message.content.startswith("!청소"):
        number = int(message.content.split(" ")[1])
        await message.delete()
        await message.channel.purge(limit=number)
        await message.channel.send(f"{number}개의 메시지 삭제 완료!")

    if message.content.startswith("!불법사이트"):
        embed = discord.Embed(title="위험한 사이트", description="[현찌마의 불법사이트!](https://lolline.netlify.app/)", color=0x00ff00)
        embed.add_field(name="팡질리가 개발했습니다!", value="조심하세요..!", inline=True)
        embed.set_footer(text="경고!")
        await message.channel.send(embed=embed)

    
       



    

client.run('ODk5Njg3MjIwOTkzMjIwNjM5.YW2ZBA.7EJLIMMv93eSEvfQAR6aIoXhYLM')

