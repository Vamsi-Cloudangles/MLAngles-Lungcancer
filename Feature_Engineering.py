from sklearn import preprocessing
le = preprocessing.LabelEncoder()
from Data_Cleaning import data_cleaning
def feature_engineering():
    dataset = data_cleaning()
    for col in dataset.columns:
        print(col, len(dataset[col].unique()))
    dataset['level'] = le.fit_transform(dataset.level)
    print(dataset.head())
    return dataset
feature_engineering()