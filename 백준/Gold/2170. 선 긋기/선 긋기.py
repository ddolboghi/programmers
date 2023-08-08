n = int(input())
seg = [tuple(map(int, input().split())) for _ in range(n)]

seg = sorted(seg, key=lambda x:x[0])

e = seg[0][1]
s = seg[0][0]
length = e-s

for s in seg[1:]:
    if s[0] > e:
        length += s[1]-s[0]
        e = s[1]
    else:
        if s[1] > e:
            length += s[1]-e
            e = s[1]

print(length)