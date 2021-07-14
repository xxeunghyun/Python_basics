class Account:
    account_cnt = 0

    def __init__(self, name, balance):
        self.bank_name = "Hang Seng Bank"
        self.name = name
        self.balance = balance
        self.account_num = self.set_account()

        Account.account_cnt += 1

    def __str__(self):
        return F"총 등록 인원 : {Account.account_cnt}\n\n은행이름 : {self.bank_name}\n예금주 : {self.name}\n계좌번호 : {self.account_num}\n잔액 : {self.balance}"

    def set_account(self):
        import random
        tmp = ""

        for num in [3,2,6]:
            for _ in range(num):
                tmp += str(random.randint(0,9))
            tmp += "-"

        return tmp[:len(tmp)-1]


account = Account("홍길동", 1500)

print(account)
