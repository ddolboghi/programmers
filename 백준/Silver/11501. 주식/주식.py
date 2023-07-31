import sys
t = int(input())
for _ in range(t):
    n = int(input())
    stocks = list(map(int, input().split()))
    
    # 끝에서부터 최대값을 찾아 
    # 다음값이 최대값보다 작으면 차를 더하고
    # 다음값이 최대값보다 크면 최대값 갱신
    result = 0
    max_ = 0
    for i in range(len(stocks)-1, -1, -1):
        if stocks[i] > max_:
            max_ = stocks[i]
        else:
            result += max_ - stocks[i]
    print(result)