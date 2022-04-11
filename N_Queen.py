from typing import List # For annotations
from timeit import default_timer as timer

boardcnt = 0
solution = []

def IsBoardOk (chessboard : List, row : int, col : int) :

   # Ve si hay una reina en la fila, a la izquierda de col
   for c in range(col) :
       if (chessboard[row][c] == 'Q') :
           return False

   # Ve si hay una reina en la diagonal izquierda superior
   for r, c in zip(range(row-1, -1, -1), range(col-1, -1, -1)) :
       if (chessboard[r][c] == 'Q') :
           return False

   # Ve si hay una reina en la diagonal izquierda inferior
   for r, c in zip(range(row+1, len(chessboard), 1), range(col-1, -1, -1)) :
      if (chessboard[r][c] == 'Q') :
          return False

   return True

def DisplayBoard (chessboard : List) :

    for row in chessboard :
        print(row)

def PlaceNQueens (chessboard : List, col : int) :
    # Si todas las columnas tienen una reina 'Q', se encuentra una solución
    global boardcnt
    global solution

    if (col == len(chessboard)) :
        boardcnt += 1
        print("--------------------------")
        print("Tablero N=" + str(len(chessboard)))
        print("Solucion: ")
        solution = [x+1 for x in solution]
        print(solution)
        with open('readme.txt', 'a') as f:
            f.write(str(solution))
            f.write("\n")

    elif (boardcnt < 1) :
        # Si no hay solución tratar de colocar una reina en cada fila de la columna
        # y ver si el tablero se mantiene seguro
        for row in range(len(chessboard)) :

            chessboard[row][col] = 'Q'
            solution.append(row)

            if (IsBoardOk(chessboard, row, col) == True) :
                # Como la jugada es posible, tratar de colocar una reina en la siguiente columna
                PlaceNQueens(chessboard, col + 1)

            # Si la última jugada no es segura, se reestablece la posición y se trata con la siguiente fila
            chessboard[row][col] = '.'
            solution.pop()

def main() :
    chessboard = []
    global boardcnt
    N = 4
    while True:
        # Crear tablero de NxN
        for i in range(N):
            row = ["."] * N
            chessboard.append(row)
        # Empezar a buscar la primera solución, desde la columna 0
        start = timer()
        PlaceNQueens(chessboard, 0)
        end = timer()
        print("Tiempo: " + str(end - start) + " segundos.")
        with open('readme.txt', 'a') as f:
            f.write(str(N) + ": Tiempo: " + str(end - start) + " segundos.\n")
        #Reiniciar valores para el siguiente NxN
        chessboard = []
        boardcnt = 0
        N+=1

if __name__ == "__main__" :
    main()