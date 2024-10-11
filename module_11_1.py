import requests
import pandas
import numpy


# requests

# vk_head = requests.get('https://vk.com')
# print(vk_head.headers)


# def ya_search(search):
#     query = {'q': search}
#     req = requests.get('https://ya.ru/?utm_referrer=https%3A%2F%2Fyandex.ru%2F', params = query)
#     print(req.url)
#
#
# def alive(site_address):
#     response = requests.get(site_address)
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
# sheet = {'Продукт':['Горбуша','Свинина', 'Курица', 'Куриное яйцо'], 'Ккал':[151, 484, 161, 153]}
# df = pandas.DataFrame(sheet)
# print(df)
# print(df.describe())
# print(df.sort_values('Ккал', ascending=True).head())

# def sheet_plus(sheet_concat, products, kcals):
#     kcals_index = 0
#     if isinstance(kcals, int) and isinstance(products, str):
#         products = [products]
#         kcals = [kcals]
#     for product in products:
#         kcal = kcals[kcals_index]
#         new_product = {'Продукт': product, 'Ккал': kcal}
#         df_plus = pandas.DataFrame([new_product])
#         sheet_concat = pandas.concat([sheet_concat, df_plus], ignore_index=True)
#         kcals_index+=1
#     return sheet_concat
#
#
#
# sp = sheet_plus(df,'Банан', 98)
# print(sp)

#numpy

# array0 = numpy.array([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
# array1 = numpy.array([0, 2, 3, 1])
# array2 = numpy.array([0, 2, 3, 1])
# array_x = numpy.random.randint(0, 10, size=(5, 5))


# print(array0)
# print(numpy.array_equal(array1, array2))
# print(array0.shape, array1.shape, array2.shape)
# print(array_x)

# def matrix_upgrade(size_and_max_value):
#     matrix_line = size_and_max_value
#     matrix = numpy.zeros((size_and_max_value, matrix_line))
#     matrix += numpy.arange(size_and_max_value)
#     print(matrix)
#
# matrix_upgrade(5)

