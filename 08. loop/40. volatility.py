low = [100, 200, 400, 800, 1000]
high = [150, 300, 430, 880, 1000]
volatility = []

for i in range(len(low)):
    volatility.append(high[i]-low[i])

print(volatility)

'''
[50, 100, 30, 80, 0]
'''



'''
volatility 라는 공간을 만들어두고 그 안에 ㅊㅐ워지는 요소는
for 이용해서 어팬드 된 애들 어펜드 = ㅐ새로 떳붙여서 작성 하는 거니까
'''
