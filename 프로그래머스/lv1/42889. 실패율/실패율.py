def solution(N, stages):

    tupes=[]
    iters=0
    

    if max(stages) <= 5:
        iters=N+1
    else:
        iters=max(stages)+1

    for i in range(1,N+1,1):

        failures=[x-i for x in stages]

        clearers=[x for x in failures if x>=0]
        
        if len(clearers) != 0:
            if i < N+1:
                tupes.append((i,failures.count(0)/len(clearers)))
            else:
                continue
        else:
            tupes.append((i,0))
        
    so_tupes=sorted(tupes,key= lambda x : x[1], reverse=True)
    answer=[x[0] for x in so_tupes]

    return answer