def solution(t, p):
    answer = 0
    for i in range(0,len(t)-len(p)+1,1):
        number = int(t[i:i+len(p)])
        if number <= int(p) :
            answer += 1
        
    return answer