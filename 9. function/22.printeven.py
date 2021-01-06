def printeven(list):
    evenlist=[]

    for num in list:
        if num%2==0:
            #print(num)
            evenlist.append(num)

    print(evenlist)


printeven([2,6,7,4,9])

'''
[2, 6, 4]
'''
