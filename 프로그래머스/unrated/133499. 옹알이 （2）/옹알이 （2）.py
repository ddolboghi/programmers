def solution(babbling):
    
    dict_bub = {'a':('aya','1'),'y':('ye','2'),'w':('woo','3'),'m':('ma','4')}
    list2=[]
    
    for word in babbling:
        list1 = ['0']*len(word)
        for idx,(i,k) in enumerate(zip(word,list1)):
            if k in ['1','2','3','4']:
                continue
            def gumsa(i,alpha):
                len_bab = len(dict_bub[alpha][0])
                if i==alpha:
                    if word[idx:idx+ len_bab] == dict_bub[alpha][0]:
                        for j in range(idx,idx+len_bab):
                            list1[j]=dict_bub[alpha][1]
            for itering in dict_bub.keys():
                gumsa(i,itering)
            
        list2.append(''.join(list1))
    
    answer=0
    for lists in list2:
        #print(lists)
        if ('1111'in lists) |('222'in lists) |('3333'in lists) |('444' in lists):
            continue
        if '0' not in lists:
            answer += 1

    return answer