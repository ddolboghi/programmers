arr = list(input())

zero, one = arr.count('0')//2, arr.count('1')//2

for _ in range(zero):
  arr.pop(-arr[::-1].index('0')-1)

for _ in range(one):
  arr.pop(arr.index('1'))

print(''.join(arr))