def solution(s, skip, index):
    answer = ''
    tot = 'abcdefghijklmnopqrstuvwxyz'
    for k in skip:
        tot = tot.replace(k, '')

    for i in range(len(s)):
        for j in range(len(tot)):
            if s[i] == tot[j]:
                num = (j+index) % len(tot) if (j+index) >= len(tot) else j+index
                answer += tot[num]
    return answer