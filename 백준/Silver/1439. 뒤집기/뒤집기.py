s = input()
flag="Start"
group_1=0
group_0=0
for i in s:
    if (i=="1") and (flag=="Start"):
        group_1+=1
        flag="False"
        continue
    elif (i=="0") and (flag=="Start"):
        group_0+=1
        flag="True"
        continue
    elif (i=="1") and (flag=="True"):
        group_1+=1
        flag="False"
        continue
    elif (i=="1") and (flag=="False"):
        continue
    elif (i=="0") and (flag=="False"):
        group_0+=1
        flag="True"
        continue
    elif (i=="0") and (flag=="True"):
        continue
print(min(group_1, group_0))