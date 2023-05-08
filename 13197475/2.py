print("z,y,x,w")


for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if x ==0 and y ==1 and w ==0 and z==0:
                    continue
                if (((not x or z)==(y and not w))<=(z and y) )==0:
                    print(z,y,x,w)