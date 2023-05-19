def solution(arr1, arr2):
    answer=[]
    for arr1_a,arr2_a in zip(arr1,arr2):
        answer2=[]
        for x,y in zip(arr1_a,arr2_a):
            answer2.append(x+y)
        answer.append(answer2)
    return answer