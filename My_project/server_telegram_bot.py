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


fruit_n_vegetables_eng = ['avocado', 'orange', 'banana', 'beets', 'grapes', 'grapefruit',
                          'cabbage', 'potatoes', 'kiwi', 'lemon', 'carrot', 'cucumber', 'bell pepper',
                          'champignon', 'tomato', 'green onion', 'onion', 'garlic', 'apples', 'ginger']


API_TOKEN = '5867858545:AAGNrhwmNBUlrJv3njZO5v5NiOXSveo_8DA'

# розташування моделі
model_folder = 'C:/Users/админ/PycharmProjects/PDS2/PDS2_Kofanov/My_project/Results/fruit_classifier_ResNet50_50.h5'

# створення об'єкта бота
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()

# диспетчер
dp = Dispatcher(bot, storage=storage)

# # налаштування логування
# logging.basicConfig(level=logging.INFO)



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



def fruit_prediction(test_fruit, model_folder):
    """
    Function uses classification model for prediction classes of fruit or vegetables from image.

    :param test_fruit: the way to image for classification (str)
    :param model_folder: the way to  direction with saved model (str)
    :return pred_clas_name: name of predicted class (str)

    """

    # завантаження збереженої моделі
    model = load_model(model_folder)

    # завантаження зображення та його модифікація до стандартного формату
    img = image.load_img(test_fruit, target_size=(227, 227))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    # x = preprocess_input(x)

    # класифікація зображення та відображення ймовірності відношення для кожного класу в процентному співвідношенні
    predictions = model.predict(x)
    predictions = np.round(predictions, decimals=2)
    pred_percentage = (predictions / np.sum(predictions)) * 100
    # print(pred_percentage)

    # визначення класу з найбільшим процентним співвідношенням
    predicted_class = np.argmax(predictions)

    # відображення номеру класу як результату класифікації
    # print('Predicted class:', predicted_class)

    # відображення текстової назви даного класу
    class_names = sorted(fruit_n_vegetables_eng)
    pred_class_name = class_names[predicted_class]
    # print(pred_class_name)
    return pred_class_name


if __name__ == '__main__':

    #запуск пуллінга
    executor.start_polling(dp, skip_updates=True)
