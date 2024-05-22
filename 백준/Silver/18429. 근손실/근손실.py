n, k = map(int, input().split())
ws = list(map(int, input().split()))

cnt = 0
check = [False] * n
def per(extra, r):
  global cnt
  if extra >= 0 and r == n:
    cnt += 1
    return
  
  if extra < 0:
    return
  
  for i in range(n):
    if not check[i]:
      check[i] = True
      per(extra + ws[i] - k, r+1)
      check[i] = False

per(0, 0)
print(cnt)