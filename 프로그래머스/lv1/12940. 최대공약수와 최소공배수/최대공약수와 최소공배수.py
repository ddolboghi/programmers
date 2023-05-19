def solution(n, m):
    if n<=m:iter=m
    else:iter=n
    mini=[]
    for i in range(1,iter,1):
        if (n%i==0) & (m%i==0):
            mini.append(i)
    answer = [max(mini),(max(mini)) * (m//max(mini)) * (n//max(mini))]
    return answer