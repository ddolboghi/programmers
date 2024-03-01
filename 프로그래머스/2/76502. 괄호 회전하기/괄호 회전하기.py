def solution(s):
    answer = 0
    for i in range(0, len(s)):
        if isCorrect(s[i:len(s)]+s[:i]):
            answer += 1
    return answer

def isCorrect(g):
    # g: string
    gs = ["()", "[]", "{}"]
    stack = [g[0]]
    for i in range(1, len(g)):
        if  len(stack) > 0 and (stack[-1] + g[i]) in gs:
            stack.pop()
        else:
            stack.append(g[i])
        # print(i, stack)
    return True if len(stack) == 0 else False