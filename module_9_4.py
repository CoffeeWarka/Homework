first = 'Мама мыла раму'
second = 'Рамена было мало'
print(list(map(lambda f, s: f == s, first, second)))

first = 'Мама мыла раму'
second = 'Рамена было мало'
print(list(map(lambda f, s: f == s, first, second)))

def get_advanced_writer(file_name):

    def write_everything(*data_set):
        with open(file_name, 'w',  encoding = 'utf-8') as file:
            file.write(f'{data_set}\n')
    return write_everything

write = get_advanced_writer('example.txt')
write("Эта строчка", ["А", "это", "уже", "число", 5, "в", "списке"])
