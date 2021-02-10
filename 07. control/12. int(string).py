num = int(input("숫자를 입력하세요:"))
print(num+10)

"""
숫자를 입력하세요:
Traceback (most recent call last):
  File "/Users/seunghyunmin/Desktop/sh/코딩/python/@eona1301/7. control/12. int(string).py", line 1, in <module>
    num = int(input("숫자를 입력하세요:"))
ValueError: invalid literal for int() with base 10: ''
>>> 
 RESTART: /Users/seunghyunmin/Desktop/sh/코딩/python/@eona1301/7. control/12. int(string).py 
숫자를 입력하세요:10
20

숫자를 입력하라는 질문은 던져주고 여기서 받은 인풋은 인트형임을 알고
거기서 압력받은 수에 10을 더한 값을 출력해서 나타냄
숫자로 입력받은게 아닐시에는 에러 메세지가 뜸
"""
