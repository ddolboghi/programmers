h, m = map(int, input().split())
time = int(input())
mm = m + time
if mm >= 60:
    hh = mm // 60
    real_m = mm % 60
    real_h = h + hh
    if real_h == 24:
        print(0, real_m)
    elif real_h >= 25:
        print(real_h % 24, real_m)
    else:
        print(real_h, real_m)
else:
    print(h, mm)