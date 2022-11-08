import re

class TextProcessor:

    def __init__(self):
        self.__punctuation = '[,.:;!?-]'
        self.__bool_punctuation = None


    def get_clean_string(self, string):
        clean_string = re.sub(self.__punctuation, '', string)
        return clean_string

    def __is_punctuation(self, symb):
        self.__bool_punctuation = symb in self.__punctuation
        return self.__bool_punctuation




corector = TextProcessor()
print(corector.get_clean_string('Тестовий рядок: авівлраі:овра;вла,ваів.ваі-ваів!ва?ва'))



class TextLoader:

    def __init__(self):
        self.text_processor = TextProcessor()
        self.__clean_string = None


    def set_clean_text(self, s):
        self.__clean_string = self.text_processor.get_clean_string(s)


    def modern_clean_string(self):
        return (f'\nОчищенний текст: \n{self.__clean_string}')



corector_2 = TextLoader()
corector_2.set_clean_text('Інший тестовий рядок: авівлраі:овра;вла,ваів.ваі-ваів!ва?ва')
print(corector_2.modern_clean_string())



class DataInterface():

    def __init__(self):
        self.__text_loader = TextLoader()

    def process_text(self, list):
        for i in list:
            print(self.__text_loader.text_processor.get_clean_string(i))


print('\n')
s = ['Рядок: перший', 'Рядок: другий', 'Рядок: третій' ]
corector_3 = DataInterface()
corector_3.process_text(s)