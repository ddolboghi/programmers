def solution(dirs):
    start = (0, 0)
    length = 1
    history = []
    for i in range(len(dirs)):
        end = move(dirs[i], start)
        if (start, end) not in history and (end, start) not in history and start != end:
            history.append((start, end))
        
        start = end
        
    print(len(history), history)
    answer = 0
    return len(history)

def move(dir, pos):
    dx = {"U":0, "D":0, "R":1, "L":-1}
    dy = {"U":1, "D":-1, "R":0, "L":0}
    #pos[0]: x, pos[1]: y
    goX = pos[0] + dx[dir]
    goY = pos[1] + dy[dir]
    x = goX if -5 <= goX <= 5 else pos[0]
    y = goY if -5 <= goY <= 5 else pos[1]
    return (x, y)