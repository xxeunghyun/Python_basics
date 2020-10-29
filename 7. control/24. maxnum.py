num = []

for i in range(3): ###from 0 to index number 3 >> 0.1.2
    number = int(input(F"Input number {i+1} : "))
    num.append(number)

max_num = num[0]

for i in range(3):
    if max_num < num[i]:
        max_num = num[i]

print(max_num)

"""
Input number 1 : 7
Input number 2 : 9
Input number 3 : 2
9
>>>
"""
