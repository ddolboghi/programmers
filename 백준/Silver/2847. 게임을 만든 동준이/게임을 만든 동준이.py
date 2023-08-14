# 제출용
import sys
N = int(sys.stdin.readline())
input1 = [int(sys.stdin.readline().strip()) for i in range(N)]

input2 = input1[::-1]
summed=0
for i in range(N):
    if i == N-1:
        break
    if input2[i+1] >= input2[i]:
        summed += input2[i+1]-input2[i]+1
        input2[i+1]=input2[i]-1
        
print(summed)