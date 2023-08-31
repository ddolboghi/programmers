n = int(input())
arr = [0 for _ in range(n+1)]
if n>1:
    arr[2] = 1
if n>2:
    arr[3] = 1

for i in range(4, n+1):
    temp = []
    if i%3==0:
        temp.append(arr[i//3] + 1)
    if i%2==0:
        temp.append(arr[i//2] + 1)
    temp.append(arr[i-1] + 1)
    arr[i] = min(temp)
print(arr[n])