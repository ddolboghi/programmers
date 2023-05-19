def solution(survey, choices):
    mbti={'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    for idx,q in enumerate(survey):
        if choices[idx]<4:
            mbti[q[0]]+=(4-choices[idx])
        elif choices[idx]>4:
            mbti[q[1]]+=(choices[idx]-4)
        else:
            continue
    answer_list=[]
    cheating=['R','C','J','A']
    for i in range(0,4):
        mylist=list(mbti.items())
        if (mylist[2*i][1]<mylist[2*i+1][1]):
            answer_list.append(mylist[2*i+1][0])
        elif (mylist[2*i][1]>mylist[2*i+1][1]):
            answer_list.append(mylist[2*i][0])
        else:
            answer_list.append(cheating[i])
    
    answer=''.join(answer_list)
    return answer