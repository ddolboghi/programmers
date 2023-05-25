def sub(n, i):
    # n을 1씩 증가하는 i로 빼고 뺀 값이 n이 됨
    # n=0이면 1 반환
    # n<0이면 0 반환
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return sub(n-i, i+1)

def solution(n):
    # 자기 자신 항상 포함
    answer = 1
    # n에서 빼는 값이 n의 절반 이하일때까지만 세면 됨
    for i in range(1, n-n//2):
        answer += sub(n, i)
    return answer