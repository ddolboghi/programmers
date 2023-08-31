def sub(n):
    if n == 3:
        return 4
    elif n == 2:
        return 2
    elif n == 1:
        return 1
    elif n < 1:
        return 0
    else:
        return sub(n-1)+sub(n-2)+sub(n-3)

T = int(input())
for _ in range(T):
    n = int(input())
    print(sub(n))