class Account:
    def __init__(self, name, balance):
        self.bank_name = "Hang Seng Bank"
        self.name = name
        self.balance = balance
        self.account_number = self.set_account()


    def __str__(self):
        return F"Bank: {self.bank_name}\nCustomer: {self.name}\nAccount Number: {self.account_number}\nBalance: HKD {self.balance}"


    def set_account(self):
        import random
        tmp = ""

        for num in [3,2,6]:
            for _ in range (num):
                tmp += str(random.randint(0,9))
            tmp += "-"

        return tmp[:len(tmp)-1]


account = Account("Hong Gil Dong", 1000)
print(account)



# __init__ 에 _ 두개 아니면 에러 뜸

