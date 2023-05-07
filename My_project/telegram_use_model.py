from keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input
import numpy as np
import os

from scraper_images import fruit_n_vegetables_eng


# Функція для класифікації фруктів чи овочів по зображенню з використанням збереженої моделі класифікації.
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

