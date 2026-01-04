import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    WebAppInfo,
    BotCommand
)

TOKEN = "8372698456:AAHW_0u0EnG7i8UddtNzTS4jD_yxV5_udAI"
WEB_APP_URL = "https://webappa.netlify.app/"  # <-- Shu yerga o'zingizning URLni yozing

bot = Bot(token=TOKEN)
dp = Dispatcher()


# 🔹 /start komandasi
@dp.message(CommandStart())
async def start(message: Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🚀 Open Web App",
                web_app=WebAppInfo(url=WEB_APP_URL)
            )
        ]
    ])
    await message.answer("Web App ochish:", reply_markup=kb)


# 🔹 SET COMMANDS (menu uchun)
async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="🚀 Web App ochish"),
    ]
    await bot.set_my_commands(commands)


async def main():
    await set_commands(bot)   # 👈 Menu commands set qilinadi
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
