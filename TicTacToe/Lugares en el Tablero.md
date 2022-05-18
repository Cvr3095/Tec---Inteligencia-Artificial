## Lugares que se pueden poner en el tablero y preguntar la posición que desea poner en el, además de valir si está dentro del tablero

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
