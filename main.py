import numpy as np
from treelib import Node, Tree
def line_of_sight(x, y, n, board):

    aux_x = x
    aux_y = y
    # check diagonal derecha
    # for aux_x in range(aux_x, n):
    #     if aux_y+1<=n:
    #         aux_y+=1
    #     if board[aux_x, aux_y-1] != '1':
    #         board[aux_x, aux_y-1] = '1'
    #     if aux_y == n:
    #         break
    # check diagonal izquierda
    for aux_x in reversed(range(0, aux_x)):
        if aux_y+1>=n:
            aux_y+=1
            print('uwu')
        if board[aux_x,aux_y+1] != '1':
            board[aux_x,aux_y+1] = '1'
        if aux_y == n:
            break
    # check izquierda
    # for x in reversed(range(x, n)):
    #     if board[x, y] != 'Q':
    #         board[x, y] = 1

    #check fila
    #for i in range(n)
    #   if i == x:
    #       continue
    #   if board[i,y] == 1:
    #       return false
    #return true

    #check diagonal
    #for i in range(n):
    #   if board[x,i] == 1:
    #       

def n_queens():
    n=4
    queens = 0
    new_tree = Tree()
    board = np.zeros((n, n), dtype=int)
    # for x in range(n):
    #     for y in range(n):
    #         board[x, y] = i
    line_of_sight(0, 2, n, board)

    print(board)

n_queens()