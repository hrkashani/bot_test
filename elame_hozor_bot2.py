from bale import Bot, Update,CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton, MenuKeyboardMarkup, MenuKeyboardButton

client = Bot(token="1671716800:C4GlxS1GevFc4PTOMCLIX5ZMNik3rwqqvgdBC1qy")
global id
global x
global y
x=[]
y=[]
@client.event
async def on_ready():
	print(client.user.username, "is Ready!")

@client.event
async def on_update(update: Update):
	print(update.update_id)

@client.event
async def on_message(message: Message):
		global id
		global x
		global y
		global st1,st2
		if message.content == '/start': # to get caption or text of message
			#await message.reply('Hi, from python-bale-bot to everyone!')
			if message.chat.is_group_chat:
				await message.reply("It's is a special Hi for groups!") # work when message sent in a group
		if message.content == 'شروع آمار گیری':
			id =message.message_id
			print(id,message.reply_to_message_id)
			await message.reply("آمار گیری شروع شده است ، لطفا بچه ها حضورشونو اعلام کنند:")
			id =message.message_id+1
			print(id,message.reply_to_message_id)
		if message.reply_to_message_id==id:
				print("ok")
				print(message.content)
				text=message.text
				if text[-1]=="1":
					x.append(text)
				else:
					y.append(text)

				st1=""
				for i in x:
					st1+=str(i)+"\n"
				st2=""
				for i in y:
					st2+=str(i)+"\n"
				await message.reply("لیست شریف \n"+st1+"\nلیست میرداماد \n"+st2)
		if message.content == 'پاکسازی': # to get caption or text of message
			#await message.reply('Hi, from python-bale-bot to everyone!')
			x=[]
			y=[]
			if message.chat.is_group_chat:
				 
				await message.reply("لیست شریف \n"+st1+"\nلیست میرداماد \n"+st2)
				await message.reply("لیست پاکسازی شد")
# @client.event
# async def on_message(message: Message):
# 	if message.content == "/start":
# 		reply_markup = InlineKeyboardMarkup()
# 		reply_markup.add(InlineKeyboardButton(text="what is python-bale-bot?", callback_data="python-bale-bot:help"))
# 		reply_markup.add(InlineKeyboardButton(text="package site", url="https://python-bale-bot.ir"), row=2)
# 		reply_markup.add(InlineKeyboardButton(text="package GitHub", url="https://python-bale-bot.ir/github"), row=2)
# 		await message.reply(
# 			f"*Hi {message.author.first_name}, Welcome to python-bale-bot bot*",
# 			components=reply_markup
# 		)

# 	elif message.content == "/keyboard":
# 		await message.reply(
# 			f"*Hi {message.author.first_name}, Welcome to python-bale-bot bot*",
# 			components=MenuKeyboardMarkup().add(MenuKeyboardButton('package site')).add(MenuKeyboardButton('package github'))
# 		)

# 	elif message.content in [
# 		'package site',
# 		'package github'
# 	]:
# 		await message.reply(
# 			"{} is {}".format(message.content, {"package site": 'https://python-bale-bot.ir', "package github": 'https://python-bale-bot.ir/github'}[message.content]),
# 			components=MenuKeyboardMarkup() # to remove menu keyboards
# 		)
# @client.event
# async def on_message(message: Message):
#     if message.content == '/give_name_without_timeout':
#         await message.reply('what is your name?')
#         def answer_checker(m: Message):
#             return message.author == m.author and bool(message.text)
#         answer_obj: Message = await client.wait_for('message', check=answer_checker)
#         return await answer_obj.reply(f'Your name is {answer_obj.content}')

#     elif message.content == '/give_name_with_timeout':
#         await message.reply('what is your name?')

#         def answer_checker(m: Message):
#             return message.author == m.author and bool(message.text)
#         try:
#             answer_obj: Message = await client.wait_for('message', check=answer_checker, timeout=10.0)
#         except asyncio.TimeoutError:
#             return await message.chat.send('No response received; Therefore, the operation was canceled.')
#         else:
#             return await answer_obj.reply(f'Your name is {answer_obj.content}')
	
@client.event
async def on_callback(callback: CallbackQuery):
    if callback.id>=0:
        await callback.message.reply("ridy")

  #print(callback.data)
# See https://docs.python-bale-bot.ir/en/stable/event.html to get more information about events!

client.run()