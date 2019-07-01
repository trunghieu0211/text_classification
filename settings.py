import os

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
DATA_TRAIN_PATH = os.path.join(DIR_PATH, 'data/10_category/train/')
DATA_TEST_PATH = os.path.join(DIR_PATH, 'data/10_category/test/')
DATA_TRAIN_JSON = os.path.join(DIR_PATH, 'data_train.json')
DATA_TEST_JSON = os.path.join(DIR_PATH, 'data_test.json')
STOP_WORDS_FILE = os.path.join(DIR_PATH, 'vietnamese-stopwords.txt')

