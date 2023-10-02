import sys
na, nb = map(int, input().split())
setA = list(map(int, input().split()))
setB = list(map(int, input().split()))
setB.sort()
dif = []
def isInB(s,e,v):
    if s>e:
        return dif.append(v)
    m = (s+e)//2
    if setB[m] == v:
        return None
    elif setB[m] > v:
        e = m-1
    else:
        s = m+1
    return isInB(s,e,v)

for a in setA:
    isInB(0,nb-1,a)
if len(dif)==0:
    print(0)
else:
    dif.sort()
    print(len(dif))
    print(' '.join(map(str,dif)))