import pandas as pd

class Product:
    def __init__(self, name, link, image):
        self.name = name
        self.link = link
        self.image = image

def extract_data_from_excel(file_path, keyword=None):
    df = pd.read_excel(file_path)
    products = []
    for index, row in df.iterrows():
        name = row['Name']
        link = row['Link']
        image = row['Image']
        if keyword and keyword.lower() not in name.lower():
            continue
        product = Product(name, link, image)
        products.append(product)
    return products

def extract_line_from_excel(file_path, line_index):
    df = pd.read_excel(file_path)
    if line_index < len(df):
        row = df.iloc[line_index]
        name = row['Name']
        link = row['Link']
        image = row['Image']
        product = Product(name, link, image)
        return product
    else:
        return None

def enter_product_to_excel(file_path, product):
    df = pd.read_excel(file_path)
    new_row = pd.DataFrame({'Name': product.name, 'Link': product.link, 'Image': product.image}, index=[0])
    df = df.append(new_row, ignore_index=True)
    df.to_excel(file_path, index=False)

def delete_product_from_excel(file_path, product_name):
    df = pd.read_excel(file_path)
    df = df[df['Name'] != product_name]
    df.to_excel(file_path, index=False)
