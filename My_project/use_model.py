from keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input
import numpy as np
import os

model_folder = 'C:/Users/админ/PycharmProjects/PDS2/PDS2_Kofanov/My_project/Results/fruit_classifier_color_5.h5'
test_dir = 'C:/Users/админ/PycharmProjects/PDS2/PDS2_Kofanov/My_project/dataset_test'

# '/apples/Яблуко_1.jpg'
# '/banana/Банан_1.jpg'
# '/carrot/Морква_1.jpg'
# '/avocado/Авокадо_1.jpg'
# '/beets/Буряк_1.jpg'

test_fruit = '/avocado/Авокадо_1.jpg'
# Загрузка сохраненной модели
model = load_model(model_folder)

# Загрузка изображения и преобразование его к нужному размеру и формату
img = image.load_img(test_dir + test_fruit, target_size=(227, 227))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
# x = preprocess_input(x)

# Классификация изображения с помощью модели
predictions = model.predict(x)
predictions = np.round(predictions, decimals=2)
pred_percentage = (predictions / np.sum(predictions)) * 100
print(pred_percentage)


predicted_class = np.argmax(predictions)

# Вывод результата классификации
print('Predicted class:', predicted_class)

class_names = sorted(os.listdir(test_dir))
pred_class_name = class_names[predicted_class]
print(pred_class_name)
