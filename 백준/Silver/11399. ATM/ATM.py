inputty = [input() for _ in range(2)]
N = int(inputty[0])
list1 = sorted(list(map(int,inputty[1].split())))
summed=0
for i in list1:
    summed=summed+N*i
    N-=1
print(summed)