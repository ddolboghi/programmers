r, c = map(int, input().split())
island = [list(input()) for _ in range(r)]

dxy = [(0, -1), (0, 1), (-1, 0), (1, 0)]
sink = []
for i in range(r):
    for j in range(c):
        if island[i][j] == "X":
            adj_sea = 0
            for x, y in dxy:
                xx = j + x
                yy = i + y
                if 0 <= xx < c and 0 <= yy <r:
                    if island[yy][xx] == ".":
                        adj_sea += 1
                else:
                    adj_sea += 1
                    continue
            
            if adj_sea >= 3:
                sink.append((j, i))

for x, y in sink:
    island[y][x] = "."

island_x = []
island_y = []
for i in range(len(island)):
  for j in range(c):
    if island[i][j] == "X":
      island_x.append(j)
      island_y.append(i)

for i in range(min(island_y), max(island_y)+1):
  for j in range(min(island_x), max(island_x)+1):
    print(island[i][j], end="")
  print()