def solution(X, Y):
    answer = ''
    # 각 자리수별로 숫자 카운트(0~9)
    X_count, Y_count = [0] * 10, [0] * 10

    for x in X:
        X_count[int(x)] += 1
    for y in Y:
        Y_count[int(y)] += 1
    
    # 공통인 숫자
    common = set(str(X)) and set(str(Y))
    
    # 공통된 숫자에 대해, X와 Y에서 해당 숫자가 나타나는 개수 중 작은 값
    counts = [min(X_count[int(d)], Y_count[int(d)]) for d in common]
    
    # 선택한 개수만큼 숫자 이어붙이기
    for d, c in sorted(zip(common, counts), reverse=True):
        answer += d * c
    
    if answer == '':
        return '-1'
    elif set(answer) == {'0'}:
        return '0'
    else:
        return answer
