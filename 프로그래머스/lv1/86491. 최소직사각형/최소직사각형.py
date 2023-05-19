def solution(sizes):
    temp=0
    new_sizes=[]
    for size in sizes:
        new_size=[]
        if size[0]>size[1]:
            new_size.append(size[0])
            new_size.append(size[1])
        else:
            new_size.append(size[1])
            new_size.append(size[0])
        new_sizes.append(new_size)
    print(new_sizes)
    first_num=[]
    second_num=[]
    for size in new_sizes:
        first_num.append(size[0])
        second_num.append(size[1])
    a=max(first_num)
    b=max(second_num)
    
    answer = a*b
    return answer