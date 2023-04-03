def solution(X, Y):
    # 1. X와 Y의 각 자리수별로 나타나는 숫자를 카운트합니다.
    X_count = [0] * 10
    Y_count = [0] * 10
    for x in X:
        X_count[int(x)] += 1
    for y in Y:
        Y_count[int(y)] += 1
    
    # 2. X와 Y에서 공통으로 나타나는 숫자들을 찾습니다.
    common_digits = set(str(X)) & set(str(Y))
    
    # 3. 각 공통된 숫자에 대해, X와 Y에서 해당 숫자가 나타나는 개수 중 작은 값을 선택합니다.
    counts = [min(X_count[int(d)], Y_count[int(d)]) for d in common_digits]
    
    # 4. 선택한 개수만큼 숫자를 이어붙여서 가장 큰 수를 만듭니다.
    result = ''
    for d, c in sorted(zip(common_digits, counts), reverse=True):
        result += d * c
    
    if result == '':
        return '-1'
    elif set(result) == {'0'}:
        return '0'
    else:
        return result
