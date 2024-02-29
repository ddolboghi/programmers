import math
def solution(progresses, speeds):
    answer = []
    # 가장 오래 걸리는 기간을 갱신
    # 갱신될때 answer에 배열 길이 추가 후 배열 비우기
    maxDay = math.ceil((100-progresses[0])/speeds[0])
    realese = 1
    for i in range(1, len(speeds)):
        day = math.ceil((100-progresses[i])/speeds[i])
        if day > maxDay:
            maxDay = day
            answer.append(realese)
            realese = 0
            
        realese += 1
        
        # print(realese, maxDay, answer)
    answer.append(realese)
    return answer 