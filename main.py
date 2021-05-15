import discord
import openpyxl
client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("!명령어를 입력하세요")
    game = discord.Game("실행하려면 !명령어")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("!목장이야기"):
        await message.channel.send("진구가 업보청산했던 그거? 에휴.. 말도마. ")

    if message.content.startswith("!도라야끼"):
        await message.channel.send("뭐..? 정말! 그거 나주면 안돼?.")


    if message.content.startswith("!안녕"):
        await message.channel.send("안녕~.")

    if message.content.startswith("!성우변경"):
        await message.channel.send("미안하지만 나는 목소리가 없어서... 채팅봇이야~")
    if message.content.startswith("!잘가"):
        await message.channel.send("잘가~")

    if message.content.startswith("/사진"):
        pic = message.content.split(" ")[1]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("/채널메시지"):
        channel = message.content[7:25]
        msg = message.content[26:]
        await client.get_channel(int(channel)) .send(msg)

    if message.content.startswith("/DM"):
        author = message.guild.get_member(int(message.content[4:22]))
        msg = message.content[23:]
        await author.send(msg)

    if message.content.startswith("/경고"):
        author = message.guild.get_member(int(message.content[4:22]))
        file = openpyxl.load_workbook("경고.xlsx")
        sheet = file.active
        i = 1
        while True:
            if sheet["A" + str(i)].value == str(author.id):
                sheet["B" + str(i)].value = int(sheet["B" + str(i)].value) + i
                file.save("경고")
                if sheet["B" + str(i)].value == 15:
                    await message.guild.ban(author)
                    await message.channel.send("경고 15회 누적이야... 마치 노진구처럼 흉악범이구나...")
                else:
                    await  message.channel.send("경고를 1번만 받았어!")
                break
            if sheet["A" + str(i)].value is None:
                sheet["A" + str(i)].value = str(e.author.id)
                sheet["B" + str(i)].value = 1
                file.save("경고.xlsx")
                await message.channel.send("경고를 1번만 받았어.")
                break
            i += 1
    if message.content.startswith("!변경"):
        await message.channel.send("암기빵처럼~ 잘 암기하길 바래..")

    if message.content.startswith("!생일"):
        await message.channel.send("생일 축하해!")

    if message.content.startswith("!파란너구리"):
        await message.channel.send("아니야! 고양이형 로봇이라고!!!!!!!!!!!!!")
    if message.content.startswith("!사랑해"):
        await message.channel.send("나도~")
    if message.content.startswith("!명령어"):
        await message.channel.send("명령어 목록 : !키바맞음, !변경, !생일, !사랑해, !안녕, !성우변경, !안녕, !잘가, !목장이야기 ")
    if message.content.startswith("!키바맞음"):
        await message.channel.send("아닌것 같아...")
    if message.content.startswith("!메바맞음"):
        await message.channel.send("얘! 놀리지마!")





client.run("ODQxMTE0NzA0ODI3MjUyNzk3.YJiDHA.K_EttOYuc2aFOfTjNYQhWsCcqs0")