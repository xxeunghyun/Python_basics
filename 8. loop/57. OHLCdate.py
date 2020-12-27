ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

volatility = []

for data in ohlc[1:]:
    if data[ohlc[0].index("close")] > data[ohlc[0].index("open")]:
        print(data[ohlc[0].index("high")] - data[ohlc[0].index("low")])

'''
10
'''

'''
close = 3
open = 0

if>> yes
high = 1, low = 2
1st - 2nd

1: X
2: X
3: O >> 1st = 310, 2nd = 300, 1-2= 310-300 = 10
'''
