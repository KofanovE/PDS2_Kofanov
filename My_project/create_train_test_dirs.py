from sklearn.model_selection import train_test_split
import os
import shutil


test_size = 0.2

# Путь к папке с исходными изображениями
source_dir = 'C:/Users/админ/PycharmProjects/PDS2/PDS2_Kofanov/My_project/Datasets/dataset_parser'

# Путь к папке, в которую будут сохранены изображения для обучения модели
train_dir = 'C:/Users/админ/PycharmProjects/PDS2/PDS2_Kofanov/My_project/Datasets/train_dataset'

# Путь к папке, в которую будут сохранены изображения для тестирования модели
test_dir = 'C:/Users/админ/PycharmProjects/PDS2/PDS2_Kofanov/My_project/Datasets/test_dataset'

shutil.rmtree(train_dir)
shutil.rmtree(test_dir)

os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

for folders in fruit_n_vegetables_eng:
    os.makedirs(os.path.join(train_dir, folders))
    os.makedirs(os.path.join(test_dir, folders))

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






