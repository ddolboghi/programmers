def solution(s):
    answer = 0
    isCorrect = 0
    for i in range(len(s)):
        rot = s[i:]+s[:i]
        stack = []
        for r in rot:
            isCorrect = int(correct(r, stack))
        if isCorrect == 1:
            answer += 1
    return answer

def correct(string, stack):
    if not len(stack):
        stack.append(string)
        
    else:
        stack.append(string)
        if stack[-2:] == ['(',')']:
            stack.pop()
            stack.pop()
        elif stack[-2:] == ['{','}']:
            stack.pop()
            stack.pop()
        elif stack[-2:] == ['[',']']:
            stack.pop()
            stack.pop()
    return len(stack) == 0
    