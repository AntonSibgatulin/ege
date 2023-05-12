file = open("files/27B_7603.txt")
N = int(file.readline())
K = int(file.readline())


numbers = [int(i) for i in file]
x = max(numbers)
numbers.remove(x)
print(x+max(numbers))