n = int(input())
xs = list(map(int, input().split()))
xss = sorted(list(set(xs)))

# 순서대로 돌면서 해당 값보다 작은 값의 개수 찾기
# 해당 값의 인덱스만 찾으면 정렬되있기때문에 압축 개수 알수 있음

def binarySearch(s, e, v):
    if s>e:
        return -1
    m = (s+e)//2
    if xss[m] == v:
        return m
    elif xss[m] < v:
        s = m+1
    else:
        e = m-1
    return binarySearch(s, e, v)

for x in xs:
    print(binarySearch(0, len(xss)-1, x), end=' ')