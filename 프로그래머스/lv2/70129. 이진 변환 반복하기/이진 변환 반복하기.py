def solution(s):
    cnt = 0
    z = 0
    while s != '1':
        a = len(s)
        c = len(s.replace('0', ''))
        z += a-c
        s = bin(c)[2:]
        cnt += 1
    
    return [cnt, z]