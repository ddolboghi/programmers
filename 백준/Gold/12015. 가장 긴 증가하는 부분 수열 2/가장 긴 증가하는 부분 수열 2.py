import sys
import time
n = int(sys.stdin.readline().rstrip())
seq = list(map(int, sys.stdin.readline().rstrip().split()))

memorization = [0]
seq = [0] + seq

for s in seq:
    if memorization[-1] < s:
        memorization.append(s)
    else: #마지막 값이 s보다 작거나 같으면
        left = 0
        right = len(memorization)
    
        while left < right: #s보다 작지만 가장 가까운 값 찾기
            mid = (left + right)//2
            if memorization[mid] < s: 
                left = mid+1
            else: #s보다 작으면서 가장 가까운 값의 위치
                right = mid
        memorization[right] = s

print(len(memorization)-1)