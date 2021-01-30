class Stock:
    def __init__(self, name, code, PER, PBR, revenue):
        self.name = name
        self.code = code
        self.PER = PER
        self.PBR = PBR
        self.revenue = revenue

    def set_name(self, name):
        self.name = name

    def set_code(self,code):
        self.code = code

    def self_PER(self, PER):
        self.PER = PER

    def self_PBR(self, PBR):
        self.PBR = PBR

    def set_dividend(self, revenue):
        self.revenue = revenue

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code



samsung = Stock("SAMSUNG", "005930", 15.79, 1.33, 2.83)
hyundai = Stock("HYUNDAI", "005380", 8.70, 0.35, 4.27)
lg = Stock("LG", "066570", 317.34, 0.69, 1.37)

stock_list = [samsung, hyundai, lg]

for data in stock_list:
    print(data.code, data.PER)



'''
005930 15.79
005380 8.7
066570 317.34

모든 애들의 코드랑 PER 출력
'''

