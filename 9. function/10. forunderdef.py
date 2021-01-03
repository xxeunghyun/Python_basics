def mess1():
    print("#1")

def mess2():
    print("#2")

def mess3():
    for i in range(3):   #repeat three times
        mess2()
        print("#3")
    mess1()

mess3()


'''
2
3
2
3
2
3
1
'''
