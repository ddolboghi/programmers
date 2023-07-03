import sys
sys.setrecursionlimit(10 ** 6)
def solution(n):
    answer = 1
    # n이 2로 구성될 수 있는 최대 개수
    for i in range(1, (n//2)+1):
        s = per(i+n-2*i, 1) // (per(i, 1)*per(n-2*i, 1))
        answer += s
    return answer%1234567

def per(x, y):
    # 순열 구하는 함수, 초기 y는 반드시 1이어야함
    if x == 1:
        return y
    elif x == 0:
        return 1
    else:
        y *= x
        return per(x-1, y)