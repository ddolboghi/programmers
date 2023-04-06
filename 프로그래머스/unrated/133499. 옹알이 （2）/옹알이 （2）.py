# def solution(babbling):
#     # value의 첫번째 값은 해당 문자의 길이, 두번째는 인덱스
#     dict_bub = {'aya':(3,0), 'ye':(2,1), 'woo':(3,2), 'ma':(2,3)}
#     count = 0
#     temp = -1
#     for word in babbling:
#         compare = 0
#         print("word의 길이:", len(word))
#         for i in dict_bub.keys():
#             if i in word:
#                 if (dict_bub[i][1] != temp) :
#                     compare = compare + dict_bub[i][0]
#                     temp = dict_bub[i][1]
#         if (compare == len(word)):
#             count =+ 1
    
#     answer = count
#     return answer
# def solution(babbling):
#     # value의 첫번째 값은 해당 문자의 길이, 두번째는 인덱스
#     dict_bub = {'aya':0, 'ye':1, 'woo':2, 'ma':3}
#     count = 0
    
#     check_list=[]
#     for word in babbling:
#         compare = 0
#         temp = -1
#         print("word의 길이:", len(word))
#         for i in dict_bub.keys():
#             if i in word:
#                 if (dict_bub[i] != temp) :
#                     compare = compare + len(i)
#                     print("변경전",temp)
#                     temp = dict_bub[i]
                    
#         if (compare == len(word)):
#             count += 1
#             check_list.append(True)
#         else:
#             check_list.append(False)
#     print(check_list)
    
#     answer = count
#     return answer
def solution(babbling):
    # value의 첫번째 값은 해당 문자의 길이, 두번째는 인덱스
    dict_bub = {'aya':0, 'ye':1, 'woo':2, 'ma':3}
    list2=[]
    for word in babbling:
        list1 = ['0']*len(word)
        for idx,(i,k) in enumerate(zip(word,list1)):
            if k in ['1','2','3','4']:
                continue
            if i=='a':
                if word[idx:idx+3] == 'aya':
                    for j in range(idx,idx+3):
                        list1[j]='1'
            if i=='y':
                if word[idx:idx+2] == 'ye':
                    for j in range(idx,idx+2):
                        list1[j]='2'
            if i=='w':
                if word[idx:idx+3] == 'woo':
                    for j in range(idx,idx+3):
                        list1[j]='3'
            if i=='m':
                if word[idx:idx+2] == 'ma':
                    for j in range(idx,idx+2):
                        list1[j]='4'
                    
        list2.append(''.join(list1))
    
    answer=0
    for lists in list2:
        #print(lists)
        if ('1111'in lists) |('222'in lists) |('3333'in lists) |('444' in lists):
            continue
        if '0' not in lists:
            answer += 1
    
    
    return answer