def solution(babbling):
    # 정답, a의 인덱스, babbling의 인덱스
    answer, i, j = 0, 0, 0
    a = ["aya", "ye", "woo", "ma"]

    # a을 순차적으로 돎
    while(i<4) :
        # a가 babbling[j]에 있으면 인덱스번호로 교체  
        if a[i] in babbling[j] :
            babbling[j] = babbling[j].replace(a[i], str(i), 1)
        # 없으면 babbling의 다음 인덱스
        else : 
            j += 1
        # j가 babbling의 길이와 같으면 끝!
        if j==(len(babbling)) :
            i+=1
            j=0
    print(babbling)
    # 연속되면 숫자 제거
    # isdigit()=True인 갯수 세기
    for k in babbling :
        tmp = 0
        if k.isdigit() == True :
            for m in range(len(k)-1) :
                if k[m] == k[m+1] :
                    tmp = 1
                else :
                    tmp = 0
                if tmp == 1 :
                    break
        else :
            tmp = 1
        if tmp == 0 :
            answer += 1
    return answer