def solution(number, limit, power):
    answer = 1
    # 1~i~number까지 각 약수의 개수 구하기
    for i in range(2, number+1):
        cnt = 0
        # i의 제곱근까지만 나누고 그 짝들의 개수만 더해주기
        for j in range(1, int(i**0.5)+1):
            if i % j == 0:
                cnt += 1
                # j가 i//j와 같지 않다면 짝이므로 cnt++
                if j != i//j:
                    cnt += 1
        # print(cnt)
        if cnt > limit:
            answer += power
        else:
            answer += cnt
    return answer