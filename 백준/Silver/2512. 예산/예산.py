n = int(input())
budget = list(map(int, input().split()))
m = int(input())

start = 1
end = max(budget)
limit = 0

while start <= end:
    mid = (start+end)//2
    sum = 0
    for i in budget:
        if i >= mid:
            sum += mid
        else:
            sum += i
    
    if sum > m:
        end = mid-1
    else:
        start = mid+1
        if limit < mid:
            limit = mid
print(limit)