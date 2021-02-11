
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for data in ohlc[1:]:
    print(data[ohlc[0].index("close")] - data[ohlc[0].index("open")])


'''
close = 3, open = 0
0
-10
10

>> OO

'''
