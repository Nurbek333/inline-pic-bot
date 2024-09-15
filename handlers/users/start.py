from aiogram.types import Message,InlineQueryResultPhoto,InlineQuery
from loader import dp,db
from aiogram.filters import CommandStart
from handlers.users.search_images import fetch_inline_search_images


@dp.message(CommandStart())
async def start_command(message:Message):
    full_name = message.from_user.full_name
    telegram_id = message.from_user.id
    try:
        db.add_user(full_name=full_name,telegram_id=telegram_id) #foydalanuvchi bazaga qo'shildi
        await message.answer(text="Assalomu alaykum, botimizga hush kelibsiz")
    except:
        await message.answer(text="Assalomu alaykum")

@dp.inline_query()
async def inline_salom(inline_query:InlineQuery):

    try:
        text = inline_query.query  
        photos = await fetch_inline_search_images(text, count=50)
        results = [
            InlineQueryResultPhoto(
                id=str(i),
                photo_url=img,
                thumbnail_url=img
            )
            for i, img in enumerate(photos)
        ]  
        await inline_query.answer(results=results)

    except Exception as e:
        print(f"xatolik: {e}") 