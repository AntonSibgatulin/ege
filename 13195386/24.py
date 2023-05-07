file = open("files/24.txt")


line = ''
min_c = 1000000
for l in range(1000):
    x = file.readline()
    print(x)
    if x.count("G")<min_c:
        line = x
        min_c = x.count("G")

a = [0]*26

for x in line:
    print(x)
    if(ord(x)-65<0 or ord(x)-65>=len(a)):continue
    a[ord(x)-65]+=1

index = 0
max_ = 0
for j in range(len(a)):
    if a[j]>=max_:
        index = j
        max_ = a[j]
print("res",chr(65+index))

