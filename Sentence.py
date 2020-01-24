from string import punctuation
from re import split


class Sentence:

    def process_word(self, word):
        return word.translate(self.table).lower()

    def __init__(self, raw_sentence):
        self.text = raw_sentence
        self.table = str.maketrans('', '', punctuation)
        self.words = list(map(lambda word: self.process_word(word), split(r'\W+', self.text)))
        self.tokens = list(dict.fromkeys(self.words))
