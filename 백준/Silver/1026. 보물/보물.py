n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

#b의 최댓값은 a의 최솟값과 곱해져야함
# b 내림차순 정렬후 인덱스를 키값으로 딕셔너리 만듬
dictB = {i:v for i, v in enumerate(sorted(b, reverse=True))}
dB = dictB.copy()

#원래 b의 순서대로 키값 배열 만듬
kb = []
for i in b:
    for k, v in dB.items():
        if i == v:
            kb.append(k)
            dB.pop(k)
            break

#kb값을 오름차순 정렬한 a의 인덱스로 사용
#kb값을 dictB의 키값으로 사용
a = sorted(a)
result = 0
for x in kb:
    result += dictB[x]*a[x]
    
print(result)