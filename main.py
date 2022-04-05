import numpy as np
from treelib import Node, Tree

def line_of_sight(x, y, n, board):
    aux_x = x
    aux_y = y
    # check diagonal inferior derecha
    # for aux_x in range(aux_x, n):
    #     if aux_y+1<=n:
    #         aux_y+=1
    #     if board[aux_x, aux_y-1] != '1':
    #         board[aux_x, aux_y-1] = '1'
    #     if aux_y == n:
    #         break
    # check diagonal superior derecha
    # for aux_x in reversed(range(0, aux_x+1)):
    #     if aux_y+1<=n:
    #         print(aux_x, aux_y)
    #         aux_y+=1
    #     if board[aux_x, aux_y-1] != '1':
    #         board[aux_x ,aux_y-1] = '1'
    #     if aux_y == n:
    #         break

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
    line_of_sight(1, 2, n, board)

    print(board)

n_queens()