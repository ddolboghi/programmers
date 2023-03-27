def solution(lottos, win_nums):
    # 0이 모두 당첨 번호 --> 최고 순위
    # 0이 모두 당첨 번호 아니면 --> 최저 순위
    # 최저 순위 = 불일치 번호 개수 + 1, 불일치 5개 이상부터는 6
    # 최고 순위 = 불일치 번호 개수 + 1 - 0 개수
    dif = len(set(win_nums) - set(lottos))
    min_rank = dif + 1 if dif <5 else 6
    zero = len([x for x in lottos if x == 0])
    max_rank = dif if zero==0 and dif==6 else dif - zero + 1
    return [max_rank, min_rank]