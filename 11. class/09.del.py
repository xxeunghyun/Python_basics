class Human:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __del__(self):
        print("나의 죽음을 알리지 말라.")

    def who(self):
        print(f"NAME: {self.name}, AGE: {self.age}, GENDER: {self.gender}")

    def setinfo(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender


areum = Human("areum", 25, "Female")
#areum.setinfo("areum", 25, "Female")
#areum.who()
del areum
