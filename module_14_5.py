from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import crud_function

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb_start = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Регистрация')],
        [KeyboardButton(text='Рассчитать'), KeyboardButton(text='Информация')],
        [KeyboardButton(text='Купить')]
    ],
    resize_keyboard=True
)


buy_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='product1', callback_data="product_buying")],
        [InlineKeyboardButton(text='product2', callback_data="product_buying")],
        [InlineKeyboardButton(text='product3', callback_data="product_buying")],
        [InlineKeyboardButton(text='product4', callback_data="product_buying")]
    ]
)


kb_menu = InlineKeyboardMarkup()
norm_calc_button = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
formulas_button = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb_menu.add(norm_calc_button)
kb_menu.add(formulas_button)

prod_list = crud_function.get_all_products()


class RegistrationState(StatesGroup):
    username = State()
    email = State
    age = State
    balance = State(1000)


@dp.message_handler(text='Регистрация')
async def sing_up(message):
    await message.answer('Введите имя пользователя (только латинский алфавит):')
    await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    await state.update_data(username=message.text)
    if crud_function.is_included(message.text):
        await message.answer('Введите свой email:')
        await RegistrationState.email.set()
    else:
        await message.answer('Пользователь существует, введите другое имя')
        await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer('Введите свой возраст:')
    await RegistrationState.age.set()

@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age=message.text)
    user_data = await state.get_data()
    crud_function.add_user(user_data['username'], user_data['email'], user_data['age'])
    await message.answer('Регистрация прошла успешно!')
    await state.finish()


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
    with open ('../Images/img (1).png', 'rb') as img1:
        await message.answer(f'Название: {prod_list[0][0]} | Описание: {prod_list[0][1]}  | Цена: {prod_list[0][2]}')
        await message.answer_photo(img1)
    with open ('../Images/img (2).png', 'rb') as img2:
        await message.answer(f'Название: {prod_list[1][0]} | Описание: {prod_list[1][1]}  | Цена: {prod_list[1][2]}')
        await message.answer_photo(img2)
    with open ('../Images/img (3).png', 'rb') as img3:
        await message.answer(f'Название: {prod_list[2][0]} | Описание: {prod_list[2][1]}  | Цена: {prod_list[2][2]}')
        await message.answer_photo(img3)
    with open ('../Images/img (4).png', 'rb') as img4:
        await message.answer(f'Название: {prod_list[3][0]} | Описание: {prod_list[3][1]}  | Цена: {prod_list[3][2]}')
        await message.answer_photo(img4)
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