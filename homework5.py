immutable_var = 1, 'word', ['hand', 'leg'], False
print(immutable_var)

# я не могу изменить элементы кортежа, так как это неизменяемый объект,
# максимум, что я могу - это изменить значение внутри списка, который находится внутри кортежа (['hand', 'leg']),
# что никак не повлияет на кортеж в целом.

mutable_list = [2, 'sentence', ['head', 'eye'], True]
mutable_list = [3, 'story', ['hat', 'glasses'], False]
print(mutable_list)