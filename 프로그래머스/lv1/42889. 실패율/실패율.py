def solution(N, stages):
    # 1부터 N까지 1씩 증가하는 i
    # 스테이지 도달 but not 클리어 플레이어 수 f = i와 같은 stages의 원소 개수
    # 스테이지 도달 플레이어수 p = i보다 크거나 같은 stages의 원소 개수
    # N = 5
    # stages = [2,2,2,2]
    fail_list = []
    # st = sorted(stages)
    for i in range(1, N+1):
        f = 0
        p = 0
        for j in stages:
            if i <= j:
                p += 1
            else:
                pass
            if i == j:
                f += 1
            else:
                pass
        if p == 0:
            fail_list.append((i, 0))
        else:
            fail_list.append((i, f/p))
        # print(i, f, p)
    # print(fail_list)
    # 실패율이 높은 순, 스테이지가 낮은 순 정렬
    sort_list = sorted(fail_list, key=lambda x:x[1], reverse=True)
    answer = [x[0] for x in sort_list]
    return answer