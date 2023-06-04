def solution(brown, yellow):
    answer = []
    # brown = yellow로 만들수 있는 가로 * 세로 + 4
    for i in range(1, int(yellow**0.5)+1):
        width = yellow // i
        height = i
        if (width+height) == (brown-4)//2:
            answer = [width+2, height+2]
    return answer