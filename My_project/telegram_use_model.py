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



if __name__ == '__main__':

    # шлях до директорії, де знаходиться модель
    model_folder = 'C:/Users/админ/PycharmProjects/PDS2/PDS2_Kofanov/My_project/Results/fruit_classifier_ResNet50_50.h5'

    # шлях до директорії, де знаходяться не використанні в навчанні дані
    test_dir = '/My_project/Old_datasets/dataset_test'

    # '/apples/Яблуко_1.jpg'
    # '/avocado/Авокадо_1.jpg'
    # '/banana/Банан_1.jpg'
    # '/beets/Буряк_1.jpg'
    # '/bell pepper/Перець солодкий_1.jpg'
    # '/carrot/Морква_1.jpg'
    # '/champignon/Печериці_1.jpg'
    # '/cucumber/Огірок_1.jpg'
    # '/garlic/Часник_1.jpg'
    # '/ginger/Імбір_1.jpg'
    # '/grapefruit/Грейпфрут_1.jpg'
    # '/grapes/Виноград_1.jpg'

    # назва директорії і зображення для перевірки моделі на практиці
    test_fruit = '/cucumber/Огірок_1.jpg'

    # виконання функції класифікації фруктів та овочів
    fruit_prediction(test_fruit, test_dir, model_folder)
