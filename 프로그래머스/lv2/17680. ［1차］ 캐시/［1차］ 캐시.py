def solution(cacheSize, cities):
    answer = 0
    cache = []
    cities = [c.lower() for c in cities ]
    for city in cities:
        # 캐시에 참조값이 없을때 = cache miss
        # 캐시크기보다 작으면 추가
        # 캐시크기보다 크면 가장 오래된 원소 삭제 후 추가
        if not city in cache:
            if len(cache) < cacheSize:
                cache.append(city)
                answer += 5
            else:
                # cache 길이가 0일때는 pop안함
                if len(cache) < 1:
                    answer += 5
                    continue
                cache.pop(0)
                cache.append(city)
                answer += 5
        # 캐시에 참조값이 있을때는 위치 조정 = cache hit
        # index(원소)는 첫번째로 나타나는 원소의 인덱스 반환
        else:
            cache.pop(cache.index(city))
            cache.append(city)
            answer += 1
    return answer