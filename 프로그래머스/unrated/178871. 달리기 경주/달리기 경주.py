def solution(players, callings):
    d = dict({p:i for i, p in enumerate(players)})
    d_inv = dict({i:p for i, p in enumerate(players)})
    
    for c in callings:
        players[d[c]-1], players[d[c]] = players[d[c]], players[d[c]-1]
        # d 수정
        f = d_inv[d[c]-1] # c 앞 선수 이름
        d[f] = d[c]
        d[c] = d[c]-1
        # d_inv 수정
        d_inv[d[f]] = f
        d_inv[d[c]] = c
    return players