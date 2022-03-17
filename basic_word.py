class BasicWord:

    def __init__(self, word, sub_words):
        self.word = word
        self.sub_words = sub_words

    def is_correct(self, condidate):
        return condidate.lower() in self.sub_words

    def get_words(self):
        return len(self.sub_words)

    def __repr__(self):
        return f"{self.word} содержит {len(self.sub_words)}слов"



