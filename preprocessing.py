import pandas as pd

def load_data():
    data = pd.read_csv("job_dataset.csv")
    return data

def clean_data(data):

    data.columns = data.columns.str.strip().str.lower()

    data = data.drop_duplicates()

    data = data.fillna("Unknown")

    data['posted_date'] = pd.to_datetime(data['posted_date'],format='%d-%m-%Y')

    return data
