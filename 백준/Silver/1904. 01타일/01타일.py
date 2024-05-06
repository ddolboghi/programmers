n = int(input())

pre2 = 1
pre1 = 2

for i in range(2, n):
  next_ = (pre1 + pre2)%15746
  pre2 = pre1
  pre1 = next_

if n == 1:
  print(pre2)
else:
  print(pre1)