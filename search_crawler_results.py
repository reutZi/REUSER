import pandas as pd

def extract_data_from_file(file_path, keyword=None):
    df = pd.read_csv(file_path)
    if keyword is None or not keyword:
        return df
    index = df["name"].str.contains(keyword)
    products = df[index]
    return products

if __name__ == "__main__":
    filename = "data.csv"
    keyword = ""
    print(extract_data_from_file(filename, keyword))