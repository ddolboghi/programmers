n = int(input())

meetings = [tuple(map(int, input().split())) for _ in range(n)]

# 끝나는 시간이 가장 작은 순서대로 정렬
# 끝나는 시간이 같은 경우 시작시간이 작은 순서대로 정렬
meetings = sorted(sorted(meetings, key=lambda x:x[0]), key=lambda x: x[1]) 
#print(meetings)

arr = [meetings[0]]
i = 0
for m in meetings[1:]:
    if arr[i][1] <= m[0]:
        arr.append(m)
        i += 1
print(len(arr))