import logging
from aiogram import Bot, Dispatcher, executor, types
from chack_word import check_word
from transliterate import to_cyrillic, to_latin

API_TOKEN = '5196919255:AAG0M-3pzMuMasiSFr3w4tRB4ZmWxM14oug'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
   
    await message.reply("So'zni to'g'ri yozilganini tekshiruvchi botga xush kelibsiz\n biror so'z yozing bot tekshirib beradi")


@dp.message_handler()
async def imlo_check(message: types.Message):
    word = message.text
    if word.isascii():
        word = to_cyrillic(word)

    result = check_word(word)
    if result['available']:
        response = f'✅{word.capitalize()} ➖ {to_latin(word.capitalize())}'
    else:
        response = f'❌{word.capitalize()} ➖ {to_latin(word.capitalize())}\n--------------------------\n'
        for text in result['matches']:
            response += f'✅{text.capitalize()} ➖ {to_latin(text.capitalize())}\n'
    
    await message.answer(response)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)