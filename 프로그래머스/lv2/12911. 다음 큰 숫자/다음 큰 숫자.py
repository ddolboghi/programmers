def solution(n):
    one = bin(n)[2:].count('1')
    # 1001 110 -> 1010 011
    # 1 다음 0이 처음으로 나오는 부분의 1과 0 swap
    # swap된 숫자에서 바뀐 부분 이하의 부분이 1개수 유지하며 가장 작도록
    # 이하부분에서 1개수 세고 1의 자리부터 1로 채우기
    m = n+1
    while m > n:
        if bin(m)[2:].count('1') == one:
            break
        m += 1
    return m