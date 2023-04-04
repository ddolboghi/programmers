def solution(cards1, cards2, goal):
    answer = 'Yes'
    a, b = 0, 0
    
    for i in goal :
        if i == cards1[a] :
            a+=1
            print('a')
        elif i == cards2[b] :
            b+=1
            print('b')
        else :
            answer = 'No'
            break
        if a==len(cards1) :
            a = 0
        elif b==len(cards2) :
            b = 0
        
    return answer