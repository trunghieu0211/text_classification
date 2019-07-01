# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np


train_data = []
train_data.append({"feature": u"Hôm nay trời đẹp không ?", "target": "hoi_thoi_tiet"})
train_data.append({"feature": u"Hôm nay thời tiết thế nào ?", "target": "hoi_thoi_tiet"})
train_data.append({"feature": u"Hôm nay mưa không ?", "target": "hoi_thoi_tiet"})
train_data.append({"feature": u"Chào em gái", "target": "chao_hoi"})
train_data.append({"feature": u"Chào bạn", "target": "chao_hoi"})
train_data.append({"feature": u"Hello bạn", "target": "chao_hoi"})
train_data.append({"feature": u"Hi kimi", "target": "chao_hoi"})
train_data.append({"feature": u"Hi em", "target": "chao_hoi"})
df_train = pd.DataFrame(train_data)

print(df_train.feature.__class__)