# Método para calcular si la posición dada te hará ganar.

    def is_winner(board, letter):
    
  ### Formas de ganar en el tablero y calcular en función a las posiciones obtenidas en el juego
    ways_to_win = {(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                   (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)}
    for r in ways_to_win:
        if board[r[0]] == board[r[1]] == board[r[2]]:
            return True
    return False
