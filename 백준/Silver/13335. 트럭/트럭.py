n, w, L = map(int, input().split())

trucks = list(map(int, input().split()))

# 트럭이 다리에 한칸 들어왔을때부터 완전히 나갈때까지 거리 계산
bridge = [[trucks[0], 1]] # (트럭, 이동한 거리)

# 다음 트럭 + sum(bridge)가 L보다 작으면 트럭 추가
# 가장 앞의 트럭만 거리 계산해서 다리 다 건넜으면 제거

time = 1
i = 1
while bridge:
  time += 1

  # 가장 앞의 트럭이 다리 다 건넜으면 제거
  if bridge[0][1] >= w:
    bridge.pop(0)

  # 트럭 이동시키기
  # 이때 bridge는 w, L 범위 내
  weight = 0
  for truck in bridge:
    truck[1] += 1
    weight += truck[0]

  # 다음 트럭 추가하기
  if i < n and weight+trucks[i] <= L:
    bridge.append([trucks[i], 1])
    i += 1

  # print(bridge)

print(time)