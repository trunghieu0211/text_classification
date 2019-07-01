# -*- coding: utf-8 -*-
import settings
import load_data
import json


class DumpData:
    def __init__(self, data_path, data):
        self.data_path = data_path
        self.data = data

    def dump_json(self):
        with open(self.data_path, 'w') as f:
            json.dump(self.data, f)


if __name__ == "__main__":
    json_train = load_data.LoadData(settings.DATA_TRAIN_PATH).get_json()
    DumpData(settings.DATA_TRAIN_JSON, json_train).dump_json()
    json_test = load_data.LoadData(settings.DATA_TEST_PATH).get_json()
    DumpData(settings.DATA_TEST_JSON, json_test).dump_json()
