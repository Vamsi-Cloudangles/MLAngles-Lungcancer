from Feature_Engineering import feature_engineering

def feature_selection():
    dataset = feature_engineering()
    # Drop the unnecesssary columns
    dataset = dataset.drop(["patient_id", "index"], axis =1)    
    print(dataset.head())
    dataset.to_csv('cleaned_dataset.csv")
    return dataset

feature_selection()
