import os
import hashlib

clearing_parent_folder  = 'C:/Users/админ/PycharmProjects/PDS2/PDS2_Kofanov/My_project/dataset_parser'

def get_file_hash(file_path):
    """Функция для вычисления хеш-суммы файла"""
    with open(file_path, 'rb') as f:
        file_hash = hashlib.sha256()
        while chunk := f.read(4096):
            file_hash.update(chunk)
        return file_hash.hexdigest()

def remove_duplicate_images(folder_path):
    """Функция для удаления дублирующихся изображений в папке"""
    # Создаем словарь, где ключом является хеш-сумма, а значением – список имен файлов
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

    # Удаляем дубликаты файлов
    for hash_key in hash_to_files:
        files_list = hash_to_files[hash_key]
        if len(files_list) > 1:
            # Оставляем только один файл из списка и удаляем остальные
            for file_path in files_list[1:]:
                os.remove(file_path)
                print(f'Removed file: {file_path}')


for categoria_folder in os.listdir(clearing_parent_folder):
    clearing_folder = os.path.join(clearing_parent_folder, categoria_folder)
    remove_duplicate_images(clearing_folder)





