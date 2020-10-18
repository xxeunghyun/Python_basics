num = int(input(" Enter the input: "))

num -= 20

if num<0:
    num = 0

elif num > 255:
    num = 255

print(f"Output: {num}")

"""
 Enter the input: 10
Output: 0
>>> 
 RESTART: /Users/seunghyunmin/Desktop/sh/코딩/python/@eona1301/7. control/15.int(input)+elif.py 
 Enter the input: 290
Output: 255
>>> 
 RESTART: /Users/seunghyunmin/Desktop/sh/코딩/python/@eona1301/7. control/15.int(input)+elif.py 
 Enter the input: 200
Output: 180
>>>
"""
