def solution(n, lost, reserve):
    # 중복된 학생 제거
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)


    # 체육복 빌려주기
    for i in reserve_set:
        i1 = i-1
        i2 = i+1
        if i1 in lost_set:
            lost_set.remove(i1)
        elif i2 in lost_set:
            lost_set.remove(i2)

    answer = n - len(lost_set)
    return answer