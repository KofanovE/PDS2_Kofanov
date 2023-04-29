import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.callbacks import ModelCheckpoint

# Определяем путь к папке с датасетом фруктов
train_dir = 'C:/Users/админ/PycharmProjects/PDS2/PDS2_Kofanov/My_project/dataset_modify'
test_dir = 'C:/Users/админ/PycharmProjects/PDS2/PDS2_Kofanov/My_project/dataset_test'
path_to_save = 'C:/Users/админ/PycharmProjects/PDS2/PDS2_Kofanov/My_project/Results'

# Определяем параметры для обработки изображений
img_width, img_height = 227, 227
batch_size = 32

# Создаем объекты для генерации изображений
train_datagen = ImageDataGenerator(rescale=1./255,
                                   shear_range=0.2,
                                   zoom_range=0.2,
                                   horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1./255)

# Создаем генераторы изображений для обучения и тестирования модели
train_generator = train_datagen.flow_from_directory(train_dir,
                                                    target_size=(img_width, img_height),
                                                    batch_size=batch_size,
                                                    class_mode='categorical')
test_generator = test_datagen.flow_from_directory(test_dir,
                                                  target_size=(img_width, img_height),
                                                  batch_size=batch_size,
                                                  class_mode='categorical')

# Определяем архитектуру модели
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(img_width, img_height, 3)))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(len(os.listdir(train_dir)), activation='softmax'))

# Компилируем модель
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

model_checkpoint_callback = ModelCheckpoint(
    filepath='C:/Users/админ/PycharmProjects/PDS2/PDS2_Kofanov/My_project/Results.{epoch:02d}.h5',
    save_weights_only=True,
    monitor='val_accuracy',
    mode='max',
    save_best_only=True
)



# Обучаем модель
model.fit(train_generator,
          steps_per_epoch=train_generator.samples // batch_size,
          validation_data=test_generator,
          validation_steps=test_generator.samples // batch_size,
          epochs=20)

# Оцениваем точность модели на тестовых данных
accuracy = model.evaluate(test_generator)[1]
print('Accuracy:', accuracy)
