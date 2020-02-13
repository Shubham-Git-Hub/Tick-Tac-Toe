import random
import os


def print_board(board):  # Printing the board
    os.system('cls')
    print(
        f"""         ||       ||   
      {board[7]}  ||   {board[8]}   ||    {board[9]}
         ||       ||   
    =======================
         ||       ||   
      {board[4]}  ||   {board[5]}   ||    {board[6]}
         ||       ||   
    =======================
         ||       ||   
      {board[1]}  ||   {board[2]}   ||    {board[3]}
         ||       ||   """
    )


def user_input():  # taking an input from the user at the beginning of the match
    choice_input = ""
    while choice_input != "X" and choice_input != "O":
        choice_input = input("Player 1 choose X or O: ").upper()
    player1 = choice_input
    if player1 == "X":
        return ('x', 'O')
    else:
        return ('O', 'X')


def place_markers(board, marker, position):  # to place markers at the given position
    board[position] = marker


def win_check(board, mark):  # to check if someone won or not. Checking all the rows, columns and diagonals
    if (
            (board[1] == board[2] == board[3] == mark)
            or (board[4] == board[5] == board[6] == mark)
            or (board[7] == board[8] == board[9] == mark)
            or (board[1] == board[4] == board[7] == mark)
            or (board[2] == board[5] == board[8] == mark)
            or (board[3] == board[6] == board[9] == mark)
            or (board[7] == board[5] == board[3] == mark)
            or (board[1] == board[5] == board[9] == mark)
    ):
        return True


def go_first():  # Randomly deciding who will go first
    x = random.randint(1, 2)
    if x == 1:
        return "Player1"
    else:
        return "Player2"


def is_available(board, position):  # Checking whether the requested position is available or not
    return board[position] == " "


def full_board(board):  # Check whether there is a space on the board or not
    for i in range(1, 10):
        if board[i] == " ":
            return False
    return True


def players_choice(board):  # Taking input from the player where they want to make their next move
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not is_available(board, position):
        position = int(input('Enter a position (1-9) where you want to play: '))
    return position


def replay():
    again = input('Do you want to play again? Yes or No : ').lower()
    if again == 'Yes':
        return True
    else:
        return False


print('Welcome to Tic-Tack-Toe! ')
while True:
    board = [' '] * 10
    player1_mark, player2_mark = user_input()
    turn = go_first()
    print(turn + ' goes first! ')
    play = input('Ready to play? y or n: ')
    if play == 'y':
        game_on = True
    else:
        game_on = False
    while game_on:
        if turn == 'Player1':
            # Print the board
            print_board(board)
            # Choose a Position
            position = players_choice(board)
            # Place the marker at that position
            place_markers(board, player1_mark, position)
            # Check if they won
            if win_check(board, player1_mark):
                print_board(board)
                print("Player 1 has won! ")
                game_on = False
            else:
                if full_board(board):
                    print_board(board)
                    print('Its a tie!')
                    game_on = False
                turn = 'Player2'
        else:
            # Print the board
            print_board(board)
            # Choose a Position
            position = players_choice(board)
            # Place the marker at that position
            place_markers(board, player2_mark, position)
            # Check if they won
            if win_check(board, player2_mark):
                print_board(board)
                print("Player 2 has won! ")
                game_on = False
            else:
                if full_board(board):
                    print_board(board)
                    print('Its a tie!')
                    game_on = False
                turn = 'Player1'
    if not replay():
        break
