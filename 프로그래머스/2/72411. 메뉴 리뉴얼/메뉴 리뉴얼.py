from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    # 각 order마다 course 값으로 뽑을 수 있는 조합들 담기
    eachComb = []
    for order in orders:
        for c in course:
            eachComb += list(combinations(sorted(order), c))
    
    # 코스요리 구성 메뉴들의 최소 주문 횟수 == 2
    # -> 코스요리의 최소 주문 횟수 == 2
    # 1. order별 조합의 주문 횟수 구하기 -> Counter 활용
    # 2. 각 조합의 주문 횟수 == 이전 주문 횟수 -> 추가, 
    #    각 조합의 주문 횟수 > 이전 주문 횟수 -> 이전 값 다 삭제하고 추가 및 주문 횟수 갱신
    # 3. 뽑은 조합들에서 course의 원소 길이별로 수행해야함 -> dictionay 활용
    possible = {c:[2] for c in course}
    for courseMenu, cnt in Counter([''.join(comb) for comb in eachComb]).items(): 
        if possible[len(courseMenu)][0] == cnt:
            possible[len(courseMenu)].append(courseMenu)
        elif possible[len(courseMenu)][0] < cnt:
            possible[len(courseMenu)] = [cnt, courseMenu]
            
    # print(possible)
    for v in possible.values():
        answer += v[1:] # 주문횟수 제외하고 추가
    return sorted(answer)