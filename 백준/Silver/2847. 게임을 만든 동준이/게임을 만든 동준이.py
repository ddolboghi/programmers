n = int(input())
scores = [int(input()) for _ in range(n)]

# scores를 뒤집어서 큰것부터 다음 원소와 비교해
# 다음원소가 더 클경우 이전원소-1로 교체
result = 0
for i in range(n-1, 0, -1):
    if scores[i] <= scores[i-1]:
        temp = scores[i-1]
        scores[i-1] = scores[i]-1
        result += (temp - scores[i-1])
        
print(result)