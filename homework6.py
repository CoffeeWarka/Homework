my_dict = {'Nik': 1995, 'Pavel': 1987, 'Anna': 1980, 'Alex': 1992}
print(my_dict)
print(my_dict['Nik'])
print(my_dict.get('Serg'))
my_dict.update({'Alisa': 1988, 'Lex': 1985})
print(my_dict.pop('Alex'))
print(my_dict)

my_set = {1, 1, 1, 3, 4, 'name', True, 'name', (1, 3, 4), 2.0, (1, 3, 4), 2.0}
print(my_set)
my_set.update([7, 9])
my_set.remove('name')
print(my_set)

