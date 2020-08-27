#defining players as "X" and "O"
player1 = "X"
player2 = "O"



#creating board using a dictionary

board = {"a1": " ", "b1": " ", "c1": " ", "a2": " ", "b2": " ", "c2": " ", "a3": " ", "b3": " ", "c3": " "}

#if game is still going
game_still_going = True

#who won? or Tie?
winner = None

#who's turn is it?
current_player = player1

#welcoming you to the game
print("\nWELCOME TO TIC TAC TOE! \n")

#allowing player to input their own name
# = input("Please enter the name of player 1")
#name2 = input("Please enter the name of player 2")

#defining the board by printing the keys. The associated values will then be assigned as player "x" or player "o" inputs.
def display_board():
    print(" ")
    print("    a b c ")
    print("   -------")
    print("1  |%s|%s|%s|" %(board["a1"], board["b1"], board["c1"]))
    print("2  |%s|%s|%s|" %(board["a2"], board["b2"], board["c2"]))
    print("3  |%s|%s|%s|" %(board["a3"], board["b3"], board["c3"]))
    print("   -------")
    print(" ")

#checking if input is a valid option.

def acceptable_move(position):

    if position in list(board.keys()) and board[position] == " ":
        return True
    else:
        return False       

#defining function that handles each turn, taking the input of player1 then player2

def handle_turn():
      global current_player

      position = input("Player %s choose an available block on the board from a1 to c3 : \n" %(current_player))
      
      if acceptable_move(position): 
        board[position] = current_player
        return True
      else:
          print("The %s chosen is not acceptable" %(position))
          return False


def check_if_game_over():
      #print("TEST GAMEOVER")
      check_for_winner()
      check_for_tie()

def check_for_winner():
    
    #print("TEST CHECK FOR WINNER")

    global winner

    row_winner = check_rows()

    column_winner = check_columns()

    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return

def check_rows():
    #Set up global variables
    global game_still_going
    #Check rows for possible win if all contain the same values (and not empty)
    row_1 = board["a1"] == board["b1"] == board["c1"] != " "
    row_2 = board["a2"] == board["b2"] == board["c2"] != " "
    row_3 = board["a3"] == board["b3"] == board["c3"] != " "
    #If any row does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board["a1"]
    elif row_2:
        return board["a2"]
    elif row_3:
        return board["a3"] 
    return

def check_columns():
    #Set up global variables
    global game_still_going
    #Check columns for possible win if all contain the same values (and not empty)
    column_1 = board["a1"] == board["a2"] == board["a3"] != " "
    column_2 = board["b1"] == board["b2"] == board["b3"] != " "
    column_3 = board["c1"] == board["c2"] == board["c3"] != " "

    #print(column_1)

    #If any column does have a match, flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    if column_1:
        return board["a1"]
    elif column_2:
        return board["b1"]
    elif column_3:
        return board["c1"] 
    return

def check_diagonals():
    #Set up global variables
    global game_still_going
    #Check diagonals for possible win if all contain the same values (and not empty)
    diagonal_1 = board["a1"] == board["b2"] == board["c3"] != " "
    diagonal_2 = board["c1"] == board["b2"] == board["a3"] != " "
    #If any diagonal does have a match, flag that there is a win
    if diagonal_1 or diagonal_2:
        game_still_going = False
    if diagonal_1:
        return board["a1"]
    elif diagonal_2:
        return board["c1"]     
    return

def check_for_tie():
    global game_still_going

    if " " not in list(board.values()):
        game_still_going = False
     

def flip_player():
    global current_player
    if current_player == player1:
        current_player = player2
    else:
        current_player = player1


#defining the function that governs the flow of the gameplay

def play_game():
    
    global winner

    while game_still_going:

        display_board()

        if handle_turn():
           flip_player()

          

        check_if_game_over()
    
    display_board()

    if winner == None:
        print("The game is a tie!\n")
    else:
        print(winner + " won the game!\n")





play_game()






