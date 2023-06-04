def solution(n, words):
    answer = [0, 0]
    fail = 0
    order = 0
    rank = len(words)
    for i in range(len(words)):
        rewords = words[i+1:]
        for j in range(len(rewords)):
            if words[i] == rewords[j] or words[i][-1] != rewords[0][0]:
                if rank > (i+j+1):
                    rank = i+j+1
                    fail = (i+j+1)%n +1
                    order = (i+j+1)//n +1
                    answer = [fail, order]
    return answer