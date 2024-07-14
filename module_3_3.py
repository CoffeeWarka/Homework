def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params()
print_params(3, 'argu', False)
print_params(210)
print_params(False)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [1, True, 'test']
values_dict = {'a': 3, 'b': 'dictionary', 'c': False}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [True, 'still']
print_params(*values_list_2, 42)