## Fruit Classifier Bot

This library is a set of scripts for the step-by-step creation of a model for the classification of vegetables and fruits based on a convolutional neural network, and for the deployment of the model in the form of a telegram bot.  

Дана бібліотека являє собою набір скриптів для поетапного створення моделі класифікації овочів та фруктів на базі згорткової неронної мережі, а також деплойту моделі у вигляді телеграм бота.

## System requirements for  use library


- **Python version: 3.10 (or later)**
- **RAM: 8 Gb (or more)**
- **System memory: 6 Gb (or more) for installing packages and geting result models**

## Used packages

- **numpy**
- **pandas**
- **tensorflow**
- **keras**
- **cv2**
- **aiogram**

**and other**

## Using scripts and functions

- **scraper_images.py**     
Даний скрипт призначений для скрапінгу бібліотеки зображень з пошукової системи Google.

  
- **clearing_dataset.py**  
Даний скрипт призначений для видалення зображень, що мають однакові хеш-суми.

  
- **modify_image.py**   
Даний скрипт призначений для приведення зображень до одного формату стандартного розміру та їх нормалізацію. 

  
- **dataset_presentation.ipynb**   
Презентаційний скрипт з прикладом зображень кожного класу.

  
- **create_train_test_dirs.py**   
Розбивка датасету на навчальну та тестові вибірки.

  
- **model_ResNet50.py**   
Створення моделі згорткової нейронної мережі.

  
- **use_model.py**   
Тестове використання отриманої моделі для зазначених зображень.

  
- **server_telegram_bot.py**   
Деплойт використання моделі у вигляді телеграм-бота, викладенного на сервері AWS EC2
  


## Using telegram-bot for classification fruit and vegetable

Бот можна знайти за назвою **@Fruit_n_Veget_Class_bot**    

Програма керування ботом та класифікаційна модель завантажені на сервер **AWS EC2**, що дає змогу користуватися телеграм-ботом **24/7**.  

**Для користування програмою доступні наступні дії:**
- команда **/start** викликає повідомлення з описом призначення бота.
- команда **/help** викликає повідомлення з інструкцією по використанню бота.
- на завантаження зображення або фотоповідомлення бот відповідає результатом класифікації об'єкта.
