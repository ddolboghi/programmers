def solution(lottos, win_nums):
    answer = [] #최고순위, 최저순위
    low = 1
    zero = lottos.count(0)
        
    # 틀린갯수 + 1 = 등수 : 틀린갯수 5개 이상이면 그냥 6등
    # 최저 ) 틀린갯수 + 1 : 0도 다 틀린거라고 생각
    for i in lottos :
        if i not in win_nums :
            low += 1
    if low >= 6 :
        low = 6
        
    # 최고 ) 틀린갯수 + 1 - 0갯수 : 0을 다 맞춘거라고 생각
    # 만약 틀린갯수 + 1 - 0갯수 가 0이하면 그냥 1등
    if low - zero <= 0 :
        zero = low - 1
        
    answer = [low-zero, low]
    return answer