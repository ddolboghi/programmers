import re
def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub('[^\w\.\_\-]', '', new_id)
    new_id = re.sub('\.{2,}', '.', new_id)
    new_id = re.sub('^\.|\.$', '', new_id)
    if new_id == '':
        new_id = 'a'
    if len(new_id)>=16:
        new_id = new_id[:15]
        new_id = re.sub('\.$', '', new_id)
    if len(new_id)<3:
        new_id = new_id.ljust(3, new_id[-1])
    #st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return new_id