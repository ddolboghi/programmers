def solution(name, yearning, photo):
    answer = []
    
    for i in photo :
        n = 0
        for j in range(len(i)) :
            if i[j] in name :
                n += yearning[name.index(i[j])]
        answer.append(n)
        
    return answer