def solution(X, Y): 
    d = {}
    eq = sorted((set(X) & set(Y)), reverse=True)
    for i in eq:
        d[i] = min(X.count(i),Y.count(i))
        X = X.replace(i, '')
        Y = Y.replace(i, '')
    # print(d)
    jg = ''
    for k, v in d.items():
        jg += k * v
    if len(jg) == 0:
        return '-1'
    elif jg[0] == '0':
        return '0'
    else:
        return jg