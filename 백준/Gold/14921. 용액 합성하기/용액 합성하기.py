n = int(input())
sol = list(map(int, input().split()))

main_min = float('inf')
sub_min = float('inf')

def searchMin(start, end, value, sub_min):
    if start > end:
        return sub_min

    mid = (start + end)//2
    mix = value + sol[mid]
    if abs(sub_min) > abs(mix):
        sub_min = mix
    # print(value, sub_min)
    if mix == 0:
        return sub_min
    elif mix > 0:
        end = mid - 1
    else:
        start = mid + 1    
    return searchMin(start, end, value, sub_min)

for i in range(n-1):
    tmp = searchMin(i+1, n-1, sol[i], sub_min)

    if abs(main_min) > abs(tmp):
        main_min = tmp

print(main_min)