   ### Método para validación de lugares en el tablero
    def legal_moves(board):

     moves = []
     for i in range(9):
        if board[i] in list("012345678"):
            moves.append(i)
     return moves

   ### Preguntar la posición que desea poner en el tablero.
    def get_player_move(board):

      move = 9  # El valor inicial 9 es el mensaje de error
      while move not in legal_moves(board):
         move = int(input("Elija la posición de ubicación (0-8)"))
      return move
