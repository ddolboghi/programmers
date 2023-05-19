def solution(s):
    answer=[]
    for idx, alph in enumerate(s):
        if alph in s[:idx]:
            for i in range(idx-1,-1,-1):
                if alph == s[i]:
                    answer.append(idx-i)
                    break
        else :
            answer.append(-1)
    return answer