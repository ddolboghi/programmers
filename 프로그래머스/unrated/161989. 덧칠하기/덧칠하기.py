def solution(n, m, section):
    # section의 숫자+m-1까지는 m으로 커버 --> cnt++
    # 다음 숫자가 이전 숫자+m-1 안에 있다면 패스하고
    # 다음 숫자가 이전 숫자+m-1 밖에 있다면 다음숫자부터 m개까지 커버 --> cnt++
    val = 0
    cnt = 0
    for i in section:
        if val < i:
            val = i+m-1
            cnt += 1
        
    return cnt