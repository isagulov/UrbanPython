class UrTube:

    def __init__(self, users, videos, current_user = None):
        # Список всех пользователей
        self.users = users
        # Список всех экземпляров класс видео
        self.videos = videos
        self.current_user = current_user

    def log_in(self, nickname, password):
        for user in self.users:
            if nickname == user.nickname and hash(password) == user.password:
                self.current_user = user
            else:
                self.current_user = None

    def register(self, nickname, password, age):
        for user in self.users:
            if nickname == user.nickname:
                print(f'Пользователь {nickname} уже существует')
            else:
                new_user = User(nickname=nickname, password=password, age=age)
                self.users.append(new_user)
                self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for video in self.videos:
            for i in range(*args)