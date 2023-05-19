# 9시 5분 시작
# 

def solution(board, moves):


    cursor=[-1]
    k=[]
    
    for move in moves:
        for idx in range(0,len(board)):
            if board[idx][move-1]!=0:
                if board[idx][move-1]==cursor[-1]:
                    popped=cursor.pop()
                    print(popped)
                    k.append(popped)
                    
                    board[idx][move-1]=0
                    break
                else:
                    cursor.append(board[idx][move-1])
                    board[idx][move-1]=0
                    break
    #print(cursor)
    
    answer=len(k)*2
    return answer