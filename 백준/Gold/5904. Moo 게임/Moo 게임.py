def find_string(n, k, total_length):
  if n <= 3:
    return "moo"[n-1]
  
  if n > total_length:
    # 수열 길이 증가시키기
    k += 1
    return find_string(n, k, total_length*2 + k+3)
  
  else:
    prev_length = (total_length-(k+3))//2
    
    # 좌측 구간에 속하는 경우 이전 단계로 돌아가기
    if n <= prev_length: 
      return find_string(n, k-1, prev_length)
    
    # 우측 구간에 속하는 경우 이전 단계로 돌아가기
    # n값을 이전 단계의 moo 길이에 맞게 우측구간 전까지의 길이 빼기
    elif n > prev_length + k+3:
      return find_string(n-prev_length - (k+3), k-1, prev_length)
    
    # 중간 구간에 속하는 경우
    # 좌측 구간 길이 빼면 "m"이 1부터 시작
    else:
      if n-prev_length == 1:
        return "m"
      else:
        return "o"

n = int(input())
print(find_string(n, 0, 3))