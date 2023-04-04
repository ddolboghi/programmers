def solution(n, lost, reserve):
    no_lost_rev = set(lost) & set(reserve)
    real_lost = list(set(lost) - no_lost_rev)
    real_rev = list(set(reserve) - no_lost_rev)
    answer = n - len(real_lost)
    tot_rev = []
    # print(real_lost, real_rev)
    for j in real_lost:
        for i in real_rev:
            print(real_rev)
            if len(real_rev) == 0:
                break
            if j == i-1:
                answer += 1
                real_rev.remove(i)
            elif j == i+1:
                answer += 1
                real_rev.remove(i)
            
    return answer