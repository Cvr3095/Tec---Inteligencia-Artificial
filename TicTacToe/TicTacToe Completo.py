def display_board(b):
    print("\t{0}|{1}|{2}".format(b[0], b[1], b[2]))
    print("\t_|_|_")
    print("\t{0}|{1}|{2}".format(b[3], b[4], b[5]))
    print("\t_|_|_")
    print("\t{0}|{1}|{2}".format(b[6], b[7], b[8]))

def legal_moves(board):
    moves = []
    for i in range(9):
        if board[i] in list("012345678"):
            moves.append(i)
    return moves

def get_player_move(board):
    move = 9  # El valor inicial 9 es el mensaje de error
    while move not in legal_moves(board):
        move = int(input("Elija la posición de ubicación (0-8)"))
    return move

def get_computer_move(board, computer_letter, player_letter): 
    board_copy = board.copy()  # Copia el tablero de ajedrez sin afectar al original
    # Regla 1: Determine si se puede ganar una posición, luego elija esa posición
    for move in legal_moves(board_copy):
        board_copy[move] = computer_letter
        if is_winner(board_copy, computer_letter):  # Determina si ganar
            return move
        board_copy[move] = str(move)

    # Regla 2: en una determinada posición, el jugador puede ganar el siguiente movimiento y luego elegir esa posición
    for move in legal_moves(board_copy):
        board_copy[move] = player_letter
        if is_winner(board_copy, player_letter): # Determina si ganar
            return move
        board_copy[move] = str(move)

    # Regla 3: Según el centro (4), ángulos (0, 2, 6, 8) y aristas (1, 3, 5, 7)
    for move in (4, 0, 2, 6, 8, 1, 3, 5, 7):
        if move in legal_moves(board):
            return move

def is_winner(board, letter):   
    ways_to_win = {(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                   (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)}
    for r in ways_to_win:
        if board[r[0]] == board[r[1]] == board[r[2]]:
            return True
    return False

def is_tie(board):
    for i in list("012345678"):
        if i in board:
            return False
    return True

def tic_tac_toe():
    board = list("012345678")
    # Pídale al jugador que elija una pieza: la pieza X se mueve primero, la pieza O se mueve después
    player_letter = input("Elige la figura que quieres X o 0 (X va primero, O va después):")
    if player_letter in ("X", "x"):
        turn = "Jugador"  # Los jugadores van primero
        computer_letter = "O"
    if player_letter in ("O", "o", "0"):
        turn = "IA"
        computer_letter = "X"
        player_letter = "O"
    print("{} ¡es primero!".format(turn))

    while True:  # Ciclo por turnos
        display_board(board)
        if turn == 'Jugador':  # Ubicación del jugador
            move = get_player_move(board)  # Pregunte por la ubicación
            board[move] = player_letter   # Laozi
            if is_winner(board, player_letter):  # Determina si ganar
                display_board(board)
                print("¡Felicitaciones al jugador por ganar!")
                break
            else:
                turn = "IA"
        else:  # Inteligencia artificial informática AI drop
            move = get_computer_move(board, computer_letter, player_letter)
            print("La posición de la Inteligencia Artificial:", move)
            board[move] = computer_letter   # Laozi
            if is_winner(board, computer_letter):  # Determina si ganar
                display_board(board)
                print('¡La Inteligencia Artificial gana! ')
                break
            else:
                turn = "Jugador"
        # Determina si es un empate
        if is_tie(board):
            display_board(board)
            print("¡Empate!")
            break

if __name__ == '__main__':
    tic_tac_toe()
