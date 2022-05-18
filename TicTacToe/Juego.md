### Se inicializa el tablero del 0 al 8

    def tic_tac_toe():

    board = list("012345678")
   ### Pídale al jugador que elija una pieza: la pieza X se mueve primero, la pieza O se mueve después
    player_letter = input("Elige la figura que quieres X o 0 (X va primero, O va después):")
   ### Los jugadores van primero
    if player_letter in ("X", "x"):
        turn = "Jugador"  
        computer_letter = "O"
   ### El IA es primero
    if player_letter in ("O", "o", "0"):
        turn = "IA"
        computer_letter = "X"
        player_letter = "O"
    print("{} ¡es primero!".format(turn))

   ### Ciclo por turnos
        while True:  
        display_board(board)
   ### Ubicación del jugador en el tablero
        if turn == 'Jugador': 
   ### Preguntar por la posición que desea en el tablero
            move = get_player_move(board) 
   ### Mover en el tablero
            board[move] = player_letter   
   ### Determina si ganar
            if is_winner(board, player_letter):  
                display_board(board)
                print("¡Felicitaciones al jugador por ganar!")
                break
            else:
                turn = "IA"
   ### Movimiento de la IA en el tablero
        else:  
            move = get_computer_move(board, computer_letter, player_letter)
            print("La posición de la Inteligencia Artificial:", move)
            board[move] = computer_letter   # Laozi
   ### Determina si ganar         
            if is_winner(board, computer_letter):  
                display_board(board)
                print('¡La Inteligencia Artificial gana! ')
                break
            else:
                turn = "Jugador"
   ### Determina si es un empate
        if is_tie(board):
            display_board(board)
            print("¡Empate!")
            break


if __name__ == '__main__':
    tic_tac_toe()
    
    
