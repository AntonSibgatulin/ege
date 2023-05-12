file = open("files/24_7600.txt")

line = file.read().replace("Q","*").replace("R","*").replace("S","*").replace("**","* *").split(" ")
max_=0

for x in line:
    max_ = max(max_,len(x))
print(max_)