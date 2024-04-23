# 탐색은 가장 작은 n = 1일때만 수행
# n = 1이 될때까지 분할한 뒤에 탐색
# 탐색할때 분할로부터 넘겨받은 x, y 값과 r, c 비교
# 4등분 = 사분면
# 시간 단축위해 r, c가 포함되있지 않은 사분면은 재귀 안돌고 건너뛰기
# 건너뛸때 순서는 가져가야하므로 건너뛴 사분면 넓이만큼 더하기

def visit(n, x, y, order):
  global r, c
  if n == 0:
    if x == c and y == r:
      print(order)
    return order + 1

  half = n // 2
  # 원점
  yh = y+half
  xh = x+half

  # 1사분면
  if r < yh and c < xh:
    return visit(half, x, y, order)
  order += half * half # 사분면에 해당하지 않으면 건너뛴 칸 수 추가

  # 2사분면
  if r < yh and c >= xh:
    return visit(half, xh, y, order)
  order += half * half

  # 3사분면
  if r >= yh and c < xh:
    return visit(half, x, yh, order)
  order += half * half

  # 4사분면
  return visit(half, xh, yh, order)

n, r, c = map(int, input().split())
visit(2**n, 0, 0, 0)