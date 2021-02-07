price = ['20200930', 100, 130, 140, 150, 160, 170]

for data in price:
    if type(data) != int:
        price.remove(data)  # !=int means string or char = 20200930.
                            # 20200930 will be removed from the list price

print(price)


price = ['20200930', 100, 130, 140, 150, 160, 170]
print(price[1:])  # maybe print list price from the "first" position till the end


"""
[100, 130, 140, 150, 160, 170]
[100, 130, 140, 150, 160, 170]
"""
