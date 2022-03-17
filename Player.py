class Player:

    def __init__(self, name):
        self.name = name
        self.used_words = []


    def count_words(self):
        return len(self.used_words)

    def add_word(self, newword):
        self.used_words.append(newword)

    def is_used(self, word):
        return word in self.used_words

    def __repr__(self):
        return f"{self.name} угадал слова {', '.join(self.used_words)}"