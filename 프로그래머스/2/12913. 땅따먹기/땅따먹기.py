def solution(land):    
    for i in range(1, len(land)):
        for j in range(len(land[i])):
            land[i][j] = max([land[i][j] + land[i-1][k] for k in range(len(land[i-1])) if j != k])

    return max(land[-1])