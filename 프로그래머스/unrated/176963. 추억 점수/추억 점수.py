def solution(name, yearning, photo):
    answer = []
    dict_ori = {name[i]:yearning[i] for i in range(len(name))}
    for phot in photo:
        jumsu = 0
        for pho in phot:
            if pho in name:
                print(pho,dict_ori[pho])
                jumsu = jumsu + dict_ori[pho]
        answer.append(jumsu)
    return answer