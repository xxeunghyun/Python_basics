def fun1(num):
    return num+4

def fun2(num):
    num = num+2
    return fun1(num)


c = fun2(10)
print(c)


'''
fun2(10)
10 > 12
fun1(12)
12+4 = 16
'''
