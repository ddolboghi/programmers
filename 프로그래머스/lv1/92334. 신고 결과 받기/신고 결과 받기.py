def solution(id_list, report, k):
    email = dict({i:0 for i in id_list})
    res = dict({i:[] for i in id_list})
    for r in report:
        res[r.split()[1]].append(r.split()[0])
        res[r.split()[1]] = list(set(res[r.split()[1]]))
    # print(res)
    
    for i,v in res.items():
        if len(v) >= k:
            for j in v:
                email[j] += 1
    # print(email)
    return list(email.values())