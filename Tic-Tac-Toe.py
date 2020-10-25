import random
import sys
board = [' NULL',' ',' ',' ',' ',' ',' ',' ',' ',' ']
example_board=["null",'1','2','3','4','5','6','7','8','9']

def check_for_empty_space(position):
    return(board[position]==' ')


def print_board():
    print('\n')
    print(board[1] + '|' + board[2] + '|' + board[3] )
    print(board[4] + '|' + board[5] + '|' + board[6] )
    print(board[7] + '|' + board[8] + '|' + board[9] )


def print_example_board():

    print(example_board[1] + '|' + example_board[2] + '|' + example_board[3] + '|')
    print(example_board[4] + '|' + example_board[5] + '|' + example_board[6] + '|')
    print(example_board[7] + '|' + example_board[8] + '|' + example_board[9] + '|')
def winner(board,letter):
    return (board[1]==letter and board[2]==letter and board[3]==letter) \
           or (board[4]==letter and board[5]==letter and board[6]==letter) \
           or (board[7]==letter and board[8]==letter and board[9]==letter) \
           or (board[1]==letter and board[4]==letter and board[7]==letter) \
           or (board[2]==letter and board[5]==letter and board[8]==letter) \
           or (board[3]==letter and board[6]==letter and board[9]==letter) \
           or (board[1]==letter and board[5]==letter and board[9]==letter) \
           or (board[7]==letter and board[5]==letter and board[3]==letter)
def board_full():
    if board.count(' ') > 0 :  # Since we always have one blank element in board we must use > 1
        return False
    else:
        return True



def availability(letter):
    if board[letter]==' ':
        return(True)
    else:
        return(False)
def player_move():
    y=True
    x=True
    while y==True or x==True:
        print_board()
        ask=input("Select a position within the desired range(1-9) : ")
        try:
            int(ask)
        except:
            print('This is not an integer. Please try again.')
            continue

        if int(ask) in [1,2,3,4,5,6,7,8,9]:
            y=False
        else:
            print("Invalid response. Remember to enter a number in the range(1-9) : ")
        if y==False:
            if availability(int(ask))==True:
                board[int(ask)]='X'
                return(ask)
            else:
                print("This position has already been taken. Please chose another position")

def AI_move():
    possible_moves=[]
    for x in enumerate(board):
        if x[1] == ' ':
            possible_moves.append(x[0])
    move=0
    for letter in ['O','X']:
        for x in possible_moves:
            copy=board[:]
            copy[x]=letter
            if winner(board,letter):
                move = x
                return(move)
    opencorners = []
    for open in possible_moves:
        if open in [1,3,7,9]:
            opencorners.append(open)
    if len(opencorners)>0:
        move = random.choice(opencorners)
        return(move)
    if 5 in possible_moves:
        move=5
        return(move)
    openedges=[]
    for open in possible_moves:
        if open in [2,4,6,8]:
            openedges.append(open)
    if len(openedges)>0:
        move=random.choice(openedges)
        return(move)
    return(move)



def check_for_experience():
    y = True
    while y == True:
        check = input("Welcome to Tic Tac Toe. Just to clarify, have you played tic tac toe before(Y or N) : ")
        if check == 'Y':
            print("Great, lets get started! Good Luck!")
            print("By the Way, this here is how the grid system in this game works. Each position corresponds to a specific number. When asked, please type the number corresponding to your desired position.")
            print_example_board()
            y=False
        elif check == 'N':
            print('If you have not played before, then that is totally fine. The objective of this game is to get 3 in a row of the marker you are assigned(X or O). Remember thaht diagonals count. Good Luck!')
            print_example_board()
            print("By the Way, this here is how the grid system in this game works. Each position corresponds to a specific number. When asked, please type the number corresponding to your desired position.")
            y=False
        else:
            print("Invalid response. Please type Y if you have played before and N if you have not. Remember that the response is case sensitive")

def main():
    check_for_experience()
    while not(board_full()):
        if not(winner(board,'X')):
            player_move()
            print_board()
        else:
            print("Congratulations, you have won the game!")
            sys.exit()

        if not(winner(board,'O')):
            move=AI_move()
            if move==0:
                print("The game is a tie! Nobody has one.")
                sys.exit()
            else:
                board[move]='O'
                print('\n')
                print("The computer has entered O into position {}".format(move))
                print_board()
        else:
            print('The computer has won. Better luck next time!')
            sys.exit()
        if board_full():
            print("The board is full")



main()

