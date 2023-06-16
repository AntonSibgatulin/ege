file = open("files/24.txt")

line = file.read()
a1 = 'ABCDF'
a2 = 'EU'
for x in range(0,len(line)-3,3):
    if x>=len(line):break
    if line[x] in a1 and line[x+1] in a2 and line[x+2] in a1:
        line = line.replace(line[x]+line[x+1]+line[x+2],'*',1)

max_ = 0
count = 0
for l in line:
    if l == "*":
        count+=1
        max_ = max(count, max_)
    else:
        max_ = max(count,max_)
        count = 0

print(max_)