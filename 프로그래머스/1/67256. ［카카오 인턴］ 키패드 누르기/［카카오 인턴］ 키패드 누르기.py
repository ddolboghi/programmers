def solution(numbers, hand):
    answer = ''
    pad = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    loc = {pad[r][c]:[r, c] for r in range(len(pad)) for c in range(len(pad[r]))}
    h = {'L':'*', 'R':'#'}
    for i in range(len(numbers)):
        if numbers[i] in [1,4,7]:
            answer += 'L'
            h['L'] = numbers[i]
        elif numbers[i] in [3,6,9]:
            answer += 'R'
            h['R'] = numbers[i]
        # 2580이면 직전 위치로부터 맨해튼 거리 구하기
        else:
            l_dis = abs(loc[h['L']][0]-loc[numbers[i]][0])+abs(loc[h['L']][1]-loc[numbers[i]][1])
            r_dis = abs(loc[h['R']][0]-loc[numbers[i]][0])+abs(loc[h['R']][1]-loc[numbers[i]][1])
            print(h, l_dis, r_dis)
            if l_dis == r_dis:
                x = hand[0].upper()
                answer += x
                h[x] = numbers[i]
            elif l_dis > r_dis:
                answer += 'R'
                h['R'] = numbers[i]
            else:
                answer += 'L'
                h['L'] = numbers[i]
            
            
    
    return answer