# 8시 42분 시작
def cal_func(func):
    first=func[0]
    dict1={first:1,'others':0}
    s1=func[1::]
    i=0
    numb=1
    while dict1[first]!=dict1['others']:
        if s1[i]==first:
            dict1[first]+=1
            i+=1
        else:
            dict1['others']+=1
            i+=1
    return func[i+1:]
def solution(s):
    answer = 0
    while s!="":
        answer+=1
        try:
            s=cal_func(s)
            #print(s)
        except:
            break
    
    #print(cal_func(s))
    
    return answer