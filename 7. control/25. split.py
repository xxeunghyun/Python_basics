phone = input("Enter the phone number: ")
phone = phone.split('-')[0]

if phone == "010":
    newsweire = "unknown"

elif phone == "011":
    newsweire = "SKT"

elif phone == "016":
    newsweire = "KT"

elif phone == "019":
    newsweire = "LGU"

print(f"You are {newsweire} user.")

"""
Enter the phone number: 010-838-202
You are unknown user.
>>> 
 RESTART: /Users/seunghyunmin/Desktop/sh/코딩/python/@eona1301/7. control/25. split.py 
Enter the phone number: 011-8889-2233
You are SKT user.
>>>
"""
