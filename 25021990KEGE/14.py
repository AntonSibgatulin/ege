mat= 2*(729**1021)-2*(243**1022)+(81**1023)-2*(27**1024)-1025

def to(a,b):
    string = ""
    while a>0:
        string = string+str(a%b)
        a=a//b
    return string

string = to(mat,3)
count = 0
print(string)
while string.startswith('0'):
    string = string.replace('0','',1)
    count+=1
print(count)

print(to(4,2))