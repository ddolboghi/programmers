def solution(want, number, discount):
    answer = 0
    d = dict({i:j for i, j in zip(want, number)})
    
    for i in range(len(discount)-9):
        empty = dict({i:0 for i in want})
        for j in discount[i:i+10]:
            if j in d.keys():
                empty[j] += 1
        if empty == d:
            answer += 1
                
        
            
    print(empty)
    return answer