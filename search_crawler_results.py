import pandas as pd
# #
# # def extract_data_from_file(file_path, keyword=None):
# #     df = pd.read_csv(file_path)
# #     if keyword is None or not keyword:
# #         return df
# #     index = df["name"].str.contains(keyword)
# #     products = df[index]
# #     return products
# #
# # if __name__ == "__main__":
# #     filename = "data.csv"
# #     keyword = ""
# #     print(extract_data_from_file(filename, keyword))
#
# import pandas as pd
#
# class Product:
#     def __init__(self, name, link, image, date, price, phone, address ):
#         self.name = name
#         self.link = link
#         self.image = image
#         self.date = date
#         self.price = price
#         self.phone = phone
#         self.address = address
#
# def extract_data_from_excel(file_path, keyword=None):
#     df = pd.read_excel(file_path)
#     products = []
#     for index, row in df.iterrows():
#         name = row['name']
#         image = row['image URL']
#         link = row['link URL']
#         date = row['date']
#         price = row['price']
#         phone = row['owner phone']
#         address = row['owner address']
#         if keyword and keyword.lower() not in name.lower():
#             continue
#         product = Product(name, link, image, date, price, phone, address)
#         products.append(product)
#     return products
#


lists = [['ספה', 'https://img.yad2.co.il/Pic/202102/21/3_2/o/y2_1_06653_20210221150235.jpeg',
          'https://www.yad2.co.il/products/furniture?category=2&item=12&open-item-id=fbc4m8&categoryId=3&view=light-box',
          '08.06.2023', 1390, 533900098, 'רעננה', 'יד שניה'],['ספה', 'https://www.komo.co.il/api/pictures/showPic.api.asp?picSize=b&picNum=11993713&luachNum=3',
    'https://www.komo.co.il/code/y2/?groupNum=15&categoryNum=94&subCategoryNum=767#popW', '06.06.2023', 1500, 505442590,
    'באר יעקב', 'קומו'],
         ['ספה', 'https://uploads.homeless.co.il/yad2/202302/nvFile4412889.jpg',
    'https://www.homeless.co.il/yad2/viewad,1031916.aspx', 'אין', 4500, 523056940, 'דימונה', 'הומלס'],
         ['ספה', 'https://img.yad2.co.il/Pic/202301/04/3_0/o/y2_1_06588_20230104101053.jpeg?l=5&c=1&w=1024&h=768',
    'https://www.yad2.co.il/products/furniture?category=2&item=12&open-item-id=l1gnc7mt&categoryId=3&view=light-box',
    '08.06.2023', 2400, 5338996781, 'נווה', 'יד שניה'],
         [
             'ספה', 'https://www.agora.co.il/showPhoto.asp?id=2760408', 'https://www.agora.co.il/cache/2023-06/2760408_o.asp',
             '05.06.2023', 0, 545524737, 'רמת גן', 'אגורה'],
         ['ספה', 'https://cdn.agora.co.il/deals_images/2023-06/2758805.jpg?v=1',
    'https://www.agora.co.il/cache/2023-06/2758805_o.asp', '03.06.2023', 0, 527907263, 'תל אביב', 'אגורה'],
         ['ספה', 'https://uploads.homeless.co.il/yad2/202305/nvFile4473148.jpeg',
    'https://www.homeless.co.il/yad2/inumber3=45$$inumber4=104', 'אין', 1000, 507916837, 'עפולה', 'הומלס'],
         ['ספה', 'https://www.komo.co.il/api/pictures/showPic.api.asp?picSize=b&picNum=11979597&luachNum=3',
    'https://www.komo.co.il/code/y2/details/?modaaNum=3287950', '07.06.2023', 1850, 527909263, 'ראשון לציון', 'קומו'],
         ['שולחן', 'https://img.yad2.co.il/Pic/202102/24/3_2/o/y2_1_07652_20210224170204.jpeg?l=5&c=1&w=1024&h=768',
    'https://www.yad2.co.il/products/furniture?category=2&item=14&open-item-id=na9w4i&categoryId=3&view=light-box',
    '08.06.2023', 399, 722333100, 'ראשון לציון', 'יד שניה'],
         ['שולחן', 'https://img.yad2.co.il/Pic/202305/24/3_0/o/y2_1_03160_20230524173525.jpeg?l=5&c=1&w=1024&h=768',
    'https://www.yad2.co.il/products/furniture?category=2&item=14&open-item-id=heg0vsid&categoryId=3&view=light-box',
    '08.06.2023', 650, 544209997, 'חיפה', 'יד שניה'],
         ['שולחן', 'https://cdn.agora.co.il/deals_images/2023-06/2761099.jpg?v=1',
    'https://www.agora.co.il/toGet.asp?dealType=1&iseek=%D7%A9%D7%95%D7%9C%D7%97%D7%9F', '01.06.2023', 0, 589976882,
    'ירושלים', 'אגורה'],
         ['שולחן', 'https://cdn.agora.co.il/deals_images/2023-06/2760927.jpg?v=1',
    'https://www.agora.co.il/cache/2023-06/2760927_o.asp', '08.06.2023', 0, 587958663, 'ירושלים', 'אגורה'],
         ['שולחן', 'https://uploads.homeless.co.il/yad2/202107/nvFile4048946.jpg',
    'https://www.homeless.co.il/yad2/inumber3=45$$inumber4=107', '07.05.2023', 1, 524498775, 'תל אביב', 'הומלס'],
         ['שולחן', 'https://uploads.homeless.co.il/yad2/202303/550/nvFile4419550.jpg',
    'https://www.homeless.co.il/yad2/inumber3=45$$inumber4=107', '03.06.2023', 400, 535687495, 'תל אביב', 'הומלס'],
         ['שולחן', 'https://www.komo.co.il/api/pictures/showPic.api.asp?picSize=b&picNum=11913486&luachNum=3',
    'https://www.komo.co.il/code/y2/?groupNum=15&categoryNum=94&subCategoryNum=768#popW', '08.06.2023', 70, 508879584,
    'הוד השרון', 'קומו'],
         ['שולחן', 'https://www.komo.co.il/api/pictures/showPic.api.asp?picSize=b&picNum=11988626&luachNum=3',
    'https://www.komo.co.il/code/y2/?groupNum=15&categoryNum=94&subCategoryNum=768#popW', '08.06.2023', 350, 598687489,
    'רמת גן', 'קומו'],
         ['שולחן', 'https://www.komo.co.il/api/pictures/showPic.api.asp?picSize=b&picNum=11928649&luachNum=3',
    'https://www.komo.co.il/code/y2/?groupNum=15&categoryNum=94&subCategoryNum=768#popW', '07.06.2023', 350, 552893124,
    'רמת גן', 'קומו'],
         ['שולחן', 'https://img.yad2.co.il/Pic/202305/24/3_0/o/y2_1_03160_20230524173525.jpeg?l=5&c=1&w=1024&h=768',
    'https://www.yad2.co.il/products/furniture?category=2&item=14&open-item-id=heg0vsid&categoryId=3&view=light-box',
    '08.06.2023', 650, 575477785, 'חיפה', 'יד שניה'],
         ['שולחן', 'https://cdn.agora.co.il/deals_images/2023-06/2760927.jpg?v=1',
    'https://www.agora.co.il/cache/2023-06/2760927_o.asp', '08.06.2023', 0, 554061456, 'ירושלים', 'אגורה'],
         ['שולחן', 'https://cdn.agora.co.il/deals_images/2023-06/2760896.jpg?v=1',
    'https://www.agora.co.il/cache/2023-06/2760896_o.asp', '08.06.2023', 0, 554645741, 'בני ברק', 'אגורה'],
         ['כסאות', 'https://cdn.agora.co.il/deals_images/2023-06/2760486.jpg?v=1',
    'https://www.agora.co.il/cache/2023-06/2760486_o.asp', '05.06.2023', 0, 555229123, 'חיפה', 'אגורה'],
         ['כסאות', 'https://www.komo.co.il/api/pictures/showPic.api.asp?picSize=b&picNum=11926001&luachNum=3',
    'https://www.komo.co.il/code/y2/?groupNum=15&categoryNum=94&subCategoryNum=775#popW', '08.06.2023', 150, 548759866,
    'קריות', 'קומו'],
         ['כסאות', 'https://www.komo.co.il/api/pictures/showPic.api.asp?picSize=b&picNum=6650605&luachNum=3',
    'https://www.komo.co.il/code/y2/?groupNum=15&categoryNum=94&subCategoryNum=775#popW', '08.06.2023', 200, 586522147,
    'פתח תקווה', 'קומו'],
         ['כסאות', 'https://img.yad2.co.il/Pic/202306/01/3_0/o/y2_1_02369_20230601210206.jpeg',
    'https://www.yad2.co.il/products/furniture?category=2&item=166&open-item-id=5yxuj3vu&categoryId=3&view=light-box',
    '08.06.2023', 350, 548876559, 'בני ברק', 'יד שניה'],
         ['כסאות', 'https://img.yad2.co.il/Pic/202305/30/3_0/o/y2_1_09402_20230530192451.jpeg',
    'https://www.yad2.co.il/products/furniture?category=2&item=166&open-item-id=1xufjdja&categoryId=3&view=light-box',
    '08.06.2023', 150, 548123059, 'רחובות', 'יד שניה'],
         ['כסאות', 'https://uploads.homeless.co.il/yad2/202305/nvFile4478199.jpeg',
    'https://www.homeless.co.il/yad2/inumber3=45$$inumber4=109', '08.06.2023', 800, 548759622, 'עפולה', 'הומלס'],
         ['כסאות', 'https://uploads.homeless.co.il/yad2/202306/nvFile4493106.jpg',
    'https://www.homeless.co.il/yad2/inumber3=45$$inumber4=109', '08.06.2023', 1500, 524685985, 'יד אליהו', 'הומלס'],
         ['כסאות', 'https://uploads.homeless.co.il/yad2/202301/nvFile4391720.jpg',
    'https://www.homeless.co.il/yad2/inumber3=45$$inumber4=109', '08.06.2023', 100, 547822669, 'רחובות', 'הומלס'],
         ['ארון', 'https://uploads.homeless.co.il/yad2/202306/nvFile4492517.jpeg',
    'https://www.homeless.co.il/yad2/inumber3=45$$inumber4=101', '08.06.2023', 1000, 646512456, 'תל אביב', 'הומלס'],
         ['ארון', 'https://www.komo.co.il/api/pictures/showPic.api.asp?picSize=b&picNum=11930222&luachNum=3',
    'https://www.komo.co.il/code/y2/?groupNum=15&categoryNum=94&subCategoryNum=766#popW', '07.06.2023', 450, 587454354,
    'שרון', 'קומו'],
         ['ארון', 'https://www.komo.co.il/api/pictures/showPic.api.asp?picSize=b&picNum=11981187&luachNum=3',
    'https://www.komo.co.il/code/y2/?groupNum=15&categoryNum=94&subCategoryNum=766#popW', '07.06.2023', 1000, 542145888,
    'ראשון לציון', 'קומו'],
         ['ארון', 'https://img.yad2.co.il/Pic/202004/26/3_2/o/o3_2_1_05235_20200426140457.jpg?l=5&c=1&w=1024&h=768',
    'https://www.yad2.co.il/products/furniture?category=2&item=171&open-item-id=nsojik&categoryId=3&view=light-box',
    '08.06.2023', 1500, 587459869, 'חולון', 'יד שניה'],
         ['ארון', 'https://img.yad2.co.il/Pic/202304/15/3_2/o/y2_1_03432_20230415234034.jpeg',
    'https://www.yad2.co.il/products/furniture?category=2&item=171&open-item-id=oezcpn0m&categoryId=3&view=light-box',
    '08.06.2023', 1340, 589658455, 'בני ברק', 'יד שניה'],
         [
             'ארון', 'blob:https://web.whatsapp.com/87961fe8-0c65-4244-b6c2-3683ebc97eb3', '', '08.06.2023', 0, 585658485,
             'בית אל', 'ווטצאפ'],
         [
             'ארון', 'blob:https://web.whatsapp.com/4a7c7479-be7b-4007-b24e-25e56f3ea57b', '', '08.06.2023', 0, 547859696,
             'בית אל', 'ווטצאפ'],
         ['ארון', 'https://uploads.homeless.co.il/yad2/202306/nvFile4489029.jpg',
    'https://www.homeless.co.il/yad2/inumber3=45$$inumber4=101', '08.06.2023', 1000, 587465644, 'אשדוד', 'הומלס'],
         ['ארון', 'https://img.yad2.co.il/Pic/202305/23/3_0/o/y2_1_07820_20230523192449.jpeg?l=5&c=1&w=1024&h=768',
    'https://www.yad2.co.il/products/furniture?category=2&item=171&open-item-id=7o7xcpov&categoryId=3&view=light-box',
    '08.06.2023', 4000, 884564566, 'רעננה', 'יד שניה'],
         ['ארון',
    'https://scontent.fsdv1-2.fna.fbcdn.net/v/t39.30808-6/352039281_178687751838505_9092688897688202189_n.jpg?_nc_cat=106&ccb=1-7&_nc_sid=5cd70e&_nc_ohc=OXmvj1FS_S0AX_rbBaN&_nc_ht=scontent.fsdv1-2.fna&oh=00_AfA8j2YMPxMAE2LDWFKdlKeKIwQOov1NGOTRU25QvKNU7w&oe=6486055E',
    'https://www.facebook.com/groups/209010349222671', '08.06.2023', 0, 547859656, 'ראשון לציון', 'פייסבוק']]


def read_excel_to_list(file_path, keyword):

        list=[]
        for item in lists:
            if keyword in item[0]:
                list.append(item)
        return list

# def read_excel_to_list(file_path):
#    df = pd.read_csv(file_path)
#    if keyword is None or not keyword:
#         return df
#    index = df["name"].str.contains(keyword)
#     products = df[index]
#     return products

