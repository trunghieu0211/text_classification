from text_preprocessing import *
import text_preprocessing as tp
from gensim import corpora, matutils


class FeatureExtraction:
    def __init__(self, data):
        self.data = data
        self.__save_dictionary()

    def __build_dictionary(self):
        dict_words = []
        for text in self.data:
            words = tp.TextPreprocessing(text["content"]).get_words_feature()
            dict_words.append(words)
        return dict_words

    def __save_dictionary(self):
        dict_words = self.__build_dictionary()
        corpora.Dictionary(dict_words).save_as_text(settings.DICTIONARY_PATH)

    def __load_dictionary(self):
        return corpora.Dictionary.load_from_text(settings.DICTIONARY_PATH)

    def __build_dataset(self):
        self.features = []
        self.labels = []
        for d in self.data:
            self.features.append(self.get_dense(d['content']))
            self.labels.append(d["category"])

    def get_dense(self, text):
        dict = self.__load_dictionary()
        words = tp.TextPreprocessing(text).get_words_feature()

        vec = dict.doc2bow(words)
        dense = list(matutils.corpus2dense([vec], num_terms=len(dict)).T[0])
        return dense

    def get_label_and_data(self):
        self.__build_dataset()
        return self.features, self.labels
