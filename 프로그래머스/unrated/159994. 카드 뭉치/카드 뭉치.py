def solution(cards1, cards2, goal):
    # cards1, cards2각각 순서대로 가면서 goal 원소와 같은지 비교
    # cards의 첫번째 원소부터 같아야함 --> 같으면 첫번째 원소 제거
    # 길이 > 0 --> No
    for g in goal:
        if len(cards1) and g == cards1[0]: cards1.pop(0)
        elif len(cards2) and g == cards2[0]: cards2.pop(0)
        else: return 'No' 
    return 'Yes'