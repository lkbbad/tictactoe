import string
import time

"""
Creates dictionary with key values definining empty game board.
"""
def empty_board():
    return {"A1": '  ', "B1": '  ', "C1": '  ',"A2": '  ',"B2": '  ',"C2": '  ',
    "A3": '  ',"B3": '  ',"C3": '  '}

"""
Check the current state of the board after the most recent play to determine if 
there is a win. A win is determined by three X's or three O's in a row.
"""
def check_win(board):
    if (board['A1'] == board['A2'] == board['A3'] != '  '): # down left side
        return board['A1']
    elif (board['A1'] == board['B1'] == board['C1'] != '  '): # across top
        return board['A1']
    elif (board['A2'] == board['B2'] == board['C2'] != '  '): # across middle
        return board['A2']
    elif (board['B1'] == board['B2'] == board['B3'] != '  '): # down middle
        return board['B1']
    elif (board['A3'] == board['B3'] == board['C3'] != '  '): # across bottom
        return board['A3']
    elif (board['C1'] == board['C2'] == board['C3'] != '  '): # down right side
        return board['C1']
    elif (board['A1'] == board['B2'] == board['C3'] != '  '): # top left to 
        # bottom right diagonal
        return board['A1']
    elif (board['A3'] == board['B2'] == board['C1'] != '  '): # top right to 
        # bottom left diagonal
        return board['A3']
    else: return False

"""
Print current state of the game board to the console. 
Positions are defined by printed horizontal and vertical axes. 
"""
def print_board(board):
    print()
    print("     " + "A" + "  " + "B" + "  " + "C")
    print('   ----------')
    print("1  " + '|' + board['A1'] + '|' + board['B1'] + '|' + board['C1'] + '|')
    print('   ----------')
    print("2  " + '|' + board['A2'] + '|' + board['B2'] + '|' + board['C2'] + '|')
    print('   ----------')
    print("3  " + '|' + board['A3'] + '|' + board['B3'] + '|' + board['C3'] + '|')
    print('   ----------')
    print(flush=True)

"""
Function that runs tic-tac-toe game play. 
"""
def play_game():
    print('\nWelcome to Tic Tac Toe!\n', flush=True)
    time.sleep(1.0)
    print("Player 1, you are X.", flush=True)
    print("Player 2, you are O.", flush=True)
    print("Press Q to quit.", flush=True)
    time.sleep(1.0)
    print("\nLet's go!\n", flush=True)
    print()
    time.sleep(1.0)

    p1 = " X"
    p2 = " O"
    board = empty_board()
    player = 0
    won = False

    for i in range(1,10): # maximum of 9 possible moves, 9 spaces on the game board
        if (i % 2 == 0): # Player 2 plays on even-numbered turns
            player = 2
        else: # Player 1 plays on odd-numbered turns
            player = 1
        print("\nPlayer " + str(player) + ", choose a position.\n", flush=True)
        print_board(board)

        position = input().upper()

        while (position not in board.keys()): # if player does not input an 
            # acceptable position...
            if position == "Q": # input of Q exits the game
                exit()
            print("Position is invalid. Choose again.", flush=True)
            position = input().upper()

        while (board[position] != "  "): # if the position is already taken...
            print("Position already taken. Choose again.", flush=True)
            position = input().upper()
        if (player == 1):
            board[position] = p1
        else: board[position] = p2

        if i >=5: # start checking for wins after 5 moves 
            iswin = check_win(board)
            
            if (iswin == p1):
                won = True
                print_board(board)
                print("\nPlayer 1 wins!\n", flush=True)
                time.sleep(1.0)
                break
            elif (iswin == p2):
                won = True
                print_board(board)
                print("\nPlayer 2 wins!\n", flush=True)
                time.sleep(1.0)
                break
            else: continue
        
    if (won == False):
        print("\nGame Over.\n", flush=True)                
        print("\nIt's a Tie!\n", flush=True)
        time.sleep(1.0)
    
    # print("Play again? Y or N: ", flush=True)
    # time.sleep(1.0)

    # againYN = input().upper()
    # if (againYN == "Y"):
    #     play_game()
    # else: exit()

    exit()

"""
Main function for code execution.
"""
def main():
    play_game()

####################################################################
if __name__ == "__main__":
    main()



