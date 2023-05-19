def solution(keymap, targets):
    answer = []
    kstr = ""
    kidx = [0]
    klen = 0
    for k in keymap:
        kstr+=k
        klen+=len(k)
        kidx.append(klen)
    print(kstr,kidx)
    for t in targets:
        cnt_list = []
        for s in t:
            if s not in kstr:
                answer.append(-1)
                break
            else:
                id_list = [kstr[kidx[i]:kidx[i+1]].find(s)+1 for i in range(len(kidx)-1) if kstr[kidx[i]:kidx[i+1]].find(s) != -1]
                cnt_list.append(min(id_list))
                if len(cnt_list) == len(t):
                    answer.append(sum(cnt_list))
    return answer