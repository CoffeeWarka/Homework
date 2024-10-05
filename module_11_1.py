import requests
import pandas

# pandas - file check
# numpy - massive
# matplotlib - visual data
# pillow - images

# requests
# def ya_search(search):
#     query = {'q': search}
#     req = requests.get('https://ya.ru/?utm_referrer=https%3A%2F%2Fyandex.ru%2F', params = query)
#     print(req.url)
#
#
# def alive(site_adress):
#     response = requests.get(site_adress)
#     if response.status_code == 200:
#         print("It's Alive!")
#     elif response.status_code == 404:
#         print("Nope... He's dead.")
#
# ya_search('urban')
# alive('https://ru.wikipedia.org/wiki/Заглавная_страница')

# pandas

# pandas_example = pandas.Series([6, -1111, -128, 48])
# print(pandas_example)
#
#
#
sheet = {'Продукт':['Горбуша','Свинина', 'Курица', 'Куриное яйцо'], 'Ккал':[151, 484, 161, 153]}
df = pandas.DataFrame(sheet)
# print(df)
# print(df.describe())
# print(df.sort_values('Ккал', ascending=False).head())

def sheet_plus(sheet_concat, products, kcals):
    kcals_index = 0
    if isinstance(kcals, int) and isinstance(products, str):
        products = [products]
        kcals = [kcals]
    for product in products:
        kcal = kcals[kcals_index]
        new_product = {'Продукт': product, 'Ккал': kcal}
        df_plus = pandas.DataFrame([new_product])
        sheet_concat = pandas.concat([sheet_concat, df_plus], ignore_index=True)
        kcals_index+=1
    return sheet_concat



sp = sheet_plus(df,'Банан', 98)
print(sp)