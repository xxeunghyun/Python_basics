import datetime
import time

while True:
    now = datetime.datetime.now()
    print(now.strftime("%H:%M: %S"))
    time.sleep(1)


'''
20:24: 34
20:24: 35
20:24: 36
20:24: 37
20:24: 38
20:24: 39
20:24: 40
20:24: 41
20:24: 42
20:24: 43


printing the time with the interval of 1 sec
only ends when i press esc key
'''
