from PIL import Image
import os
from skimage import io
from skimage import exposure

input_folder = 'C:/Users/админ/PycharmProjects/PDS2/PDS2_Kofanov/My_project/dataset_free'
output_folder = 'C:/Users/админ/PycharmProjects/PDS2/PDS2_Kofanov/My_project/Modify_Images'

# Создаем новую папку для сохранения обработанных изображений
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Проходимся по каждому файлу в папке "input"
for filename in os.listdir(input_folder):
    # Извлекаем расширение файла
    ext = os.path.splitext(filename)[1]
    # Если расширение не .jpg, конвертируем изображение в формат .jpg
    if ext != '.jpg':
        with Image.open(os.path.join(input_folder, filename)) as img:
            img = img.convert('RGB')
            filename = os.path.splitext(filename)[0] + '.jpg'
            img.save(os.path.join(input_folder, filename), 'JPEG')

    # Открываем изображение и изменяем его размер до 227х227
    with Image.open(os.path.join(input_folder, filename)) as img:
        img = img.resize((227, 227))
        # Преобразуем изображение в оттенки серого
        img = img.convert('L')

        # Сохраняем изображение в папку "output"
        img.save(os.path.join(output_folder, filename))


    image = io.imread(os.path.join(output_folder, filename))
    # нормализуем изображение
    normalized_image = exposure.rescale_intensity(image)
    # сохраняем нормализованное изображение
    io.imsave(os.path.join(output_folder, filename), normalized_image)


    img = Image.open(os.path.join(output_folder, filename))
    # поворачиваем изображение на 90 градусов
    rotated_img = img.rotate(90)
    rotated_img.save(os.path.join(output_folder, 'rotated_90_'+filename))
    # поворачиваем изображение на 180 градусов
    rotated_img = img.rotate(180)
    rotated_img.save(os.path.join(output_folder, 'rotated_180_'+filename))
    # поворачиваем изображение на 270 градусов
    rotated_img = img.rotate(270)
    rotated_img.save(os.path.join(output_folder, 'rotated_270_'+filename))



