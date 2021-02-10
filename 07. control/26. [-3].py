num = input("Postcode: ")

if num[:3] in ["010","011","012"]:
     print("강북구")

elif num[:3] in ["013","014","015"]:
    print("도봉구")

elif num[:3] in ["016", "017", "018", "019"]:
    print("노원구")

else:
    print("존재하지 않음")

"""
Postcode: 018
노원구
>>> 
 RESTART: /Users/seunghyunmin/Desktop/sh/코딩/python/@eona1301/7. control/26. [-3].py 
Postcode: 016
노원구
>>> 
 RESTART: /Users/seunghyunmin/Desktop/sh/코딩/python/@eona1301/7. control/26. [-3].py 
Postcode: 022
>>> 
 RESTART: /Users/seunghyunmin/Desktop/sh/코딩/python/@eona1301/7. control/26. [-3].py 
Postcode: 010
강북구

Postcode: 020
존재하지 않음
"""
