def solution(n, left, right):
    unit = [i for i in range(1, n+1)]
    arr = []
    k = 0
    for i in range(left, right+1):
        if k != i//n + 1:
            k = i//n + 1
            unit[:k] = [k for _ in range(k)]
            arr += unit
            # print(unit, k)
        else:
            pass
    return arr[left%n:left%n+(right-left)+1]