from feature_extraction import NaiveBayesModel
import json
import settings
import pandas as pd
from sklearn.metrics import accuracy_score
import joblib


class TextClassification(object):
    def __init__(self, data_train, data_test):
        self.data_train = data_train
        self.data_test = data_test

    def build_model(self):
        df_train = pd.DataFrame(self.data_train)
        model = NaiveBayesModel()
        model.clf.fit(df_train.content, df_train.category)
        return model.clf

    def save_model(self, file_name):
        clf = self.build_model()
        joblib.dump(clf, file_name)

    def eval_model(self):
        clf = self.build_model()
        df_test = pd.DataFrame(self.data_test)
        y_true, y_predict = df_test.category, clf.predict(df_test.content)
        print("Accuracy: %.2f%%" % (accuracy_score(y_true, y_predict)*100))


class Predict:
    def __init__(self, file_name):
        self.file_name = file_name

    def load_model(self):
        return joblib.load(self.file_name)

    def predict(self, data_predict):
        model = self.load_model()
        df_predict = pd.DataFrame(data_predict)
        return model.predict(df_predict.content)


if __name__ == '__main__':
    with open(settings.DATA_TRAIN_JSON) as f:
        data_train = json.load(f)
    with open(settings.DATA_TEST_JSON) as f:
        data_test = json.load(f)

    # tcp = TextClassification(data_train, data_test)
    # tcp.eval_model()
    # tcp.save_model('text_classification.pkl')
