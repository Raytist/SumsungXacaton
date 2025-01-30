import datetime
import asyncio
import datetime
import schedule
from aiogram import Dispatcher, types, Router, F, Bot
from keyboards import *
from aiogram.fsm.state import StatesGroup, State
from aiogram.filters import Command
from configs import TG_TOKEN
from apscheduler.schedulers.asyncio import AsyncIOScheduler

router = Router()
bot = Bot(TG_TOKEN)
stats = 9999
n = 1
target = datetime.time(hour=20, minute=6)


@router.message(Command('start'))
async def start(message: types.Message):
    await message.answer('бот для просмотра статистики', reply_markup=greet_kb)


async def send(messaage: types.Message):
    while True:
        print(now.time())
        now = datetime.datetime.now()
        if now.time() == target:
            await bot.send_message(messaage.from_user.id, f'время: статистика по просмотрам:\n{stats}')
            await asyncio.sleep(120)
        await asyncio.sleep(60)

@router.callback_query(F.data == 'show_graph')
async def show_grah(callback: types.CallbackQuery):
    await callback.answer()
    await bot.send_message(callback.from_user.id,text="*график*",reply_markup=greet_kb_grah)
@router.callback_query(F.data == 'get_stats_for_day')
async def get_stats_for_day(callback: types.CallbackQuery):
    await callback.answer()
    await bot.send_message(callback.from_user.id,
                           text=f'статистика по просмотрам за день:\nтелеграм: {stats}\nвк: {stats + 15}\nвеб-сайт: {stats - 1000}',reply_markup=greet_kb_stats)



@router.callback_query(F.data == 'get_stats_for_week')
async def get_stats_for_day(callback: types.CallbackQuery):
    await callback.answer()
    await bot.send_message(callback.from_user.id,
                           text=f'статистика по просмотрам за неделю:\nтелеграм: {stats}\nвк: {stats + 15}\nвеб-сайт: {stats - 1000}',
                           reply_markup=greet_kb_stats)


@router.callback_query(F.data == 'back')
async def back(callback: types.CallbackQuery):
    callback.message.delete()
    await callback.answer()
    callback.message.delete()
    await start(callback.message)


# стата за месяц
@router.callback_query(F.data == 'get_stats_for_month')
async def get_stats_for_day(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.answer()
    await bot.send_message(callback.from_user.id,
                           text=f'статистика по просмотрам за месяц:\nтелеграм: {stats}\nвк: {stats + 15 * 15}\nвеб-сайт: {stats * 15 - 1000}',reply_markup=greet_kb_stats)


@router.callback_query(F.data == 'show_most_popular_post')
async def show_popular_post(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.answer()
    await bot.send_message(callback.from_user.id,
                           text='*ссылка на популярный пост в вк* \nпросмотры: n\n'
                                '*ссылка на популрный пост на сайте*\nпросмотры: n\n'
                                '*ссылка на популярный пост в тг* \n просмотры: n \n',reply_markup=greet_kb_back)


@router.callback_query(F.data == 'show_most_unpopular_post')
async def show_unpopular_post(callback: types.CallbackQuery):

    await callback.answer()
    await callback.message.delete()
    await bot.send_message(callback.from_user.id,
                           text='*ссылка на непопулярный пост в вк* \nпросмотры: n\n'
                                '*ссылка на непопулрный пост на сайте*\nпросмотры: n\n'
                                '*ссылка на непопулярный пост в тг* \n просмотры: n \n',reply_markup=greet_kb_back)


@router.callback_query(F.data == 'back_in stats')
async def back_stats(callback: types.CallbackQuery):
    await callback.answer()
    await get_stats_for_day(callback)
    await callback.message.delete()

@router.callback_query(F.data == 'back')
async def back(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.answer()
    await start(callback.message)

@router.callback_query(F.data == 'back_out_grah')
async def back_out_grah(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.answer()
    await get_stats_for_day(callback)