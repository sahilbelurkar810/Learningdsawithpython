class User:
    def __init__(self, name, username, email):
        self.username = username
        self.email = email
        self.name = name

    def __repr__(self):
        return f"User(name={self.name}, username={self.username}, email={self.email})"


class userDatabase:
    def __init__(self):
        self.users = []

    def insert(self, user):
        i = 0
        while i < len(self.users):
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)

    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user

    def update(self, updated_user):
        target = self.find(updated_user.username)
        if target:
            target.name = updated_user.name
            target.email = updated_user.email

    def list_all(self):
        return self.users


# Example usage:
database = userDatabase()
John = User("John", "johndoe", "johndoe@gmail.com")
database.insert(John)

# Update John's email
database.update(User(name="John", username="johndoe", email="johnemail@gmail.com"))

# Find the updated user
user = database.find("johndoe")
print(user)  # Output: User(name=John, username=johndoe, email=johnemail@gmail.com)


# List all users
print(
    database.list_all()
)  # Output: [User(name=John, username=johndoe, email=johnemail@gmail.com)]


