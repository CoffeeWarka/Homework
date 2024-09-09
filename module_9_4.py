from random import choice

first = 'Мама мыла раму'
second = 'Рамена было мало'
print(list(map(lambda f, s: f == s, first, second)))


def get_advanced_writer(file_name):

    def write_everything(*data_set):
        with open(file_name, 'w',  encoding = 'utf-8') as file:
            for line in data_set:
                file.write(f'{line}\n')
    return write_everything

write = get_advanced_writer('example.txt')
write("Эта строчка", ["А", "это", "уже", "число", 5, "в", "списке"])

class MysticBall:
    def __init__(self, words):
        self.words = words

    def __call__(self):
        return choice(self.words)

first_ball = MysticBall(('Yes', 'No', 'Probably'))
print(first_ball())
print(first_ball())
print(first_ball())
