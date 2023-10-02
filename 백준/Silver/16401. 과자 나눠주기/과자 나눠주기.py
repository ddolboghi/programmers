m, n = map(int, input().split())
snack = list(map(int, input().split()))

start, end = 1, max(snack)
while start<=end:
    cnt = 0
    mid = (start+end)//2
    for i in snack:
        cnt += i//mid
    if cnt >= m:
        start = mid+1
    else:
        end = mid-1
print(end)