# 9시 5분 시작
# 9시 48분 종료
def solution(board, moves):
    cursor=[-1]
    k=[] # pop 갯수 세기
    for move in moves:
        for idx in range(0,len(board)):
            if board[idx][move-1]!=0:
                # 바구니 안 마지막 요소와 숫자가 같으면 pop
                if board[idx][move-1]==cursor[-1]:
                    popped=cursor.pop()
                    k.append(popped)
                    board[idx][move-1]=0
                    break
                # 아니라면 더해줌
                else:
                    cursor.append(board[idx][move-1])
                    board[idx][move-1]=0
                    break
    answer=len(k)*2
    return answer