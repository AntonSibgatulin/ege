string = "1"+"0"*75

while "10" in string or "1" in string:
    if '10' in string:
        string = string.replace("10",'001',1)
    else:
        string = string.replace('1','00',1)

print(string.count("0"))