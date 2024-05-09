import sys

for _ in range(int(input())):
  n = int(input())
  heights = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
  
  head, tail = heights[0], heights[1]
  dif = abs(head-tail)

  for i in range(2, n):
    if i%2 == 0:
      if dif < abs(heights[i] - head):
        dif = abs(heights[i] - head)
      head = heights[i]
    else:
      if dif < abs(heights[i] - tail):
        dif = abs(heights[i] - tail)
      tail = heights[i]
  
  if dif < abs(head - tail):
    dif = abs(head - tail)

  print(dif)