file = open("files/24 (1).txt")

line = file.read().split("PP")
max_ = -10**11
for x in line:
    max_ = max(max_,len(x))
print(max_+2)