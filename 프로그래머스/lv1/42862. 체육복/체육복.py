def solution(n, lost, reserve):
    answer = 0
    a = []
    # 전체 n
    # 없는애 lost
    # 여벌 있는애 reserve
    res = list(set(reserve) - set(lost))
    lst = list(set(lost) - set(reserve))
    
    for i in lst :
        if (i-1) in res :
            res.remove(i-1)
            a.append(i)
        elif (i+1) in res :
            res.remove(i+1)
            a.append(i)

    answer = n - len(lst) + len(a)
    
    return answer