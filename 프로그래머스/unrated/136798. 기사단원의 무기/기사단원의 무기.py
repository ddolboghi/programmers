import collections
import math
### 에라토스테네스의 채

def real_func(number):
    primes = []
    d = 2
    while d * d <= number:
        while (number % d) == 0:
            primes.append(d)
            number //= d
        d += 1
    if number > 1:
        primes.append(number)
    return math.prod([x+1 for x in collections.Counter(primes).values()])


### 계산된 약수의 개수를 딕셔너리에 저장
def solution(number, limit, power):
    factor_counts = {}
    answer_list = []
    
    for i in range(2, number+1):
        #print(i,"번째 약수 개수",real_func(i))
        if i not in factor_counts:
            factor_counts[i] = real_func(i)
        tres = factor_counts[i]
        if tres > limit:
            answer_list.append(power)
        else:
            answer_list.append(tres)
            
    return sum(answer_list) + 1