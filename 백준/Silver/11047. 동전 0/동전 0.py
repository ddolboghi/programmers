input1 = input().split()
N, K = int(input1[0]), int(input1[1])

input2 = [int(input()) for _ in range(N)][::-1]

count = 0
idx = 0

while K > 0 and idx < len(input2):
    if K // input2[idx] < 1:
        idx += 1
    else:
        count += (K // input2[idx])
        K = K - (K // input2[idx]) * input2[idx]

print(count)