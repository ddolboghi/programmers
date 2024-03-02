def solution(n):
    # 1. n(몫)을 3으로 나누어서 나머지 == 0이면 4로 바꾸고 answer++ 아니면 나머지 바로 answer++
    # 1-1. 나머지 == 0일때 몫--
    # 2. 몫 < 3이 될때까지 나누고 1번 반복
    # 3. 마지막 몫 answer++        
    answer = ''
    
    while n >= 3:
        mod = n % 3
        n //= 3
        if mod == 0:
            answer += '4'
            n -= 1
        else:
            answer += str(mod)
            
    answer += str(n%3) if n != 0 else ''
    return answer[::-1]
