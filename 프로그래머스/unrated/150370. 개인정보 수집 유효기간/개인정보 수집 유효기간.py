def cal_day(a):
    a=a.split('.')
    return int(a[0])*12*28+int(a[1])*28+int(a[2])
def solution(today, terms, privacies):
    today_day = cal_day(today)
    dict_term = {x.split(' ')[0]:int(x.split(' ')[1])*28 for x in terms}
    answer=[]
    for idx,privacy in enumerate(privacies):
        priv = privacy.split(' ')
        
        if cal_day(priv[0])+dict_term[priv[1]]<=today_day:
            answer.append(idx+1)
    print(answer)
    
    return answer