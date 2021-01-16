import datetime

day = "2021-01-16"
ret = datetime.datetime.strptime(day, "%Y-%m-%d")
print(ret, type(ret))


'''
2021-01-16 00:00:00 <class 'datetime.datetime'>
'''
