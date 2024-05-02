n, k = map(int, input().split())

# dp 테이블 초기화 (모든 값은 0으로 설정)
dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    w, v = map(int, input().split())  # i번째 물건의 무게와 가치 입력 받기
    for j in range(1, k + 1):
        if j < w:  # 현재 무게 제한 j가 물건의 무게 w보다 작은 경우, 물건을 넣을 수 없음
            dp[i][j] = dp[i-1][j]
        else:  # 물건을 넣을 수 있는 경우
            # 물건을 넣지 않는 경우와 넣는 경우 중 최댓값 선택
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)

# n개의 물건을 고려했을 때, 무게 제한 k일 때의 최대 가치합 출력
print(dp[n][k])
