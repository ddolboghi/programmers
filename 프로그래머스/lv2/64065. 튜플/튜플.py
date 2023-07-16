def solution(s):
    ss = sorted(s[2:-2].split('},{'), key=lambda x: len(x))
    # print(ss)
    arr = []
    for i in ss:
        if len(arr) == 0:
            arr += i.split(',')
        else:
            sr = set(i.split(','))
            arr += list(sr - set(arr))
    return [int(a) for a in arr]