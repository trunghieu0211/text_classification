from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from text_preprocessing import TextPreprocessing
import settings


class NaiveBayesModel(object):
    def __init__(self):
        self.clf = self.__init_pipeline()

    def __stopwords(self):
          with open(settings.STOP_WORDS_FILE) as f:
              stopwords = [line.strip().replace(" ", "_") for line in f.readlines()]
          return stopwords

    def __init_pipeline(self):
        pipe_line = Pipeline([
            ("text_preprocessing", TextPreprocessing()),
            ("vect", CountVectorizer(self.__stopwords())),
            ("tfidf", TfidfTransformer()),
            ("clf", MultinomialNB())
        ])

        return pipe_line
