class User:
    def __init__(self, user_id=None, username=None):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        print("new user being created...")

    def follow(self, user):
        user.following += 1
        self.following += 1


user_1 = User("001", "richard")
user_2 = User("002", "kevin")
user_1.follow(user_2)


