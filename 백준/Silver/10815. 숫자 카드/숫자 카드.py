n = int(input())
cards = list(map(int, input().split()))
m = int(input())
finds = list(map(int, input().split()))

cards.sort()
def binarySearch(s,e,v):
    if s>e:
        return 0
    m = (s+e)//2
    if cards[m] == v:
        return 1
    elif cards[m] > v:
        e = m-1
    else:
        s = m+1
    return binarySearch(s,e,v)
for f in finds:
    print(binarySearch(0, n-1, f), end=' ')