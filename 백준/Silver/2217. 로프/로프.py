n = int(input())
ropes = [int(input()) for _ in range(n)]

ropes = sorted(ropes, reverse=True)
max_weight = 0
for i in range(n):
    if (ropes[i] * (i+1)) > max_weight:
        max_weight = ropes[i] * (i+1)
        
print(max_weight)