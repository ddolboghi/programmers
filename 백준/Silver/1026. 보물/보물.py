inputty = [input() for _ in range(3)]
N = int(inputty[0])
A = list(map(int,inputty[1].split()))
B = list(map(int,inputty[2].split()))

print(sum([sorted(A)[i]*sorted(B,reverse=True)[i] for i in range(N)]))