def solution(a, b):
    
    # 2월은 29일까지
    # 31일까지인 달: 1,3,5,7,8,10,12
    # 30일까지인 달: 4,6,9,11
    # 2016년 1월 1일은 금요일
    
    day=0
    month_30=[4,6,9,11]
    month_31=[1,3,5,7,8,10,12]
    days=["THU","FRI","SAT","SUN","MON","TUE","WED"]
    for month in range(1,a,1):
        if month in month_30:
            day=day+30
        elif month in month_31:
            day=day+31
        else:
            day=day+29
    day=day+b
    index = day%7
    answer = days[index]
    
    return answer