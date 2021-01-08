def printmxn(string,n):
    for i in range(0, len(string), n):
        print(string[i:i+n])

printmxn("HelloEveryone", 3)

'''
Hel
loE
ver
yon
e
'''
