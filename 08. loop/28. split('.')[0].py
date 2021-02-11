data = ['hello.py', 'ex01.py', 'intro.docx']

for i in data:
    print(i.split('.')[0])


'''
hello/ex01/intro >> O
.을 기준으로 왼쪽이 [0] 오른쪽이 [1]
'''
