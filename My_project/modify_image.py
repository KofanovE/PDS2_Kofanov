from PIL import Image
import os
from skimage import io
from skimage import exposure


# Функція модифікації та збереження даного зображення
def image_modification(filename, carent_folder):
    """
    The functon getting name of image and doing next changes with it:
        - convert to jpg format
        - change size of image to 227*227
        - convert to RGB format
        - normalize of image
        - save modify image

    :param filename: name of image for modification (str)
    :param carent_folder: name of directory for saving modified image

    """

    # отримуємо розширення зображення
    ext = os.path.splitext(filename)[1]

    # Якщо розширення не .jpg, конвертуємо зображення в даний формат
    if ext != '.jpg':
        with Image.open(os.path.join(carent_folder, filename)) as img:
            img = img.convert('RGB')
            filename = os.path.splitext(filename)[0] + '.jpg'
            img.save(os.path.join(carent_folder, filename), 'JPEG')


    # Відкриваємо зображення для виконання операцій над ним
    with Image.open(os.path.join(carent_folder, filename)) as img:

        # змінюємо формат розміру на 227х227
        img = img.resize((227, 227))

        # конвертуємо зображення в RGB тип
        img = img.convert('RGB')
        # img = img.convert('L')

        # зберігаємо результат перетворень
        img.save(os.path.join(carent_folder, filename))

    # відкриваємо збережене зображення
    image = io.imread(os.path.join(carent_folder, filename))

    # виконуємо нормалізацію зображення
    normalized_image = exposure.rescale_intensity(image)

    # зберігаємо нормалізоване зображення
    io.imsave(os.path.join(carent_folder, filename), normalized_image)



if __name__ == '__main__':

    # цільова директорія
    data_folder = 'C:/Users/админ/PycharmProjects/PDS2/PDS2_Kofanov/My_project/Clear_version/dataset_parser'

    # Відкриваємо дочірні директорії (зберігають зображення окремого класу) в цільовій директорії
    for categoria_folder in os.listdir(data_folder):

        # шлях до даної дочірньої директорії
        carent_folder = os.path.join(data_folder, categoria_folder)

        # список файлів, що зберігаються в даній дочірній директорії
        folders = os.listdir(os.path.join(data_folder, categoria_folder))

        # Для кожного файлу використовуємо функцію модифікації
        for filename in folders:
            image_modification(filename, carent_folder)






