def solution(prices):
    answer = []
    for i in range(len(prices)-1):
        answer.append(len(prices)-1 - i)
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]:
                answer.pop()
                answer.append(j-i)
                break
    answer.append(0)
    return answer