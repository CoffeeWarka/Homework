team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 18015.2
team2_time = 17099
challenge_result = ''
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники данных!'
else:
    challenge_result = 'Ничья!'

tasks_total = score_1 + score_2
time_avg_ = (team1_time + team2_time)/tasks_total
time_avg = (f'{time_avg_:.1f}')
print('В команде Мастера кода участников: %s !' % team1_num)
print('Итого сегодня в командах участников %s и %s !' % (team1_num, team2_num))
print("Команда Волшебники данных рашила задач: {} !".format(score_2))
print('Волшебники данных решили задачи за {} с !'.format(team1_time))
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {challenge_result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')

import os
import time

directory = os.getcwd()
for root, dirs, files in os.walk(directory):
for file in files:
filepath = os.path.join(directory, file)
filetime = os.path.getmtime(file)
formatted_time = time.strftime('%d.%m.%Y. %H.%M', time.localtime(filetime))
filesize = os.path.getsize(file)
parent_dir = os.path.dirname(directory)
print(f'Обнаружен файл: {file}, Путь: {filepath}, '
f'Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
