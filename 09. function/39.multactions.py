def fun0(num):
    return num*2

def fun1(num):
    return fun0(num+2)

def fun2(num):
    num = num+10
    return fun1(num)


c = fun2(2)
print(c)


'''
12
fun1(12)
fun0(14)
28
'''
