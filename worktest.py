class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


class Video:
    def __init__(self, title, duration, time_now = 0, adult_mod = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mod = adult_mod


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = User

    def log_in(self, nickname, password):
        log_in = False
        password = hash(password)
        if nickname and password in self.users:
            self.current_user = User
            log_in = True
        return log_in

    def register(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age
        if self.users.__contains__(self.nickname):
            print(f'Пользователь {nickname} уже существует.')
        else:
            self.users = self.users.append(User)

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        if args not in self.videos:
            self.videos = self.videos.append(Video)

    def get_videos(self, search):
        videos_list = []
        search_low = search.casefold()
        for i in self.videos:
            if i.title == search_low:
                videos_list = videos_list.append(i.title)

    def watch_video(self):
        if not self.log_in:
            print('Войдите в аккаунт, чтобы смотреть видео')




ur = UrTube()
ur.register("Nik", 'ololo', 29)
ur.register('Nik', 'lol', 20)
