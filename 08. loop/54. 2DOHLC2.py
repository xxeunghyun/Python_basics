ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [300, 310, 300, 310]]

for data in ohlc[1:]:
    for i in range(len(data)):
        if ohlc[0].index("close") == i and data[i] > 150:
            print(data[i])

'''
310
'''
