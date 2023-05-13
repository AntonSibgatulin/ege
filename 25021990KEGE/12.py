string = '7'*104

while '33333' in string or '777' in string:
    if '33333' in string:
        string = string.replace("33333","7",1)
    else:
        string = string.replace("777",'3',1)
print(string)