
print("y z w x")


for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if x ==1 and w ==0 and z ==0 and y==0:
                    continue
                if( not((x and not(y)) == (z or not(w))) or (x and z)  )==0:
                    print(y,z,w,x)