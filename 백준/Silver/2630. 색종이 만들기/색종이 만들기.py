# n * n 종이가 모두 같은 숫자인지 체크
# 다른 숫자가 있으면 n//2
# blue, white 키에 종이 개수 누적

# paper를 분할해서 재귀함수에 넘겨주기 --> 실패

# 처음 입력 받은 paper를 그대로 재귀함수에 넘겨주고 
# 분할된 paper의 시작 좌표(좌상단)와 n//2값도 넘겨주기 --> 성공

paper_cnt = {"white":0, "blue":0}

def isAllSameColor(paper, x, y, n):
  init = paper[y][x]
  for i in range(y, y+n):
    for j in range(x, x+n):
      if paper[i][j] != init:
        return False
  return True

def count(paper, x, y, n):
  global paper_cnt
  if isAllSameColor(paper, x, y, n):
    paper_cnt["white"] += 1 if paper[y][x] == 0 else 0
    paper_cnt["blue"] += 1 if paper[y][x] == 1 else 0
  
  else:
    n //= 2
    for i in range(2):
      for j in range(2):
        count(paper, x+n*j, y+n*i, n)

import sys
n = int(input())
paper = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
count(paper, 0, 0, n)

print(*paper_cnt.values())