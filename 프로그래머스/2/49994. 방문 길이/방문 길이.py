def solution(dirs):
    history = []
    dxy = {"U":(0, 1), "D": (0, -1), "R": (1, 0), "L": (-1, 0)}
    start = (0, 0)
    for d in dirs:
        xx = start[0] + dxy[d][0]
        yy = start[1] + dxy[d][1]
        x = xx if -5 <= xx <= 5 else start[0]
        y = yy if -5 <= yy <= 5 else start[1]
        end = (x, y)
        if (start, end) not in history and (end, start) not in history and start != end:
            history.append((start, end))
        start = end
    return len(history)