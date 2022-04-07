import numpy as np
from treelib import Node, Tree

def line_of_sight(x, y, n, board):
    aux_x = x
    aux_y = y
    is_valid = []
    # # check diagonal inferior derecha
    for aux_x in range(aux_x, n):
        if aux_y+1<=n:
            aux_y+=1
        if board[aux_x, aux_y-1] != '1':
            board[aux_x, aux_y-1] = '1'
        elif board[aux_x, aux_y-1] == '1':
            is_valid.append(False)
        if aux_y == n:
            break
    aux_x = x
    aux_y = y
    # # check diagonal superior derecha
    for aux_x in reversed(range(0, aux_x+1)):
        if aux_y+1<=n:
            aux_y+=1
        if board[aux_x, aux_y-1] != '1':
            board[aux_x ,aux_y-1] = '1'
        elif board[aux_x, aux_y-1] == '1':
            is_valid.append(False)
        if aux_y == n:
            break
    aux_x = x
    aux_y = y
    # # check fila
    for aux_y in range(0, n):
        if board[aux_x, aux_y] != '1':
            board[aux_x, aux_y] = '1'
        elif board[aux_x, aux_y] == '1':
            is_valid.append(False)
    aux_x = x
    aux_y = y
    # # check columna
    for aux_x in range(0, n):
        if board[aux_x, aux_y] != '1':
            board[aux_x, aux_y] = '1'
        elif board[aux_x, aux_y] == '1':
            is_valid.append(False)
    aux_x = x
    aux_y = y
    # # check diagonal inferior izquierda
    for aux_x in range(aux_x, n):
        if aux_y-1>=0:
            aux_y-=1
        if board[aux_x, aux_y+1] != '1':
            board[aux_x, aux_y+1] = '1'
        elif board[aux_x, aux_y+1] == '1':
            is_valid.append(False)
        if aux_y == 0:
            break
    aux_x = x
    aux_y = y
    # # check diagonal superior izquierda
    for aux_x in reversed(range(0, aux_x+1)):
        if aux_y < 0:
            break
        if aux_y>=0:
            aux_y-=1
        if board[aux_x, aux_y+1] != '1':
            board[aux_x, aux_y+1] = '1'
        elif board[aux_x, aux_y+1] == '1':
            is_valid.append(False)
    print(is_valid)
    # for item in is_valid:
    #     if item == False:
    #         return False
    #     else:
    #         return True


def n_queens():
    n=4
    queens = 0
    new_tree = Tree()
    board = np.zeros((n, n), dtype=int)
    valid_position = line_of_sight(2, 3, n, board)
    if valid_position == True:
        print('posicion valida')
    else:
        print('posicion no valida')
    print(board)

n_queens()