import numpy as np
from treelib import Node, Tree

def line_of_sight(x, y, n, board):
    aux_x = x
    aux_y = y
    # # check diagonal inferior derecha
    # for aux_x in range(aux_x, n):
    #     if aux_y+1<=n:
    #         aux_y+=1
    #     if board[aux_x, aux_y-1] != '1':
    #         board[aux_x, aux_y-1] = '1'
    #     if aux_y == n:
    #         break
    # # check diagonal superior derecha
    # for aux_x in reversed(range(0, aux_x+1)):
    #     if aux_y+1<=n:
    #         aux_y+=1
    #     if board[aux_x, aux_y-1] != '1':
    #         board[aux_x ,aux_y-1] = '1'
    #     if aux_y == n:
    #         break
    # # check fila
    # for aux_y in range(0, n):
    #     if board[aux_x, aux_y] != '1':
    #         board[aux_x, aux_y] = '1'
    # # check columna
    # for aux_x in range(0, n):
    #     if board[aux_x, aux_y] != '1':
    #         board[aux_x, aux_y] = '1'
    # # check diagonal inferior izquierda
    # for aux_x in range(aux_x, n):
    #     if aux_y-1>=0:
    #         aux_y-=1
    #     if board[aux_x, aux_y+1] != '1':
    #         board[aux_x, aux_y+1] = '1'
    #     if aux_y == 0:
    #         break
    # # check diagonal superior izquierda
    for aux_x in reversed(range(0, aux_x+1)):
        if aux_y < 0:
            break
        if aux_y>=0:
            print(aux_x, aux_y)
            aux_y-=1
        if board[aux_x, aux_y+1] != '1':
            board[aux_x, aux_y+1] = '1'


def n_queens():
    n=4
    queens = 0
    new_tree = Tree()
    board = np.zeros((n, n), dtype=int)
    line_of_sight(2, 3, n, board)

    print(board)

n_queens()