fruit = {"Spring": "Strawberry", "Summer":"Tomato", "Autumn":"Apple"}

### link two keywords

data = input("Your favourite fruit is?\n")

if data in list(fruit.values()):
    print("It's in list!")

else:
    print("Not in list!")

"""
 RESTART: /Users/seunghyunmin/Desktop/sh/코딩/python/@eona1301/7. control/20. dict_values.py 
Your favourite fruit is?
Apple
It's in list!
>>>
"""
