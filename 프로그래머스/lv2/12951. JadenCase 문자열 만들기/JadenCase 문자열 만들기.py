def solution(s):
    return ' '.join([w[0].upper()+w[1:].lower() if w else w for w in s.split(' ')])