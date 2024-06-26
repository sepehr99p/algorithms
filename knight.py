
def isSafe(x, y, board):
    if(x >= 0 and y >= 0 and x < 8 and y < 8 and board[x][y] == -1):
        return True
    return False


def printSolution(n, board):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()

def solveKT(n):

    board = [[-1 for i in range(n)]for i in range(n)]
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    board[0][0] = 0
    steps = 1
    if(not solveKTUtil(n, board, 0, 0, move_x, move_y, steps)):
        print("Solution does not exist")
    else:
        printSolution(n, board)


def solveKTUtil(n, board, curr_x, curr_y, move_x, move_y, steps):
    if(steps == n**2):
        return True

    for i in range(8):
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        if(isSafe(new_x, new_y, board)):
            board[new_x][new_y] = steps
            if(solveKTUtil(n, board, new_x, new_y, move_x, move_y, steps+1)):
                return True
            board[new_x][new_y] = -1
    return False



if __name__ == "__main__":
    solveKT(8)