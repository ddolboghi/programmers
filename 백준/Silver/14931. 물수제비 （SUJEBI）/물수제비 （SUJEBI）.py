import sys

l = int(input())
scores = list(map(int, sys.stdin.readline().split()))

# 1 <= d <= 1,000,000
# d = 1일때 1000000번 루프, d = 1000000일때 1번 루프

max_score = 0
min_d = float("inf")

d = 1
while d <= l:
    score = 0
    for s in scores[d - 1 :: d]:
        score += s

    if max_score < score:
        if max_score == score:  # 점수가 같으면 더 작은 d
            min_d = min(min_d, d)
        else:
            min_d = d
        max_score = score

    d += 1

if max_score <= 0:
    print(0, 0)
else:
    print(min_d, max_score)
