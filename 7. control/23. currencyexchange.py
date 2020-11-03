rate = {"달러": 1167, "엔": 1.1096, "유로":1268, "위안":171}

user = input("Enter:\n")

num, currency = user.split()

print(float(num) * rate[currency], "원")

"""
Enter:
100 달러
116700.0 원
"""
