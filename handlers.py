from aiogram import types, Router
from aiogram.filters.command import Command
from aiogram.fsm.state import StatesGroup, State
from ai import query


router = Router()
user_data = []


class Order(StatesGroup):
    waiting_text = State()

@router.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer('бот запущен')

@router.message(Command('ask'))
async def process_copy(message: types.Message):
    try:
        await message.answer(query(message.from_user.first_name,message.text))
    except Exception as e:
        print(e)




    
    
    
