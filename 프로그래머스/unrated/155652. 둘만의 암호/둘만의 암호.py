def solution(s, skip, index):
    alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    alphabet=sorted(list(set(alphabet)-set(skip)))
    answer = ''
    for alpha in s:answer+=alphabet[(alphabet.index(alpha)+index)%len(alphabet)]
    return answer