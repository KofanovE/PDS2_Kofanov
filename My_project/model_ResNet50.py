import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.callbacks import ModelCheckpoint



# Функція для створення, навчання, тестування та збереження моделі класифікації фруктів по зображенню.
def train_n_test_model(train_dir, test_dir, path_to_save):
    """
    Function creates and tests a convolutional neural network. The model is saved in the specified directory.

    :param train_dir: the way to direction with train data (str)
    :param test_dir: the way to  direction with test data (str)
    :param test_dir: the way to  direction from saving the model (str)

    """

    # визначення параметрів для обробки зображень
    img_width, img_height = 227, 227
    batch_size = 64

    # створення об'єкті для генерації зображень
    train_datagen = ImageDataGenerator(rescale=1./255,
                                       rotation_range=20,
                                       shear_range=0.2,
                                       width_shift_range=0.2,
                                       height_shift_range=0.2,
                                       horizontal_flip=True)
    test_datagen = ImageDataGenerator(rescale=1./255)

    # створення генераторів зображень для навчання та тестування моделі
    train_generator = train_datagen.flow_from_directory(train_dir,
                                                        target_size=(img_width, img_height),
                                                        batch_size=batch_size,
                                                        class_mode='categorical')
    test_generator = test_datagen.flow_from_directory(test_dir,
                                                      target_size=(img_width, img_height),
                                                      batch_size=batch_size,
                                                      class_mode='categorical')

    # визначення архітектури моделі
    model = Sequential()

    model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(img_width, img_height, 3)))
    model.add(MaxPooling2D((2, 2)))

    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D((2, 2)))

    model.add(Conv2D(128, (3, 3), activation='relu'))
    model.add(MaxPooling2D((2, 2)))


    model.add(Conv2D(256, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Flatten())

    model.add(Dense(512, activation='relu'))
    model.add(Dropout(0.5))

    model.add(Dense(len(os.listdir(train_dir)), activation='softmax'))

    # компіляція моделі
    model.compile(loss='categorical_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])

    model_checkpoint_callback = ModelCheckpoint(
        filepath='C:/Users/админ/PycharmProjects/PDS2/PDS2_Kofanov/My_project/Results/{epoch:02d}.h5',
        save_weights_only=True,
        monitor='val_accuracy',
        mode='max',
        save_best_only=True)

    # навчання моделі
    model.fit(train_generator,
              steps_per_epoch=train_generator.samples // batch_size,
              validation_data=test_generator,
              validation_steps=test_generator.samples // batch_size,
              epochs=100)

    # визначення і відображення якості моделі з допомогою тестового набору даних
    accuracy = model.evaluate(test_generator)[1]
    print('Accuracy:', accuracy)

    # збереження моделі в заданій директорії
    model.save(path_to_save + '/fruit_classifier_ResNet50_100_full.h5')



if __name__ == '__main__':

    # шлях до директорії з даними навчальної вибірки
    train_dir = 'C:/Users/админ/PycharmProjects/PDS2/PDS2_Kofanov/My_project/Datasets/dataset_parser'

    # шлях до директорії з даними тестової вибірки
    test_dir = 'C:/Users/админ/PycharmProjects/PDS2/PDS2_Kofanov/My_project/Datasets/dataset_test_full'

    # шлях до директорії для збереження отриманої моделі
    path_to_save = 'C:/Users/админ/PycharmProjects/PDS2/PDS2_Kofanov/My_project/Results'

    # створення моделі класифікації
    train_n_test_model(train_dir, test_dir, path_to_save)