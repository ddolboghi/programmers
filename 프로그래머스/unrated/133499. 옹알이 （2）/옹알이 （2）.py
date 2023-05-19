def solution(babbling):
    answer = 0
    d = {'aya':'1','ye':'2','woo':'3','ma':'4'}
    # 각 단어를 숫자로 바꾸기
    # 없는 단어가 있다면 int변환 안되므로 리스트에 안넣음
    words = []
    for bab in babbling:
        for i, v in d.items():
            bab = bab.replace(i, v)
        try:
            words.append(int(bab))
        except:
            continue
    # print(words)    
    # 단어에서 어떤 숫자의 이전/이후 숫자가 같지 않으면 answer++
    
    for word in words:
        temp, cnt = '', 0
        word = str(word)
        for w in word:
            if temp != w:
                temp = w
            else:
                cnt += 1
        if cnt == 0:
            answer += 1
    return answer