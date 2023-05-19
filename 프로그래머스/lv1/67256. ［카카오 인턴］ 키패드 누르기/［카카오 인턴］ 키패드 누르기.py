def cal_dist(tup1,tup2):
    x = abs(tup1[0]-tup2[0])
    y = abs(tup1[1]-tup2[1])
    return x+y
def solution(numbers, hand):
    jwapyo = {1 : (0,0), 2 : (0,1), 3 : (0,2),
              4 : (1,0), 5 : (1,1), 6 : (1,2),
              7 : (2,0), 8 : (2,1), 9 : (2,2),
              '*':(3,0), 0 : (3,1),'#': (3,2)}
    L = [1,4,7,'*']
    R = [3,6,9,'#']
    answer_list = []
    current_Lloc = '*'
    current_Rloc = '#'
    for i in numbers :
        print(current_Lloc,current_Rloc)
        if i in L : 
            answer_list.append('L')
            current_Lloc = i
            continue
        elif i in R :
            answer_list.append('R')
            current_Rloc = i
            continue
        else:
            if (cal_dist(jwapyo[current_Lloc],jwapyo[i]))<\
            (cal_dist(jwapyo[current_Rloc],jwapyo[i])):
                answer_list.append('L')
                current_Lloc = i
                continue
            elif (cal_dist(jwapyo[current_Lloc],jwapyo[i]))>\
            (cal_dist(jwapyo[current_Rloc],jwapyo[i])):
                answer_list.append('R')
                current_Rloc = i
                continue
            else:
                if hand == "right":
                    answer_list.append('R')
                    current_Rloc = i
                    continue
                else:
                    answer_list.append('L')
                    current_Lloc = i # 여기 corrent_Lloc이라고 오타가 있었음...
                    continue
    #print(answer_list)
    answer = ''.join(answer_list)     
    return answer