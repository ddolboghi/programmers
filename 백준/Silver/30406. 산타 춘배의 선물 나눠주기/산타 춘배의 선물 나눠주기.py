import sys

n = int(input())
presents = list(map(int, sys.stdin.readline().rsplit()))

counts = [0, 0, 0, 0]

for p in presents:
  counts[p] += 1

answer = 0

max_count = min(counts[0], counts[3])
answer += max_count * 3
counts[0] -= max_count
counts[3] -= max_count

max_count = min(counts[1], counts[2])
answer += max_count * 3
counts[1] -= max_count
counts[2] -= max_count

remain_two, remain_one = -1, -1

for i in range(4):
  if counts[i] > 0:
    if remain_two == -1:
        remain_two = i
    else:
        remain_one = i

if remain_one == -1:
  print(answer)
else:
  answer += min(counts[remain_two], counts[remain_one]) * (remain_two ^ remain_one)
  print(answer)