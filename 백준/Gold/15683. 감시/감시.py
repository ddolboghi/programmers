import copy

n, m = map(int, input().split())
office = []
cctv = []
for i in range(n):
    office.append(list(map(int, input().split())))
    for j in range(m):
        if 1<=office[i][j]<=5:
            cctv.append((office[i][j], i, j))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

cctvMode = [[],
            [[0], [1], [2], [3]],
            [[0, 1], [2, 3]],
            [[0, 2], [1, 2], [0, 3], [1, 3]],
            [[0,2,3], [1,2,3], [0,1,2],[0,1,3]],
            [[0,1,2,3]]]

# 모든 경우의 수 파악, dfs 이용
def monitoring(officeCopy, direction, x, y):
    for i in direction:
        xx = x
        yy = y
        while True:
            xx += dx[i]
            yy += dy[i]
            if xx<0 or xx>=m or yy<0 or yy>=n:
                break
            if officeCopy[yy][xx] == 6:
                break
            elif officeCopy[yy][xx] == 0:
                officeCopy[yy][xx] = 7


def dfs(cctvNum, office):
    global minValue
    if cctvNum == len(cctv):
        cnt = 0
        # 매번 탐색하는 경우가 끝날때마다 사각지대 개수 갱신 
        for i in range(n):
            cnt += office[i].count(0)
        minValue = min(minValue, cnt)
        return

    officeCopy = copy.deepcopy(office)
    num, y, x = cctv[cctvNum]
    for direction in cctvMode[num]:
        monitoring(officeCopy, direction, x, y)
        dfs(cctvNum+1, officeCopy)
        # 한번에 하나의 방향만 탐색하므로 다음 반복때는 원본 office 필요
        officeCopy = copy.deepcopy(office)

minValue = int(1e9)
dfs(0, office)
print(minValue)