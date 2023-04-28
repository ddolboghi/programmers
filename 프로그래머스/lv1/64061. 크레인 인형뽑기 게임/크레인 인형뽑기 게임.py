def solution(board, moves):
    answer = 0
    d = {}
    for i in range(len(board)):
        col = []
        for row in board:
            if row[i] != 0:
                col.append(row[i])
        d[i+1] = col
    # print(d)
    basket = []
    for loc in moves:
        # d.value의 길이가 0보다 크다면
        if len(d[loc]) > 0:
            if len(basket) == 0:
                # value의 0번째 원소를 basket에 추가
                basket.append(d[loc][0])
            
            # basket의 마지막 원소 == value의 0번째 원소
            # -> basket의 마지막 원소 제거, answer++
            elif basket[-1] == d[loc][0]:
                basket = basket[:-1]
                answer += 2
            else:
                basket.append(d[loc][0])
            
            # value의 0번째 값 삭제
            d[loc] = d[loc][1:]
        else:
            continue
        # print(basket)
    return answer