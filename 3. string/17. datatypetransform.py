cost = "5,969,782,550"
cost = cost.replace(',','')
cost = int(cost)

print(F"결과 값은 {cost}이며 타입은 {type(cost)}이다.")

"""
결과 값은 5969782550이며 타입은 <class 'int'>이다.

중요한 점 : replace(',',' ') 처럼 공백으로 대체하면string 이므로
형변환 실패
"""
