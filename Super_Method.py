class User:
    def __init__(self, email):
        self.email = email
        print("This is my Email "+email)

class Wizard(User):
    def __init__(self, email, name):
        super().__init__(email)
        self.name = name
        self.email = email
    
w1 = Wizard('shital@gmail.com', 'shital')
