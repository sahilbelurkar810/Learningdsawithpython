class User:
    def __init__(self,name,username,email):
        self.username=username
        self.email=email
        self.name=name
    def introduce(self,guestname):
        print("Hi {}! , I am {}! contact me at {}".format(guestname,self.name,self.email))
    
    def __repr__(self): 
        return "User(username:{}, name:{}, email:{})".format(self.username,self.name,self.email)
    def __str__(self):
        return self.__repr__()
user3 = User("jane","janedoe","janedoe@gmail")
# user3.introduce("Sahil")
# print(user3.username)

users_list = [
    User("Jane", "janedoe", "ajanedoe@gmail.com"),
    User("John", "johndoe", "johndoe@gmail.com"),
    User("Alice", "alice123", "alice@example.com"),
    User("Bob", "bobmartin", "bobmartin@yahoo.com"),
]
users_lists = sorted(users_list, key=lambda user1: user1.name)
print(users_lists)
