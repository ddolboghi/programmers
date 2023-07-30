def min_formula(formula):
    # - 사이에 있는 숫자들을 모두 더하고 여기에 -를 각각 붙여서 총합 구하기
    
    # 입력된 식을 -를 기준으로 분리
    subtract_parts = formula.split('-')
    
    # 분리된 부분은 +로만 이뤄진 식이므로 부분 총합을 subtract_parts에 저장
    for i, part in enumerate(subtract_parts):
        add_parts = list(map(int, part.split('+')))
        subtract_parts[i] = sum(add_parts)
    
    # subtract_parts는 -로만 이뤄진 식이므로
    # 첫번째 값에 다른 값들을 모두 빼주면 됨
    result = subtract_parts[0]
    for i in range(1, len(subtract_parts)):
        result -= subtract_parts[i]
    
    return result


# 입력을 받습니다.
formula = input().strip()

# 최소 값을 계산하고 출력합니다.
print(min_formula(formula))
