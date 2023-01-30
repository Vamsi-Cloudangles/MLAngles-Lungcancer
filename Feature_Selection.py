from Feature_Engineering import feature_engineering
import pandas as pd

def feature_selection():
    dataset = feature_engineering()
    # Drop the unnecesssary columns
    dataset = dataset.drop(["patient_id"], axis =1)    
    print(dataset.head())
    return dataset

feature_selection()