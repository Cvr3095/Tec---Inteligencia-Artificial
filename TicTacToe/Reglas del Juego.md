## Con esto calcularemos la posición de ubicación de la IA, algoritmo central en el Tic Tac Toe y además definimos las reglas para el juego.

    def get_computer_move(board, computer_letter, player_letter):
   
### Copia el tablero de ajedrez sin afectar al original

    board_copy = board.copy() 
    
### Regla 1: Determine si se puede ganar una posición, luego elija esa posición

    for move in legal_moves(board_copy):
        board_copy[move] = computer_letter
        if is_winner(board_copy, computer_letter):  # Determina si gana la IA
            return move
        board_copy[move] = str(move)
 
### Regla 2: en una determinada posición, el jugador puede ganar el siguiente movimiento y luego elegir esa posición.

    for move in legal_moves(board_copy):
        board_copy[move] = player_letter
        if is_winner(board_copy, player_letter): # Determina si gana el jugador
            return move
        board_copy[move] = str(move)

### Regla 3: Según el centro (4), ángulos (0, 2, 6, 8) y aristas (1, 3, 5, 7).
    
    for move in (4, 0, 2, 6, 8, 1, 3, 5, 7):
        if move in legal_moves(board):
            return move
