apart = [[101, 102], [201, 202], [301, 302]]

for item in apart[::-1]:
    for detail in item:
        print("ROOM #",detail)


'''
ROOM # 301
ROOM # 302
ROOM # 201
ROOM # 202
ROOM # 101
ROOM # 102
'''
