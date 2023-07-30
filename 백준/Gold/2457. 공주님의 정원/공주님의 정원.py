import sys

# 꽃들의 총 개수 N
n = int(sys.stdin.readline())

# 꽃들이 피고 지는 날짜
dates = []
for _ in range(n):
    # 꽃이 피고 지는 날짜에 대해 월에 100을 곱한 뒤, 일이랑 덧셈
    start_m, start_d, end_m, end_d = map(int, sys.stdin.readline().split())
    dates.append([start_m * 100 + start_d, end_m * 100 + end_d])
dates.sort() # 오름차순 정렬

end = 301
cnt = 0
while dates:
    # 첫 시작날짜가 301보다 크면 0 출력해야함
    # 저번 반복의 마지막 끝날짜 > 1130면 cnt만 보면됌 
    #  끝날짜 < 첫 시작날짜면 (앞조건에서 걸렀으므로)비는 날이 생기는 경우만 발생
    if end >= 1201 or dates[0][0] > end:
        break
    
    # end보다 일찍 피는 꽃들 중에서 가장 늦게 지는 꽃 찾기
    temp_end = -1
    for _ in range(len(dates)):
        if dates[0][0] <= end:
            if temp_end <= dates[0][1]:
                temp_end = dates[0][1] # 이전 end보다 크거나 같은 것만 저장
            
            dates.remove(dates[0])
        else:
            break
    
    end = temp_end
    cnt += 1
            
if end < 1201:
    print(0)
else:
    print(cnt)
