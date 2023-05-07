import logging
import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from keras.models import load_model
from keras_preprocessing import image
from keras_preprocessing.image import img_to_array
import numpy as np
import tensorflow as tf
import cv2
from cred import API_TOKEN
from telegram_use_model import fruit_prediction


# розташування моделі
model_folder = 'C:/Users/админ/PycharmProjects/PDS2/PDS2_Kofanov/My_project/Results/fruit_classifier_ResNet50_50.h5'

# створення об'єкта бота
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()

# диспетчер
dp = Dispatcher(bot, storage=storage)

# налаштування логування
logging.basicConfig(level=logging.INFO)



# обробка команди /start
@dp.message_handler(commands=['start'])
async def echo(message: types.Message):

  await message.reply('Привіт! Я бот, що розпізнає овочі та фрукти по фото')



# обробка команди /help
@dp.message_handler(commands=['help'])
async def echo(message: types.Message):

  await message.reply('Просто відправ мень зображення овоча чи фрукта, який необхідно розпізнати')



# класифікація завантаженого фото фрукта
@dp.message_handler(content_types=[types.ContentType.PHOTO])
async def download_photo(message: types.Message):

    # завантаження фото в директорію по замовченню
    await message.photo[-1].download()

    # визначаємо шлях до завантаження фото
    img_path = (await bot.get_file(message.photo[-1].file_id)).file_path

    # отримання класифікації
    pred = fruit_prediction(img_path, model_folder)

    # відправка результату класифікації
    await message.answer(f"Хм... схоже на {pred}..")




if __name__ == '__main__':

    #запуск пуллінга
    executor.start_polling(dp, skip_updates=True)
