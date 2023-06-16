for n in range(1, 62):
    string = ">" + (15 * "1") + ("2" * n) + ('3' * 16)
    while '>1' in string or '>2' in string or '>3' in string:
        if '>1' in string:
            string = string.replace('>1', "22>", 1)
        if '>3' in string:
            string = string.replace('>3', '13>', 1)
        if '>2':
            string = string.replace('>2', '1000>3', 1)
    string = string.replace('>', '')
    summ = sum(list(map(int, list(string))))
    if summ % len(string)-1 == 0:
        print(n)
        break
