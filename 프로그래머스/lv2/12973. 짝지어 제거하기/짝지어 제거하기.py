def solution(s):
    stack = []
    for i in range(len(s)):
        stack.append(s[i])
        if len(stack)>1 and stack[-2] == stack[-1]:
            stack.pop()
            stack.pop()
    answer = 1 if len(stack)==0 else 0
    return answer