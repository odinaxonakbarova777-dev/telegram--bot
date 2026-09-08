import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from deep_translator import GoogleTranslator
import os

TOKEN = os.getenv("8824880375:AAGzckKonjnv0ICyTamHWp5cc-gv9HAW9Rs")

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(
        "👋 Assalomu alaykum!\n\n"
        "🌍 Men o'zbek 🇺🇿, rus 🇷🇺 va ingliz 🇬🇧 tillarida tarjima qilaman.\n\n"
        "✍️ Istalgan tilda matn yuboring."
    )


@dp.message()
async def translate_message(message: types.Message):
    text = message.text

    if not text:
        await message.answer("❗ Iltimos, matn yuboring.")
        return

    try:
        uz = GoogleTranslator(source="auto", target="uz").translate(text)
        ru = GoogleTranslator(source="auto", target="ru").translate(text)
        en = GoogleTranslator(source="auto", target="en").translate(text)

        result = (
            "🇺🇿 O'zbekcha:\n" + uz
            + "\n\n🇷🇺 Ruscha:\n" + ru
            + "\n\n🇬🇧 Inglizcha:\n" + en
        )

        await message.answer(result)

    except Exception as e:
        print("XATOLIK:", e)
        await message.answer(
            "❌ Tarjima qilishda xatolik yuz berdi.\n\n"
            "Iltimos, boshqa matn yuborib ko'ring."
        )


async def main():
    print("🤖 Tarjimon bot ishga tushdi!")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())