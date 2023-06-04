def solution(n,a,b):
    answer = 0
    i = 1
    while n >= 2**i:
        if (a-1)//(2**i) == (b-1)//(2**i):
            answer = i
            break
        i += 1
    return answer

def another_level(n,a,b):
    return ((a-1)^(b-1)).bit_length()