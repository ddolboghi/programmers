n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]
cnt = 0
for c in coins[::-1]:
    if c <= k:
        cnt += k//c
        k %= c
print(cnt)