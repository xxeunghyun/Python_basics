temp = ('apple', 'banana', 'cake')
a,b,c = temp
print(a,b,c)


"""
less than tuple elements number
    a,b = temp
ValueError: too many values to unpack (expected 2)
"""

"""
more than tuple elements number
    a,b,c,d = temp
ValueError: not enough values to unpack (expected 4, got 3)
"""

"""
correct output: apple banana cake
"""

