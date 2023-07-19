import re
def solution(str1, str2):
    # 두글자씩 끊을때 영문자만 유효 --> 정규표현식
    set1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if re.match("^[A-Za-z]+$",str1[i:i+2])]
    set2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if re.match("^[A-Za-z]+$",str2[i:i+2])]

    # 각 원소의 개수 세기
    d1 = {i:set1.count(i) for i in set(set1)}
    d2 = {i:set2.count(i) for i in set(set2)}
    print(d1, d2)
    # inner = set(d1) & set(d2)
    inner = [i for i in d1.keys() for j in d2.keys() if i == j]
    outer = set(d1) ^ set(d2)
    innerLength, outerLength = 0, 0
    if len(outer) != 0:
        for i in outer:
            if i in d1.keys():
                outerLength += d1[i]
            else:
                outerLength += d2[i]
    if len(inner) != 0:
        for i in inner:
            innerLength += min(d1[i], d2[i])
            outerLength += max(d1[i], d2[i])
    
    if outerLength == 0:
        return 65536
    else:
        return int((innerLength/outerLength)*65536)