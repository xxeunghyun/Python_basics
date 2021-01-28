class Human:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def who(self):
        print(f"NAME: {self.name}, AGE: {self.age}, GENDER: {self.gender}")


areum = Human("areum",25, "Female")
areum.who()
