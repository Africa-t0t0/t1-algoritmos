import numpy as np
import treelib

def line_of_sight(x, y, n, board):
    aux_x = x 
    aux_y = y
    # check diagonal derecha 
    for aux_x in range(aux_x, n):
        if aux_y+1<=n:
            aux_y+=1
        if board[aux_x, aux_y-1] != '1':
        # check derecha
            if aux_x == n:
                aux_x = x
                aux_y = y
                for x in range(aux_x, n):
                    if board[aux_x, aux_y] != '1':
                        board[aux_x, aux_y] = '1'
            
    # check izquierda
    # for x in reversed(range(x, n)):
    #     if board[x, y] != 'Q':
    #         board[x, y] = 1


def n_queens():
    n=4
    queens = 0
    board = np.zeros((n, n), dtype=int)
    # for x in range(n):
    #     for y in range(n):
    #         board[x, y] = i
    line_of_sight(0, 0, n, board)

    print(board)

n_queens()