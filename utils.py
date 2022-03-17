import requests
import random
from basic_word import BasicWord


def load_random_word():
    words_list = requests.get('https://jsonkeeper.com/b/F8CS')
    words = words_list.json()
    random_words = random.choice(words)
    return BasicWord(random_words["word"], random_words["subwords"])
