def solution(n, k):
    answer = 0
    s = ''
    while n > 0:
        s += str(n%k)
        n //= k
    # print(s[::-1].split('0'))
    for i in s[::-1].split('0'):
        if len(i) != 0 and i != '1':
            og = int(i)
            cnt = 0
            for j in range(2, int(og**0.5)+1):
                if og % j == 0:
                    cnt +=1
                    break
            if cnt == 0:
                answer += 1
    return answer