score = int(input("Enter the score:\n"))

if 81 <= score <= 100:
    print("grade: A")

elif 61 <= score <= 80:
    print("grade: B")

elif 41 <= score <= 60:
    print("grade: C")

else:
    print("grade: F")


"""
Enter the score:
77
grade: B
>>> 
 RESTART: /Users/seunghyunmin/Desktop/sh/코딩/python/@eona1301/7. control/22. elif.py 
Enter the score:
100
grade: A
>>> 
 RESTART: /Users/seunghyunmin/Desktop/sh/코딩/python/@eona1301/7. control/22. elif.py 
Enter the score:
22
grade: F
>>> 
 RESTART: /Users/seunghyunmin/Desktop/sh/코딩/python/@eona1301/7. control/22. elif.py 
Enter the score:
41.2
Traceback (most recent call last):
  File "/Users/seunghyunmin/Desktop/sh/코딩/python/@eona1301/7. control/22. elif.py", line 1, in <module>
    score = int(input("Enter the score:\n"))
ValueEr
"""
