class User:
    def log(self):
        print("Logged In")

class UserOne(User):
    def Logged(self, name):
        print("Logged In Sucessfully! "+name)


u1 = UserOne()
u1.Logged('shital')
u1.log()