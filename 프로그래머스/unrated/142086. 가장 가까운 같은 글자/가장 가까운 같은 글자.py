def solution(s):
    answer = []
    word_dict = {}
    for i in range(0,len(s),1) :
        if  s[i] not in word_dict.keys() :
            word_dict[s[i]] = i
            answer.append(-1)
        else :
            answer.append(i - word_dict[s[i]])
            word_dict[s[i]] = i
            
    return answer