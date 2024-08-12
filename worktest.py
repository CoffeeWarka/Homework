import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age


class Video:
    def __init__(self, title = '', duration = 0, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self, users = [], videos = [], current_user = User):
        self.users = users
        self.videos = videos
        self.current_user = current_user

    user_log_in = False
    # good_one
    def log_in(self, nickname, password):
        for i in self.users:
            # hash_pass = i.password
            if i.__contains__(nickname) and i.__contains__(password):
                self.current_user = User(self.nickname, self.password, self.age)
                UrTube.user_log_in = True
            return UrTube.user_log_in


    def register(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age
        users = self.users
        for i in users:
            if i.__contains__(nickname):
                print(f'Пользователь {nickname} уже существует.')
        else:
                users = users.append([nickname, hash(password), age])
                UrTube.log_in(self, nickname, hash(password))

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        videos_list = self.videos
        vid = Video
        for i in args:
            if not videos_list.__contains__(i.title):
                videos_list.append(i)

    def get_videos(self, search):
        result = []
        for i in self.videos:
            search_title_low = i.title.casefold()
            if search_title_low.__contains__(search.casefold()):
                result.append(i.title)
        return result
#good_one

    def watch_video(self, video_title):
        if not UrTube.user_log_in:
            print('Войдите в аккаунт, чтобы смотреть видео')
        elif self.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
        else:
            for i in self.videos:
                if video_title.__eq__(i.title):
                    j = 1
                    while j <= i.duration:
                        print(j, end=' ')
                        time.sleep(1)
                        j += 1
                    print('Конец видео')
                else:
                    str(self.current_user)

    def __str__(self):
        return f'{self.current_user}'

        #good_one





if __name__ == 'main':
    user = User()
    video = Video()


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

#
# # Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
#
# # Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
#
# # Проверка входа в другой аккаунт
print(ur.current_user)
#
# # Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
