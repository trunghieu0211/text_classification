from feature_extraction import *
import feature_extraction as fe
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import classification_report


class TextClassification:
    def __init__(self, features_train, labels_train, features_test, labels_test):
        self.features_train = features_train
        self.labels_train = labels_train
        self.features_test = features_test
        self.labels_test = labels_test

    def training(self):
        clf = BernoulliNB()
        clf.fit(self.features_train, self.labels_train)

        # print(len(self.labels_test))
        print(self.features_test)
        # y_true, y_pred = self.labels_test, clf.predict(self.features_test)
        # print(classification_report(y_true, y_pred))

    def save_model(self):
        pass


if __name__ == "__main__":
    with open(settings.DATA_TRAIN_JSON) as f:
        data_train = json.load(f)
    with open(settings.DATA_TEST_JSON) as f:
        data_test = json.load(f)

    features_train, labels_train = fe.FeatureExtraction(data_train).get_label_and_data()
    features_test, labels_test = fe.FeatureExtraction(data_test).get_label_and_data()

    TextClassification(features_train, labels_train, features_test, labels_test).training()


