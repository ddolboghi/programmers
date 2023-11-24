from collections import deque
# 각 큐에서 pop하면 다른 큐에 자동으로 append
# --> 한번의 pop = 작업 1회
def solution(queue1, queue2):
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum1, sum2 = sum(q1), sum(q2)
    if (sum1 + sum2) % 2 == 0:
        goal = (sum1 + sum2) // 2
    else:
        return -1
        
    case = (len(q1) + len(q2))*2 
    while sum1 != goal or sum2 != goal:     
        if answer >= case:
            answer = -1
            break
        
        if sum1 < goal:
            v2 = q2.popleft()
            sum2 -= v2
            q1.append(v2)
            sum1 += v2
            answer += 1
            
        elif sum2 < goal:
            v1 = q1.popleft()
            sum1 -= v1
            q2.append(v1)
            sum2 += v1        
            answer += 1
            
    return answer