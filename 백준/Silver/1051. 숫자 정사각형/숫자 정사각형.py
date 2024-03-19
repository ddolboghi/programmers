N, M = map(int, input().split())

rac = [input() for _ in range(N)]

area = 1
for i in range(N):
  for j in range(M-1):
    num = rac[i][j]
    for k in range(1, (M-j)):
      if j+k < M and i+k < N and rac[i][j + k] == num and rac[i+k][j] == num and rac[i+k][j+k] == num:
        area = max(area, (k+1)**2)
print(area)
