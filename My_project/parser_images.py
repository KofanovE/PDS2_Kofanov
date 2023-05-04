import os
import urllib.request
from bs4 import BeautifulSoup
import requests


data_folder = 'C:/Users/админ/PycharmProjects/PDS2/PDS2_Kofanov/My_project/dataset_parser'



fruit_n_vegetables_eng = ['avocado', 'orange', 'banana', 'beets', 'grapes', 'grapefruit',
                          'cabbage', 'potatoes', 'kiwi', 'lemon', 'carrot', 'cucumber', 'bell pepper',
                          'champignon', 'tomato', 'green onion', 'onion', 'garlic', 'apples', 'ginger']

fruit_n_vegetables_fr = ['avocat', 'orange', 'banane', 'betterave', 'raisin', 'pamplemousse',
                          'chou', 'pomme de terre', 'kiwi', 'citron', 'carotte', 'concombre', 'poivron',
                          'champignon', 'tomate', 'oignon vert', 'oignon', 'ail', 'pomme', 'gingembre']

fruit_n_vegetables_sp = ['aguacate', 'naranja', 'plátano', 'remolacha', 'uva', 'pomelo',
                          'repollo', 'papa', 'kiwi', 'limón', 'zanahoria', 'pepino', 'pimiento morrón',
                          'hongo', 'tomate', 'cebolla verde', 'cebolla', 'ajo', 'manzana', 'jengibre']

fruit_n_vegetables_shv = ['avokado', 'apelsin', 'banan', 'rödbetor', 'grape', 'grapefrukt',
                          'kål', 'potatis', 'kiwi', 'citron', 'morot', 'gurka', 'peppar',
                          'svamp', 'tomat', 'grön lök', 'lök', 'vitlök', 'äpple', 'ingfära']

fruit_n_vegetables_de = ['Avocado', 'Orange', 'Banane', 'Rüben', 'Trauben', 'Grapefruit',
                         'Kohl', 'Kartoffeln', 'Kiwi', 'Zitrone', 'Karotte', 'Gurke', 'Paprika',
                         'Champignon', 'Tomate', 'Frühlingszwiebel', 'Zwiebel', 'Knoblauch', 'Äpfel', 'Ingwer']

fruit_n_vegetables_it = ['avocado', 'arancia', 'banana', 'barbabietola', 'uva', 'pompelmo', 'cavolo',
                         'patate', 'kiwi', 'limone', 'carota', 'cetriolo', 'peperone', 'champignon',
                         'pomodoro', 'cipolla verde', 'cipolla', 'aglio', 'mele', 'zenzero']

fruit_n_vegetables_tr = ['avokado', 'portakal', 'muz', 'pancar', 'üzüm', 'greyfurt',
                          'lahana', 'patates', 'kivi', 'limon', 'havuç', 'salatalık', 'biber',
                          "mantar", "domates", "yeşil soğan", "soğan", "sarımsak", "elma", "zencefil"]

fruit_n_vegetables_gr = ['αβοκάντο', 'πορτοκάλι', 'μπανάνα', 'παντζάρια', 'σταφύλι', 'γκρέιπφρουτ',
                          'λάχανο', 'πατάτα', 'ακτινίδιο', 'λεμόνι', 'καρότο', 'αγγούρι', 'πιπεριά',
                          'μανιτάρι', 'ντομάτα', 'πράσινο κρεμμύδι', 'κρεμμύδι', 'σκόρδο', 'μήλο', 'τζίντζερ']

fruit_n_vegetables_uk = ['авокадо', 'апельсин', 'банан', 'буряк', 'виноград', 'грейпфрут',
                         'капуста', 'картопля', 'ківі', 'лимон', 'морква', 'огірок', 'перець болгарський',
                         'печериця', 'помідор', 'цибуля зелена', 'цибуля', 'часник', 'яблука', 'імбир']




library_list = [fruit_n_vegetables_eng, fruit_n_vegetables_fr, fruit_n_vegetables_sp, fruit_n_vegetables_shv,
                fruit_n_vegetables_de, fruit_n_vegetables_it, fruit_n_vegetables_tr, fruit_n_vegetables_gr,
                fruit_n_vegetables_uk]

def scrape_images(query, num_images, save_dir, num_lib):
    query = query.split()
    query = '+'.join(query)
    url = "https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"
    header = {'User-Agent': 'Mozilla/5.0'}
    soup = BeautifulSoup(requests.get(url, headers=header).content, 'html.parser')
    images = [a['src'] for a in soup.find_all("img", {"src": True})]
    images = images[1:num_images+1]
    for i, image in enumerate(images):
        try:
            print(f"{num_lib}.{query}.{i+1}")
            filename = f"{query}_{num_lib}_{i+1}.jpg"
            filepath = os.path.join(save_dir, filename)
            urllib.request.urlretrieve(image, filepath)
        except:
            continue


if not os.path.exists(data_folder):
    os.makedirs(data_folder)
    for folders in fruit_n_vegetables_eng:
        os.makedirs(os.path.join(data_folder, folders))

num_library = 0
for library in library_list:
    num_library += 1
    for n in range(len(library)):
        path_to_folder = os.path.join(data_folder, fruit_n_vegetables_eng[n])
        scrape_images(library[n], 100, path_to_folder, num_library)




