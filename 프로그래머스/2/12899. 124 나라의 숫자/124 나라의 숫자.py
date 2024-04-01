def solution(n):
    # 3보다 작아질때까지 나누기
    # 나머지가 0이면 4로 바꾸고 다음 차례에 (몫-1)/3
    answer = ''
    while n >= 3:
        mod = n % 3
        n //= 3
        if mod == 0:
            answer += "4"
            n -= 1
        else:
            answer += str(mod)

    # 마지막 몫 합치기
    answer += str(n) if n != 0 else ""
    
    return answer[::-1]