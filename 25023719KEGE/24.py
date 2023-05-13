file = open("files/24_7624.txt")
line = file.read().replace("X","*").replace("Y","*").replace("Z","*").replace("**","* *").split(" ")
max_ = 0

for x in line:
    max_ = max(max_,len(x))
print(max_)