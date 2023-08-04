n = int(input())
num = [int(input()) for _ in range(n)]


# 내림차순 정렬
num = sorted(num, reverse=True)

result = 0
flag = 0
if len(num) > 1:
    for i in range(0, len(num), 2):
        if i+1 <= len(num)-1 and num[i+1] > 1:
            result += (num[i]*num[i+1])
            flag = i+2

        if num[-2] < 0:
            result += num[-1]*num[-2]
            num.pop(-1)
            num.pop(-1)

            
if 0 in num[flag:]:
    result += sum(num[flag:num.index(0)])

else:
    result += sum(num[flag:])

print(result)