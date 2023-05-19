def solution(players, callings):
    
    dict1 = {rank+1:name for rank,name in enumerate(players)}
    dict2 = {name:rank+1 for rank,name in enumerate(players)}
    
    for call in callings:
        k=dict2[call]
        dict2[dict1[k]]-=1
        dict2[dict1[k-1]]+=1
        temp = dict1[k]
        dict1[k]=dict1[k-1]
        dict1[k-1]=temp
        
    #print(dict1,"\n",dict2)
    answer=[]
    for a in dict1.values():
        answer.append(a)
    return answer