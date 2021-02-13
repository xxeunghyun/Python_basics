def printeven(data):
    result = []
    for i in data:
        if i%2 == 0:
             result.append(i)
    return result


printeven([5,3,7,8,3,1,2,4])
