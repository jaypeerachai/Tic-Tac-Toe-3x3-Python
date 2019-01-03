# Tic Tac Toe 3x3 Game
# Created by Jay
# 2/1/2019
import random

def tictactoe():
    '''
    Main 
    '''
    print('\nWelcome to Tic Tac Toe!')
    re = True
    while re:
        board = list(" "*10)
        print("GAME STARTS")
        display_guide_board(board)
        player1, player2 = player_input()
        print("player1: {}\nplayer2: {}".format(player1, player2))
        turn = choose_first()
        print("{} go first".format(turn))
        print("\n==========================================")
        i = 1
        print("Round {}".format(i))

        while not full_board_check(board):
            print("==========================================")
            if  turn == 'player1':
                # Player1's turn.

                display_board(board)
                print('TURN: {}'.format(turn))
                position = player_choice(board)
                place_marker(board, player1, position)

                if win_check(board, player1):
                    display_board(board)
                    print('Congratulations! player1 won the game!')
                    break
                else:
                    if full_board_check(board):
                        display_board(board)
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'player2'
            else:
                # Player2's turn.

                display_board(board)
                print('TURN: {}'.format(turn))
                position = player_choice(board)
                place_marker(board, player2, position)

                if win_check(board, player2):
                    display_board(board)
                    print('Congratulations! player2 won the game!')
                    break
                else:
                    if full_board_check(board):
                        display_board(board)
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'player1'
            i += 1
            print("\n==========================================")
            print("Round {}".format(i))

        re = replay()   


def display_guide_board(board):
    '''
    Display the board with the index of each position at the beginning of game
    INPUT: board
    '''
    print("\n7|8|9\n-----\n4|5|6\n-----\n1|2|3\n")  


def display_board(board):
    '''
    Display the current board for each rounds
    INPUT: board
    '''
    print("\n{}|{}|{}\n-----\n{}|{}|{}\n-----\n{}|{}|{}\n".format(board[7],board[8],board[9],board[4],board[5],board[6],board[1],board[2],board[3]))


def player_input():
    '''
    Ask a player to select a marker
    OUTPUT: 'X','O'
    '''
    while True:
        player1 = input("player1: Please pick a marker 'X' or 'O': ")
        if not player1 == 'X' and not player1 == 'O':
            print("Wrong!!! Please pick the marker again")
            continue
        else:
            if player1 == 'X':
                player2 = 'O'
                return (player1, player2)
            else:
                player2 = 'X'
                return (player1, player2)


def place_marker(board, marker, position):
    '''
    Assign the marker to a desired position on board
    INPUT: board, marker, position
    '''
    board[position] = marker


def win_check(board, mark):
    '''
    Check whether someone has won or not
    INPUT: board, mark
    OUTPUT: True, False
    '''
    count = 0
    for i in range(1,4):
        if not board[i] == mark:
            break
        else:
            count += 1
    if count == 3:
        return True
    count = 0
    for i in range(4,7):
        if not board[i] == mark:
            break
        else:
            count += 1
    if count == 3:
        return True
    count = 0
    for i in range(7,10):
        if not board[i] == mark:
            break
        else:
            count += 1
    if count == 3:
        return True
    count = 0
    for i in range(1,8,3):
        if not board[i] == mark:
            break
        else:
            count += 1
    if count == 3:
        return True
    count = 0
    for i in range(1,9,3):
        if not board[i] == mark:
            break
        else:
            count += 1
    if count == 3:
        return True
    count = 0
    for i in range(1,9,3):
        if not board[i] == mark:
            break
        else:
            count += 1
    if count == 3:
        return True
    count = 0
    for i in range(3,10,3):
        if not board[i] == mark:
            break
        else:
            count += 1
    if count == 3:
        return True
    count = 0
    for i in range(1,10,4):
        if not board[i] == mark:
            break
        else:
            count += 1
    if count == 3:
        return True
    count = 0
    for i in range(3,8,2):
        if not board[i] == mark:
            break
        else:
            count += 1
    if count == 3:
        return True

    return False


def choose_first():
    '''
    Randomly decide which player goes first.
    OUTPUT: 'player1','player2'
    '''
    rand = random.randint(1,2)
    if rand == 1:
        return 'player1'
    else:
        return 'player2'


def space_check(board, position):
    '''
    Check whether a space on the board is freely available or not
    INPUT: board,position
    OUTPUT: True, False
    '''
    return board[position] == " "


def full_board_check(board):
    '''
    Check whether board is full or not
    INPUT: board
    OUTPUT: True, False
    '''
    board = board[1:10]
    return not " " in board


def player_choice(board):
    '''
    Ask for a player's next position (as a number 1-9)
    INPUT: board
    OUTPUT: position
    '''
    while True:
        position = int(input('Please enter a number to place a marker: '))
        if not position in range(1,10):
            print("Wrong!!! Please enter the number again")
        else:
            if space_check(board, position):
                return position
            else:
                print("{} is not free, please enter new number".format(position))


def replay():
    '''
    Ask the player if they want to play again
    OUTPUT: True, False
    '''
    replay = input("Do you want to play it again (Y/N): ")
    if replay == 'Y':
        return True
    return False


tictactoe()