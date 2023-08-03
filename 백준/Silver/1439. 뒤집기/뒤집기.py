S = input()

# S에서 1이 연속되는 문자열과 0이 연속되는 문자열 개수를 각각 저장해서
# 더 작은 개수가 정답
one = ''
zero = ''
one_cnt = 0
zero_cnt = 0
for i in S:
    if i == '1':
        if zero != '':
            zero_cnt += 1
        zero = ''
        one += i
        
    else:
        if one != '':
            one_cnt += 1
        one = ''
        zero += i
        
if one != '':
    one_cnt += 1
    
if zero != '':
    zero_cnt += 1
        
print(min(one_cnt, zero_cnt))