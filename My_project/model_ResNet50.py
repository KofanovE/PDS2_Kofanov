import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.callbacks import ModelCheckpoint

# Определяем путь к папке с датасетом фруктов
train_dir = 'C:/Users/админ/PycharmProjects/PDS2/PDS2_Kofanov/My_project/Datasets/train_dataset'
test_dir = 'C:/Users/админ/PycharmProjects/PDS2/PDS2_Kofanov/My_project/Datasets/test_dataset'
path_to_save = 'C:/Users/админ/PycharmProjects/PDS2/PDS2_Kofanov/My_project/Results'

# Определяем параметры для обработки изображений
img_width, img_height = 227, 227
batch_size = 64

# Создаем объекты для генерации изображений
train_datagen = ImageDataGenerator(rescale=1./255,
                                   rotation_range=20,
                                   shear_range=0.2,
                                   width_shift_range=0.2,
                                   height_shift_range=0.2,
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


model.add(Conv2D(256, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())

model.add(Dense(512, activation='relu'))
model.add(Dropout(0.5))

model.add(Dense(len(os.listdir(train_dir)), activation='softmax'))

# Компилируем модель
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

model_checkpoint_callback = ModelCheckpoint(
    filepath='C:/Users/админ/PycharmProjects/PDS2/PDS2_Kofanov/My_project/Results/{epoch:02d}.h5',
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
          epochs=50)

# Оцениваем точность модели на тестовых данных
accuracy = model.evaluate(test_generator)[1]
print('Accuracy:', accuracy)

model.save(path_to_save + '/fruit_classifier_ResNet50_50.h5')