class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class Urtube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None
    
    def register(self, nickname, password, age):
        for user in self.users:
            if nickname == user.nickname:
                print(f'"Пользователь {nickname} уже существует".')
                return
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            self.current_user = new_user

    def log_in(self, nickname, password):
        for user in self.users:
            if nickname == user.nickname and hash(password) == user.password:
                self.current_user = user
                return self.current_user.nickname
            print(f'пользователь {nickname} не существует')

    def lof_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if video not in self.videos:
                self.videos.append(video)
            else:
                'Такое видео уже существует'

    def watch_video(self, name_video):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        for video in self.videos:
            if video.title == name_video:
                if video.adult_mode == True and self.current_user.age < 18:
                    print('Досвидания')
                    return
                for sec in range(video.time_now, video.duration + 1):
                    print(sec)
                print('Конец видео')




    def get_video(self, key_word):
        title_list = []
        for video in self.videos:
            if key_word.lower() in video.title.lower():
               title_list.append(video.title)
            return title_list




ur = Urtube()

v1 = Video('Лучший язык программирования 2024 года', 200)

v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

ur.add(v1, v2)

print(ur.get_video('лучший'))

print(ur.get_video('ПРОГ'))

ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'lolkekcheburek', 13)

ur.watch_video('Для чего девушкам парень программист?')

ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)

ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)

print(ur.current_user)

ur.watch_video('Лучший язык программирования 2024 года!')


