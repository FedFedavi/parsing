import requests
from bs4 import BeautifulSoup
from googletrans import Translator



def get_words():
    url = "https://randomword.com/"
    translator = Translator()
    try:
        responce = requests.get(url)
        soup = BeautifulSoup(responce.content, "html.parser")
        english_words = soup.find("div", id="random_word").text.strip()
        ru_words = translator.translate(english_words, dest="ru").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()
        ru_word_definition = translator.translate(word_definition, dest="ru").text.strip()

        return {
            "ru_words": ru_words,
            "ru_word_definition": ru_word_definition
        }
    except:
        print("Произошла ошибка")

def word_game():
    print("Добро пожаловать в игру")

    while True:
        word_dict = get_words()
        word = word_dict.get("ru_words")
        word_definition = word_dict.get("ru_word_definition")

        print(f"Значение слова - {word_definition}")
        user = input("Что это за слово ?")

        if user == word:
            print("Ты прав, чувак!")
        else:
            print(f"Неа, это было {word}")

        play_again = input("Хотите сыграть еще? y/n")
        if play_again != "y":
            print("Спасибо за игру")
            break

word_game()