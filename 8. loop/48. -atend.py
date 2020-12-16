
apart = [[101, 102], [201, 202], [301, 302]]

for item in apart:
    for detail in item:
        print(detail, "호") #detail in item
    print("-"*5) # item in apart  pair

'''
101 호
102 호
-----
201 호
202 호
-----
301 호
302 호
-----
'''
