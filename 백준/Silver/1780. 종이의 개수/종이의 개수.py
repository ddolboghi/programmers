# 모든 원소가 같은지 확인
def check(matrix, x, y, n):  
  init = matrix[x][y]
  for i in range(x, x+n):
    for j in range(y, y+n):
      if matrix[i][j] != init:
        return False
  return True

def divide(matrix, x, y, n):
  # 모든 원소가 같다면
  if check(matrix, x, y, n):  
    return [1 if matrix[x][y] == -1 else 0, 1 if matrix[x][y] == 0 else 0, 1 if matrix[x][y] == 1 else 0]
  
  # 모든 원소가 같지 않으면 9등분
  n //= 3
  result = [0, 0, 0] # 각 숫자로 채워진 종이 개수
  
  # 이중반복문으로 9등분 구현
  for i in range(3):
    for j in range(3):
      b = divide(matrix, x + i*n, y + j*n, n)
      result = [result[0] + b[0], result[1] + b[1], result[2] + b[2]] # 반복마다 result값 누적됨
  return result

import sys
n = int(input())
matrix = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

minus, zero, plus = divide(matrix, 0, 0, n) # result[0], result[1], result[2]와 같음
print(minus)
print(zero)
print(plus)
