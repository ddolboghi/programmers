import re

def solution(new_id):
    # 1단계
    new_id=new_id.lower()
    print("1단계",new_id)
    # 2단계
    new_id = re.sub(r"[^a-z0-9-_.]","",new_id)
    print("2단계",new_id)
    # 3단계
    new_id = re.sub(r"\.+",".",new_id)
    print("3단계",new_id)
    # 4단계
    if new_id[0]==".":
        new_id=new_id[1:]
    try:
        if new_id[-1]==".":
            new_id=new_id[:len(new_id)-1]
    except:
        new_id=new_id
    
    print("4단계",new_id)
    # 5단계
    if new_id == "": new_id ='a'
    print("5단계",new_id)
    # 6단계
    if len(new_id)>=16:
        new_id=new_id[:15]
        if new_id[14]==".":
            new_id=new_id[:14]
    print("6단계",new_id)
    # 7단계
    while len(new_id) <= 2:
        new_id += new_id[-1]

    answer = new_id
    return answer