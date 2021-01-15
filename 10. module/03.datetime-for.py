import datetime

now = datetime.datetime.now()


for day in range(5, -1, -1):
    delta = datetime.timedelta(days = day)
    print(now-delta)


'''
2021-01-10 22:27:07.373551
2021-01-11 22:27:07.373551
2021-01-12 22:27:07.373551
2021-01-13 22:27:07.373551
2021-01-14 22:27:07.373551
2021-01-15 22:27:07.373551
'''
