#투포인터 풀이
n = int(input())
solution = list(map(int, input().split()))

left = 0
right = n-1

result = abs(solution[left]+solution[right])
result_left = left
result_right = right

while left < right:
    tmp = solution[left] + solution[right]

    if abs(tmp) < result:
        result = abs(tmp)
        result_left = left
        result_right = right

        if result == 0:
            break

    if tmp < 0: #합이 0보다 작으면 더 큰값을 더해야함
        left += 1
    else: #합이 0보다 크면 더 작은 값을 더해야함
        right -= 1

print(solution[result_left], solution[result_right])