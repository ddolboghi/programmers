l, c = map(int, input().split())
strs = input().split()

check = [False] * c
def validate(arr):
  m = 0
  for s in arr:
    if s in ["a", "e", "i", "o", "u"]:
      m += 1
  if m > 0 and (len(arr) - m) > 1:
    return True
  else:
    return False

def comb(idx, arr, r):
  global result
  if r == l and validate(arr):
    result.append("".join(sorted(arr)))
    return
  
  for i in range(idx+1, len(strs)):
    if not check[i]:
      check[i] = True
      comb(i, arr + [strs[i]], r + 1)
      check[i] = False

result = []
comb(-1, [], 0)
for r in sorted(result):
  print(r)