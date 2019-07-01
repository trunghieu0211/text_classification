# -*- coding: utf-8 -*-
import os
from random import randint
import codecs


class LoadData:
    def __init__(self, data_path):
        self.data_path = data_path

    def __get_files(self):
        folder_names = os.listdir(self.data_path)
        folder_paths = [self.data_path + folderName + "/" for folderName in os.listdir(self.data_path)]
        files = {}
        for folderPath, folderName in zip(folder_paths, folder_names):
            files[folderName] = [folderPath + fileName for fileName in os.listdir(folderPath)]
        return files

    def get_json(self):
        files = self.__get_files()
        data = []
        for topic in files:
            for file in files[topic]:
                content = codecs.open(file, encoding="utf16", errors="ignore").read()
                data.append({
                    "category": topic,
                    "content": content
                })
        return data
