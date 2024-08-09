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
    def __init__(self, users = [], videos = [], current_user = User):
        self.users = users
        self.videos = videos
        self.current_user = current_user



    def log_in(self, nickname, password):
        log_in = False
        users = ur.users
        cur_user = ur.current_user
        for i in users:
            if i.__contains__(nickname) and i.__contains__(hash(password)):
                cur_user = User
                log_in = True
                return log_in

        # good_one
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


    # good_one



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



if __name__ == 'main':
    user = User()
    video = Video()
# ur.register("Nik", 'ololo', 29)
# ur.register('Nik', 'lol', 20)

ur = UrTube()
ur.register('Nik', 'nlol', 29)
ur.register('Kik', 'klol', 29)
# ur.register('Kik', 'lol', 29)
