from tic_tac_toe import *

board = [['1','2','3'],['4','5','6'],['7','8','9']]
print_board(board)


while not game_is_over(board):
    print('\n\n\nYour Turn')
    inp = int(input("Enter the position "))
    while not select_space(board,inp,'X'):
        print("Position not available")
        inp = int(input("Enter the position "))
        pass
    print_board(board)
    if(game_is_over(board)):
        break
    print("\n\n\nComputer's Turn")
    select_space(board,minimax(board,False)[1],'O')
    print_board(board)

if evaluate_board(board)==1:
    print("\n\n\nCongratulations! You have won")
elif evaluate_board(board)==-1:
    print("\n\n\nOops! You have lost")
else:
    print("\n\n\nGame Over")
