import settings
import json
from pyvi import ViTokenizer


class TextPreprocessing:
    def __init__(self, text):
        self.text = text
        self.__set_stopwords()
        self.__tokenize()
        self.__split_words()

    def __set_stopwords(self):
        with open(settings.STOP_WORDS_FILE) as f:
            self.stopwords = [line.strip().replace(" ", "_") for line in f.readlines()]

    def __tokenize(self):
        return ViTokenizer.tokenize(self.text)

    def __split_words(self):
        text = self.__tokenize()
        return [c.strip(settings.SPECIAL_CHARACTER).lower() for c in text.split()]

    def get_words_feature(self):
        split_words = self.__split_words()
        return [word for word in split_words if word.encode("utf-8") not in self.stopwords]