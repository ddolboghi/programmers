n = int(input())
people = list(map(int, input().split()))

# people를 내림차순 정렬후 누적 합을 구하고 계속 더하면됨
result = 1
people = sorted(people)
arr = [people[0]]# 누적값 저장
for p in people[1:]:
    arr.append(arr[-1] + p)
print(sum(arr))