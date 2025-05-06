n, x = map(int, input().split())
visit = list(map(int, input().split()))

# 둘째날부터 방문자수를 누적시킨다.
# x일동안 방문자수 = a일까지 누적 방문자수 - b일까지 누적 방문자수, a > b
# a = i번째 날 + x
# b = i번째 날
# a일 - b일로 x일동안의 방문자수를 얻으려면 첫번째 원소가 0인게 편하다
acc_visit = [0, visit[0]]
for i in range(1, n):
    acc_visit.append(acc_visit[i] + visit[i])

max_visit = 0
max_cnt = 0
for i in range(n):
    end = i + x
    if end <= n:
        acc = acc_visit[end] - acc_visit[i]
        if acc >= max_visit:
            if acc != max_visit:
                max_cnt = 0
            max_visit = acc
            max_cnt += 1

if max_visit > 0:
    print(max_visit)
    print(max_cnt)
else:
    print("SAD")
