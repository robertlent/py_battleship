from random import randint
import os, sys

board = []
size = 5

def new_game():
    global size
    answer = input("Do you want to start a new game of Battleship? ").lower()
    if answer == "" or answer.isdigit() or (answer not in ['yes', 'y', 'no', 'n']):
        print("\nThat was not a valid answer.\n")
        new_game()
    else:
        if answer == 'yes' or answer == 'y':
            os.system('cls')
            size = input("Enter a number between 5 and 10.\nThis will determine how big the playing board is and "
                             "how many turns you have to find the Battleship."
                             "\n(5 rows, 5 columns, 5 turns, etc.): ")
            if size.isdigit():
                size = int(size)
                if size < 5 or size > 10:
                    print("\nI told you to pick a number between 5 and 10...\nLet's try this again...\n\n")
                    new_game()
                else:#Creates the playing board's size, based on the size chosen by the player.
                    for x in range(0, size):
                        board.append(["O"] * size)
                    game()
            else:
                print("\nI told you to pick a number, not a letter...\nLet's try this again...\n\n")
                new_game()
        elif answer == 'no' or answer == 'n':
            os.system('cls')
            print("Thank you for playing!")
            input("Press the 'Enter' key to exit the game.")
            quit

def print_board(board):
    for row in board:
        print(" ".join(row))

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

def game():
    global board
    os.system('cls')
    print("Welcome to Battleship. A Ship has been randomly placed on the below %dx%d grid.\nYou have %d turns to find it.\n" % (size, size, size))

    #Randomly places Battleship
    ship_row = random_row(board)
    ship_col = random_col(board)
    
    print_board(board)
    
    #The next two lines are for debugging purposes. They display the position of the battleship.
    #print(ship_row + 1)
    #print(ship_col + 1)

    #Give the user the amount of turns they chose, between 5 and 10.
    for turn in range(size):
        print("\nTurn", turn + 1, "\n")
        guess_row = int(input("Guess Row: ")) - 1
        guess_col = int(input("Guess Column: ")) - 1

        #Checks if Player wins
        if guess_row == ship_row and guess_col == ship_col:
            print("\nCongratulations! You sank my battleship!\n")
            board = []
            new_game()
            break
        else:#Guesses are outside of playing field
            if (guess_row > size or guess_row < 0) or (guess_col > size or guess_col < 0):
                print("Oops, that's not even in the ocean.")
            elif board[guess_row][guess_col] == "X":#Player previously guessed their current guesses
                os.system('cls')
                print("You guessed that one already.")
                input("")
            else:#User misses
                os.system('cls')
                print("You missed my battleship!\n")
                board[guess_row][guess_col] = "X"
                print_board(board)
    else:
        print("\nGame Over\n")
        board = []
        new_game()

new_game()