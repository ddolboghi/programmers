n, m = map(int, input().split())
cards = list(map(int, input().split()))

# cards에서 가장 작은 수 2개 더하고 두 수를 더한 값으로 바꿈 -> m번 반복
# 가장 작은 수를 찾고 pop하고 또 가장 작은수 찾고 pop하고 두개 더한 값 2개 추가
for _ in range(m):
    min1 = min(cards)
    cards.remove(min1)
    min2 = min(cards)
    cards.remove(min2)
    
    cards.append(min1+min2)
    cards.append(min1+min2)
print(sum(cards))