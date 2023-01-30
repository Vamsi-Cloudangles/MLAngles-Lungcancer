import pandas as pd
from sklearn import preprocessing
le = preprocessing.LabelEncoder()
from Data_Analysis import data_analysis
def data_cleaning():
    dataset = data_analysis()
    dataset =  dataset.rename(columns=str.lower)
    for col in dataset.columns:
        dataset = dataset.rename(columns = {col: col.replace(" ", "_")})
    print(dataset.columns)
    return dataset
data_cleaning()