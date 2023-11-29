def solution(cap, n, deliveries, pickups):
    answer = 0
    d, p = 0, 0 # 택배, 빈 상자 누적 값
    # 누적 값들 중 하나라도 0보다 크면 0이하가 될때까지 둘다 cap을 반복해서 뺌
    # 둘다 빼는 이유는 그 위치에서 택배(빈상자)가 담을 수 있는 용량보다 많으면 
    # 오고가며 빈상자(택배)를 담을 수 있기때문
    for i in range(n-1, -1, -1):
        d += deliveries[i]
        p += pickups[i]
        
        while d > 0 or p > 0:
            d -= cap
            p -= cap
            answer += (i+1)*2
            
    return answer