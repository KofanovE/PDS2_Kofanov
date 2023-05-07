import os
import hashlib


# Функція для отримання хеш-суми файлу
def get_file_hash(file_path):
    """
    The functon getting name of image and return hash-sum.

    :param file_path: name of image for modification (str)
    :return: hash-sum (int(hex))

    """

    # Відкриття файлу в бінарному режимі
    with open(file_path, 'rb') as f:

        # створення об'єкту для використання шифрування SHA256
        file_hash = hashlib.sha256()

        # Поблочне зчитування файлу
        while chunk := f.read(4096):

            # додавання зчитанного блоку файлу до об'єкту хеш-суми
            file_hash.update(chunk)

        return file_hash.hexdigest()



# Функція для видалення зображень з дублюючими хеш-сумами
def remove_duplicate_images(folder_path):
    """
    The functon deletes images with same hash-sum of file.

    :param folder_path: name of directory with images (str)

    """
    # Створення словника, де ключ являє собою хеш-суму файлу, а значення - імена файлів з однаковими хешами.
    hash_to_files = {}
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith('.jpg') or file_name.endswith('.png'):
                file_path = os.path.join(root, file_name)
                file_hash = get_file_hash(file_path)
                if file_hash in hash_to_files:
                    hash_to_files[file_hash].append(file_path)
                else:
                    hash_to_files[file_hash] = [file_path]

    # Видалення дублікатів зображень.
    for hash_key in hash_to_files:
        files_list = hash_to_files[hash_key]
        if len(files_list) > 1:
            # Лишаємо лише один файл з даною хеш-сумою.
            for file_path in files_list[1:]:
                os.remove(file_path)
                print(f'Removed file: {file_path}')



if __name__ == '__main__':

    # цільова директорія
    data_folder = 'C:/Users/админ/PycharmProjects/PDS2/PDS2_Kofanov/My_project/dataset_parser'

    # Використання функцій отримання хеш-суми та видалення дублікатів для директорій кожного класу.
    for categoria_folder in os.listdir(data_folder):
        clearing_folder = os.path.join(data_folder, categoria_folder)
        remove_duplicate_images(clearing_folder)





