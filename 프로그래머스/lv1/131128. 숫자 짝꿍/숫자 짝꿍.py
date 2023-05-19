#from collections import Counter
def make_dict(a):
    dict1={'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
    for i in a:
        dict1[i]+=1
    return dict1

def solution(X, Y):
    
    x_counter=make_dict(X)
    y_counter=make_dict(Y)

    sorted_x_counter = list(x_counter.values())[::-1]
    sorted_y_counter = list(y_counter.values())[::-1]
    
    answer=[]
    for idx,i in enumerate(zip(sorted_x_counter,sorted_y_counter)):
        answer.append((str(9-idx))*int('{}'.format(min(i))))
    
    answer = "".join(answer)
    #print(set(answer))
    if set(answer)=={'0'}:
        answer='0'
    elif answer == "":
        answer='-1'
    else:
        answer=answer
    return answer