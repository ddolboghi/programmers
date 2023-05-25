def solution(s):
    # stack에 push('(')
    # ) 만나면 pop
    # stack에 원소가 없는데 )가 나오면 false
    # stack에 원소가 남아있으면 false
    answer = True
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    if len(stack) > 0:
        answer = False
    return answer