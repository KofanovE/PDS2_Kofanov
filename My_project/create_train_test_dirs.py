from sklearn.model_selection import train_test_split
import os
import shutil
from scraper_images import fruit_n_vegetables_eng


# Функція для створення навчальної та тестової вибірки
def create_train_n_test_dir(source_dir, train_dir, test_dir, test_size):
    """
    The functon creates directions for train and test datasets from dataset with date.

    :param source_dir: the way to source direction with data (str)
    :param train_dir: the way to direction with train data (str)
    :param test_dir: the way to  direction with test data (str)
    :param test_size: the size of test data in percents from 0 to 1 (flt)

    """

    # видалення директорій зі старими датасетами з даними
    if os.path.exists(train_dir):
        shutil.rmtree(train_dir)
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)

    # створення нових директорій для навчальних та тестових наборів
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)

    # Створення директорій для кожного класу в навчальній та тестовій директорії окремо.
    for folders in fruit_n_vegetables_eng:
        os.makedirs(os.path.join(train_dir, folders))
        os.makedirs(os.path.join(test_dir, folders))

    # Розділення даних на навчальну та тестову вибірки для кожного класу окремо.
    for categoria_folder in os.listdir(source_dir):
        source_categoria_dir = os.path.join(source_dir, categoria_folder)
        train_categoria_dir = os.path.join(train_dir, categoria_folder)
        test_categoria_dir = os.path.join(test_dir, categoria_folder)

        image_files = os.listdir(source_categoria_dir)
        train_files, test_files = train_test_split(image_files, test_size=test_size)

        os.makedirs(train_categoria_dir, exist_ok=True)
        os.makedirs(test_categoria_dir, exist_ok=True)

        for file_name in train_files:
            source_path = os.path.join(source_categoria_dir, file_name)
            train_path = os.path.join(train_categoria_dir, file_name)
            shutil.copyfile(source_path, train_path)

        for file_name in test_files:
            source_path = os.path.join(source_categoria_dir, file_name)
            test_path = os.path.join(test_categoria_dir, file_name)
            shutil.copyfile(source_path, test_path)



if __name__ == '__main__':

    # розмір тестової вибірки
    test_size = 0.2

    # шлях до директорії з завантаженими зображеннями
    source_dir = '/My_project/Datasets/dataset_parser'

    # шлях до директорії, де будуть збережені дані для навчання моделі
    train_dir = '/My_project/Datasets/train_dataset'

    # шлях до директорії, ду будуть збережені дані для тестування моделі
    test_dir = '/My_project/Datasets/test_dataset'

    # виконання функції створення вибірок
    create_train_n_test_dir(source_dir, train_dir, test_dir, test_size)


