def convertint(data):
    data = data.split(',')
    result = ""
    for detail in data:
        result += detail
    return int(result)


print(convertint("1,234,567"))

