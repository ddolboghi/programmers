def solution(order):
    answer = 0
    put = [False] * len(order)
    assist = []
    prev = 0
    for o in order:
        for i in range(prev+1, o):
            if not put[i-1]:
                assist.append(i)
                put[i-1] = True
        # print(o, assist)
        if put[o-1]:
            if assist[-1] == o:
                assist.pop()
                answer += 1
            else:
                break
        else:
            put[o-1] = True
            answer += 1
            
        prev = o
        
    return answer