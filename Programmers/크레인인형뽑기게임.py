def solution(board, moves):
    count = 0
    move_count = 0
    crane_stack = []
    moves = [move-1 for move in moves]

    for idx, move in enumerate(moves):

        for i in range(len(board)):
            if board[i][move] != 0:
                crane_stack.append(board[i][move])
                board[i][move] = 0
                break
            if i == len(board) - 1:
                move_count -= 1

        if move_count > 0:
            if crane_stack[move_count-1] == crane_stack[move_count]:
                crane_stack = crane_stack[:move_count-1]
                move_count -= 2
                count += 2

        move_count += 1

    return count

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))