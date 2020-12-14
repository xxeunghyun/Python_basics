apart = [[101, 102], [201, 202], [301, 302]]

for item in apart[::-1]:
    for detail in item[::-1]:
        print("ROOM #",detail)

'''
ROOM # 302
ROOM # 301
ROOM # 202
ROOM # 201
ROOM # 102
ROOM # 101
'''
