class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


class Video:
    def __init__(self, title, duration, time_now, adult_mod):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mod = adult_mod
        time_now = 0
        adult_mod = False


class UrTube:
    def __init__(self):
        users = []
        videos = []
        current_user = User

    def log_in(self, nickname, password):
        password = hash(password)
        if nickname and password in self.current_user:
            self.current_user = User

    def register(self, nickname, password, age):
        nickname = input()
        password = input()
        age = input()
        if nickname in self.users:
            print(f'Пользователь {nickname} уже существует.')
        else:
            self.users = self.users.append(User)

ur = UrTube()
