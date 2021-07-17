class Account:
    account_cnt = 0

    def __init__(self, name, balance):
        self.bankname = "HSBC"
        self.name = name
        self.balance = balance
        self.account_num = self.set_account() #이전 예제랑 다른 점 여기!!

        Account.account_cnt += 1

    def __str__(self):
        return F"총 등록 인원 : {Account.account_cnt}\n은행이름 : {self.bankname}\n예금주 : {self.name}\n계좌번호 : {self.account_num}\n잔액 : {self.balance}"

    def set_account(self):
        import random
        tmp = ""

        for num in [3,2,6]:
            for _ in range(num):
                tmp += str(random.randint(0,9))
            tmp += "-"

        return tmp[:len(tmp)-1]

    def get_account_num(self):
        print(Account.account_cnt)

    def deposit(self):
        while True:
            coin = int(input("값을 입력하세요: "))

            if coin>=1 :
                self.balance += coin
            else:
                print("최소 1원 이상을 입력해야 합니다.")


account = Account("홍길동", 3000)
