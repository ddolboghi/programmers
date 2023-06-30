def solution(n):
    ans = 0
    # 순간이동으로 이동하는 거리 = 현재까지 온거리
    # 전체 거리가 1이 될때까지 2로 나누고 모든 나머지 + 마지막 몫 1 = 건전지 사용량
    while n > 1:
        ans += n%2
        n = n//2
    return ans+n