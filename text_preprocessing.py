from pyvi import ViTokenizer
from sklearn.base import TransformerMixin, BaseEstimator
import re


class TextPreprocessing(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def tokenize(self, text):
        return ViTokenizer.tokenize(text)

    def split_words(self, text):
        text = self.tokenize(text)
        text = re.sub(r'\W', " ", text)
        text = re.sub(r'\s+[a-zA-Z]\s+', " ", text)
        text = re.sub('[0-9]', " ", text)
        text = re.sub("|".join(["hi", "hello_ban"]), "", text)
        text = re.sub(" +", " ", text)
        return text

    def fit(self, *_):
        return self

    def transform(self, X, y=None, **fit_params):
        result = X.apply(lambda text: self.split_words(text))
        return result

