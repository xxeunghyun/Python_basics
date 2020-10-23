fruit = {"Spring": "Strawberry", "Summer":"Tomato", "Autumn":"Apple"}

### link two keywords

data = input("Your favourite season is?\n")

if data in list(fruit.keys()):
    print("It's in list!")

else:
    print("Not in list!")
