file = open('files/24_6757.txt')

line = file.read().replace("CFE","*").replace("FCE","*")

for x in range(1,10000):
    if line.count("*"*x) >=1:
        print(x)