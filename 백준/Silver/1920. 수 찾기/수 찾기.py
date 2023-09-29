n = int(input())
a = list(map(int, input().split()))
m = int(input())
ms = list(map(int, input().split()))

a.sort()
def binarySearch(start, end, value):
    if start > end:
        return 0
    
    mid = (start + end) // 2
    if a[mid] == value:
        return 1
    elif a[mid] > value:
        end = mid-1
    else:
        start = mid+1
    return binarySearch(start, end, value)

for i in ms:
    print(binarySearch(0, n-1, i))