from itertools import permutations as p
def solution(k, dungeons):
    k_copy = k
    max_ = 0
    for dun in p(dungeons):
        cnt = 0
        # print(dun)
        for d in dun:
            if d[0] <= k:
                k -= d[1]
                cnt += 1
                # print(k)
        k = k_copy
        if max_ <= cnt:
            max_ = cnt
    # print(f"max_: {max_}")
    return max_