for x in range(1000,9999):
    string = str(x)
    num = int(string[0])*int(string[1])
    num2 = int(string[2])*int(string[3])
    result = int(str(min(num,num2))+str(max(num,num2)))
    if result == 1214:
        print(x)