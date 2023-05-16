def solution(wallpaper):
    answer = []
    s_col, s_row = 50, 50 
    e_col, e_row = 0, 0
    for i in range(len(wallpaper)): 
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                if s_row > i:
                    s_row = i
                if e_row < i+1:
                    e_row = i+1
                if s_col > j:
                    s_col = j
                if e_col < j+1:
                    e_col = j+1 
    return [s_row, s_col, e_row, e_col]