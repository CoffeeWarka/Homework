import io
def custom_write(file_name, strings):
    file = open(file_name, 'w+', encoding='utf-8')
    string_position = {}
    line = 1
    for i in strings:
        string_position[line, file.tell()] = i
        file.write(f'{i}\n')
        line += 1
    return string_position

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
result = custom_write('text.txt', info)
for elem in result.items():
    print(elem)
