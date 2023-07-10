def solution(elements):
    sums = []
    for k in range(1,len(elements)):
        for i in range(len(elements)):
            if i+k > len(elements):
                x = sum(elements[i:]+elements[:(i+k)%len(elements)])
                sums.append(x)
            else:
                x = sum(elements[i:i+k])
                sums.append(x)
    
    sums.append(sum(elements))
    # print(set(sums))
    return len(set(sums))