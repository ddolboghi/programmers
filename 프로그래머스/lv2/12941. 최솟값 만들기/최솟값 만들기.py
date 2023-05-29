def solution(A,B):
    answer = 0
    # 가장 큰 값이 가장 작은 값과 곱해져야함
    # 이런 경우는 딱 한가지 밖에 없음
    a = sorted(A)
    b = sorted(B, reverse=True)
    for i in range(len(a)):
        answer += a[i] * b[i]
    return answer