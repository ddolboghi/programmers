import sys

n = int(input())
qs = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 1. yes와 no가 나온 횟수를 누적해나간다.
# 2. y번째까지의 yes/no 개수에서 x-1번째까지의 yes/no 개수를 빼면 x번째부터 y번째까지의 yes/no 개수를 알 수 있다.
# 3. x번째부터 y번째까지의 질문 개수가 2에서 구한 yes/no 개수와 같다면 다음 yes/no + 1

yes = [0] * (n + 2)
no = [0] * (n + 2)
yes[1] = 1

for i, q in enumerate(qs, start=2):
    a, x, y = q
    if a == 1:
        if (yes[y] - yes[x - 1]) == (y - x + 1):
            print("Yes")
            yes[i] = yes[i - 1] + 1
            no[i] = no[i - 1]
        else:
            print("No")
            yes[i] = yes[i - 1]
            no[i] = no[i - 1] + 1

    else:
        if (no[y] - no[x - 1]) == (y - x + 1):
            print("Yes")
            yes[i] = yes[i - 1] + 1
            no[i] = no[i - 1]
        else:
            print("No")
            yes[i] = yes[i - 1]
            no[i] = no[i - 1] + 1
