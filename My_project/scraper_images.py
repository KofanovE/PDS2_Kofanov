import os
import urllib.request
from bs4 import BeautifulSoup
import requests


# Списки назв класів на різних мовах:
# англійські назви
fruit_n_vegetables_eng = ['avocado', 'orange', 'banana', 'beets', 'grapes', 'grapefruit',
                          'cabbage', 'potatoes', 'kiwi', 'lemon', 'carrot', 'cucumber', 'bell pepper',
                          'champignon', 'tomato', 'green onion', 'onion', 'garlic', 'apples', 'ginger']

# французькі назви
fruit_n_vegetables_fr = ['avocat', 'orange', 'banane', 'betterave', 'raisin', 'pamplemousse',
                          'chou', 'pomme de terre', 'kiwi', 'citron', 'carotte', 'concombre', 'poivron',
                          'champignon', 'tomate', 'oignon vert', 'oignon', 'ail', 'pomme', 'gingembre']

# іспанські назви
fruit_n_vegetables_sp = ['aguacate', 'naranja', 'plátano', 'remolacha', 'uva', 'pomelo',
                          'repollo', 'papa', 'kiwi', 'limón', 'zanahoria', 'pepino', 'pimiento morrón',
                          'hongo', 'tomate', 'cebolla verde', 'cebolla', 'ajo', 'manzana', 'jengibre']

# шведські назви
fruit_n_vegetables_shv = ['avokado', 'apelsin', 'banan', 'rödbetor', 'grape', 'grapefrukt',
                          'kål', 'potatis', 'kiwi', 'citron', 'morot', 'gurka', 'peppar',
                          'svamp', 'tomat', 'grön lök', 'lök', 'vitlök', 'äpple', 'ingfära']

# німецькі назви
fruit_n_vegetables_de = ['Avocado', 'Orange', 'Banane', 'Rüben', 'Trauben', 'Grapefruit',
                         'Kohl', 'Kartoffeln', 'Kiwi', 'Zitrone', 'Karotte', 'Gurke', 'Paprika',
                         'Champignon', 'Tomate', 'Frühlingszwiebel', 'Zwiebel', 'Knoblauch', 'Äpfel', 'Ingwer']

# італійські назви
fruit_n_vegetables_it = ['avocado', 'arancia', 'banana', 'barbabietola', 'uva', 'pompelmo', 'cavolo',
                         'patate', 'kiwi', 'limone', 'carota', 'cetriolo', 'peperone', 'champignon',
                         'pomodoro', 'cipolla verde', 'cipolla', 'aglio', 'mele', 'zenzero']

# турецькі назви
fruit_n_vegetables_tr = ['avokado', 'portakal', 'muz', 'pancar', 'üzüm', 'greyfurt',
                          'lahana', 'patates', 'kivi', 'limon', 'havuç', 'salatalık', 'biber',
                          "mantar", "domates", "yeşil soğan", "soğan", "sarımsak", "elma", "zencefil"]

# грецькі назви
fruit_n_vegetables_gr = ['αβοκάντο', 'πορτοκάλι', 'μπανάνα', 'παντζάρια', 'σταφύλι', 'γκρέιπφρουτ',
                          'λάχανο', 'πατάτα', 'ακτινίδιο', 'λεμόνι', 'καρότο', 'αγγούρι', 'πιπεριά',
                          'μανιτάρι', 'ντομάτα', 'πράσινο κρεμμύδι', 'κρεμμύδι', 'σκόρδο', 'μήλο', 'τζίντζερ']

# українські назви
fruit_n_vegetables_uk = ['авокадо', 'апельсин', 'банан', 'буряк', 'виноград', 'грейпфрут',
                         'капуста', 'картопля', 'ківі', 'лимон', 'морква', 'огірок', 'перець болгарський',
                         'печериця', 'помідор', 'цибуля зелена', 'цибуля', 'часник', 'яблука', 'імбир']


# список списків назв класів на різних мовах
library_list = [fruit_n_vegetables_eng, fruit_n_vegetables_fr, fruit_n_vegetables_sp, fruit_n_vegetables_shv,
                fruit_n_vegetables_de, fruit_n_vegetables_it, fruit_n_vegetables_tr, fruit_n_vegetables_gr,
                fruit_n_vegetables_uk]



# Функція парсингу зображень на різних мовах в Google_Images
def scrape_images(query, num_images, save_dir, num_lib):
    """
    The functon getting name of image on other languages and scrapes it in Google_Images.

    :param query: name of image for scraping (str)
    :param num_images: needed number of images (int)
    :param save_dir: name of directory for saving got images (str)
    :param num_lib: carent position number library in library_list (int)

    """

    # розділяємо назву на окремі слова
    query = query.split()

    # добавляємо + для інтеграції  назви у строку пошуку
    query = '+'.join(query)

    # формуємо URL адресу з інтегрованою цільовою назвою зображення
    url = "https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"

    # створюємо заголовок браузера
    header = {'User-Agent': 'Mozilla/5.0'}

    # відправлення запиту за допомогою бібліотеки BeautifulSoup
    soup = BeautifulSoup(requests.get(url, headers=header).content, 'html.parser')

    # отримуємо посилання на зображення та зберігаємо у список
    images = [a['src'] for a in soup.find_all("img", {"src": True})]

    # обмежуємо кількість зображень
    images = images[1:num_images+1]


    # Зберігаємо всі зображення за отриманими посиланнями у цільову директорію
    for i, image in enumerate(images):
        try:
            print(f"{num_lib}.{query}.{i+1}")
            filename = f"{query}_{num_lib}_{i+1}.jpg"
            filepath = os.path.join(save_dir, filename)
            urllib.request.urlretrieve(image, filepath)
        except:
            continue



if __name__ == '__main__':

    # цільова директорія
    data_folder = 'C:/Users/админ/PycharmProjects/PDS2/PDS2_Kofanov/My_project/dataset_parser'

    # Створення цільової директорію з дочірніми директоріями для окремих класів, якщо відсутні
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)
        for folders in fruit_n_vegetables_eng:
            os.makedirs(os.path.join(data_folder, folders))

    # змінна з поточним номером бібліотеки назв зі списку бібліотек
    num_library = 0

    # Застосовуємо функцію скрапера для кожної назви з кожної бібліотеки назв
    for library in library_list:
        num_library += 1
        for n in range(len(library)):
            path_to_folder = os.path.join(data_folder, fruit_n_vegetables_eng[n])
            scrape_images(library[n], 100, path_to_folder, num_library)




