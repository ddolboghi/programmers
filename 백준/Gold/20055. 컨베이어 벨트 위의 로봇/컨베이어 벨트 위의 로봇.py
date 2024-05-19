from collections import deque

n, k = map(int, input().split())
arr = list(map(int, input().split()))
robot = [False] * n
result = 0

while arr.count(0) < k:
  # 벨트 회전
  arr = [arr[2*n-1]] + arr[:2*n-1]
  robot = [robot[n-1]] + robot[:n-1]

  # 로봇 제거
  robot[n-1] = False

  for i in range(n-2, -1, -1):
    # 로봇 이동
    if robot[i] and not robot[i+1] and arr[i+1] > 0:
      robot[i+1] = True
      robot[i] = False
      arr[i+1] -= 1

  # 로봇 제거
  robot[n-1] = False
  
  # 로봇 올리기
  if not robot[0] and arr[0] > 0:
    robot[0] = True
    arr[0] -= 1
  
  result += 1

print(result)