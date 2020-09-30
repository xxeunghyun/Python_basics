movierank = ["Dr.Strange", "Split", "Lucky", "Batman"]

for data in ["Split", "Batman"] :
    movierank.remove(data)

print(movierank)


"""
expected: Dr, Lucky only left
real: ['Dr.Strange', 'Lucky']
"""
