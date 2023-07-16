# def solution(progresses, speeds):
#     answer = []
#     days = []
#     # 남은 작업일수 계산
#     for p, s in zip(progresses, speeds):
#         day = (100-p)//s
#         if (100-p)%s != 0:
#             day += 1
#         days.append(day)
#     # print(days)
#     i = 0
#     while i < len(days):
#         cnt = 1
#         for j in range(i+1, len(days)):
#             if days[i] < days[j]:
#                 break
#             else:
#                 cnt += 1
#         answer.append(cnt)
#         i += cnt
#     return answer

# def solution2(progresses, speeds):
#     answer = []
#     time = 0
#     count = 0
#     while len(progresses)> 0:
#         if (progresses[0] + time*speeds[0]) >= 100:
#             progresses.pop(0)
#             speeds.pop(0)
#             count += 1
#         else:
#             if count > 0:
#                 answer.append(count)
#                 count = 0
#             time += 1
#     answer.append(count)
#     return answer

def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]