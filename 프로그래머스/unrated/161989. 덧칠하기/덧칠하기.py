def solution(n, m, section):
    section = sorted(section)
    answer = 1
    i , a = 0, 0
    
    while(a != -1) :
        # m씩 처리해야함
        if section[i] not in range(section[a], section[a]+m) :
            a = i
            answer += 1

        # 하나라도 인덱스 초과하면 에러남, 끝이므로 break
        if a>=len(section)-1 or i>=len(section)-1 :
            a = -1
        i+=1
    return answer