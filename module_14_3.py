from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb_start = ReplyKeyboardMarkup(resize_keyboard=True)

calc_button = KeyboardButton(text='Рассчитать')
info_button = KeyboardButton(text='Информация')
buy_button = KeyboardButton(text='Купить')

kb_start.add(buy_button)
kb_start.add(calc_button)
kb_start.add(info_button)

buy_menu = InlineKeyboardMarkup()
prod1_butt = InlineKeyboardButton(text='product1', callback_data="product_buying")
prod2_butt = InlineKeyboardButton(text='product2', callback_data="product_buying")
prod3_butt = InlineKeyboardButton(text='product3', callback_data="product_buying")
prod4_butt = InlineKeyboardButton(text='product4', callback_data="product_buying")
buy_menu.add(prod1_butt)
buy_menu.add(prod2_butt)
buy_menu.add(prod3_butt)
buy_menu.add(prod4_butt)

kb_menu = InlineKeyboardMarkup()
norm_calc_button = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
formulas_button = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb_menu.add(norm_calc_button)
kb_menu.add(formulas_button)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb_start)

@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb_menu)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('Для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.answer()

@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    data_weight = int(data['weight'])
    data_growth = int(data['growth'])
    data_age = int(data['age'])
    calories_calc = 10 * data_weight + 6.25 * data_growth - 5 * data_age + 5
    await message.answer(f"Ваша норма калорий {calories_calc}")
    await state.finish()

@dp.message_handler(text='Купить')
async def get_buying_list(message):
    await message.answer('Название: Product<number> | Описание: описание <number> | Цена: <number * 100>')
    with open ('path','rb') as img1:
        await message.answer_photo('')
    await message.answer('Название: Product<number> | Описание: описание <number> | Цена: <number * 100>')
    with open ('path','rb') as img1:
        await message.answer_photo('')
    await message.answer('Название: Product<number> | Описание: описание <number> | Цена: <number * 100>')
    with open ('path','rb') as img1:
        await message.answer_photo('')
    await message.answer('Название: Product<number> | Описание: описание <number> | Цена: <number * 100>')
    with open ('path','rb') as img1:
        await message.answer_photo('')
    await message.answer('Выберите продукт для покупки:', reply_markup=buy_menu)

@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()



@dp.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)