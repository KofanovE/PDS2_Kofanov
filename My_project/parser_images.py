import os
import urllib.request
from bs4 import BeautifulSoup
import requests


data_folder = 'C:/Users/админ/PycharmProjects/PDS2/PDS2_Kofanov/My_project/dataset_train'



fruit_n_vegetables_eng = ['avocado', 'orange', 'banana', 'beets', 'grapes', 'grapefruit',
                          'cabbage', 'potatoes', 'kiwi', 'lemon', 'carrot', 'cucumber', 'bell pepper',
                          'champignon', 'tomato', 'green onion', 'onion', 'garlic', 'apples', 'ginger']

fruit_n_vegetables_de = ['Avocado', 'Orange', 'Banane', 'Rüben', 'Trauben', 'Grapefruit',
                         'Kohl', 'Kartoffeln', 'Kiwi', 'Zitrone', 'Karotte', 'Gurke', 'Paprika',
                         'Champignon', 'Tomate', 'Frühlingszwiebel', 'Zwiebel', 'Knoblauch', 'Äpfel', 'Ingwer']

fruit_n_vegetables_it = ['avocado', 'arancia', 'banana', 'barbabietola', 'uva', 'pompelmo', 'cavolo',
                         'patate', 'kiwi', 'limone', 'carota', 'cetriolo', 'peperone', 'champignon',
                         'pomodoro', 'cipolla verde', 'cipolla', 'aglio', 'mele', 'zenzero']

fruit_n_vegetables_uk = ['авокадо', 'апельсин', 'банан', 'буряк', 'виноград', 'грейпфрут',
                         'капуста', 'картопля', 'ківі', 'лимон', 'морква', 'огірок', 'перець болгарський',
                         'печериця', 'помідор', 'цибуля зелена', 'цибуля', 'часник', 'яблука', 'імбир']

library_list = [fruit_n_vegetables_eng, fruit_n_vegetables_de, fruit_n_vegetables_it,  fruit_n_vegetables_uk]

def scrape_images(query, num_images, save_dir):
    query = query.split()
    query = '+'.join(query)
    url = "https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"
    header = {'User-Agent': 'Mozilla/5.0'}
    soup = BeautifulSoup(requests.get(url, headers=header).content, 'html.parser')
    images = [a['src'] for a in soup.find_all("img", {"src": True})]
    images = images[1:num_images+1]
    for i, image in enumerate(images):
        try:
            filename = f"{query}{i+1}.jpg"
            filepath = os.path.join(save_dir, filename)
            urllib.request.urlretrieve(image, filepath)
        except:
            continue


if not os.path.exists(data_folder):
    os.makedirs(data_folder)
    for folders in fruit_n_vegetables_eng:
        os.makedirs(os.path.join(data_folder, folders))

for library in library_list:
    for n in range(len(library)):
        path_to_folder = os.path.join(data_folder, fruit_n_vegetables_eng[n])
        scrape_images(library[n], 1, path_to_folder)




