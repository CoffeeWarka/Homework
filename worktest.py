class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


class Video:
    def __init__(self, title = '', duration = 0, time_now = 0, adult_mod = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mod = adult_mod


class UrTube:
    def __init__(self, users = [], videos = [], current_user = User):
        self.users = users
        self.videos = videos
        self.current_user = current_user

    # good_one
    def log_in(self, nickname, password):
        log_in = False
        users = ur.users
        cur_user = ur.current_user
        for i in users:
            if i.__contains__(nickname) and i.__contains__(password):
                cur_user = User
                log_in = True
                return log_in


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

        # good_one

    def add(self, *args):
        videos_list = self.videos
        vid = Video
        for i in args:
            if not videos_list.__contains__(i.title):
                videos_list.append(i)

                #good_one

            #test
    def get_videos(self, search):
        search_list = self.videos
        for i in self.videos:
            if i.title.casefold() == search.casefold():
                search_list.append(i.title)
            #test

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
# ur.register('Kik', 'klol', 29)
# ur.register('Kik', 'lol', 29)
v1 = Video('Movie', 200)
v2 = Video('Kinky', 130, adult_mod=True)
ur.add(v1, v2)
