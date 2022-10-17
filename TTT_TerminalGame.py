import random 

# define baseball player class ----------------------------------------------------
class Player:
  def __init__(self):
    self.name = ""
    self.shape = ""
    self.position=[5,5]
    self.choice = 0

  def __repr__(self):
    return "Player name is {} and their shape is {}".format(self.name, self.shape)


#Logic to randomly seect who goes first -------------------------------------
def coin_toss(player1, player2):
  validate_P1 = 0
  validate_P2 = 0
   
  print("\n\nWe will now select a number between 1-5 to decide who goes first. The person who picks a number closest to the random number selection goes first! \n")
  while validate_P1 == 0: 
    try:
      player1.choice = input("{} select a number between 1-5: \n".format(player1.name))
      if int(player1.choice) in list(range(1,6)):
        validate_P1 = 1
      else:
        print("Invalid number, {} please input a number between 1-5!!!!!!!\n".format(player1.name))
    except ValueError:
      print("Your input needs to be an interger between 1-5, please try again.")
  
  while validate_P2 == 0: 
    try:
      player2.choice = input("{} select a number between 1-5: \n".format(player2.name))
      if int(player2.choice) in list(range(1,6)):
        validate_P2 = 1
      else:
        print("Invalid number, {} please input a number between 1-5!!!!!!!\n".format(player2.name))

    except ValueError:
      print("Your input needs to be an interger between 1-5, please try again.")
      
  #Using the randint method check which user input is closer to the random nuber and select who goes first based on outcome
  chance = random.randint(1,5)
  print("The random number selected was {}".format(chance))
  selection = 0
  if (abs((chance - int(player1.choice))) < abs((chance - int(player2.choice)))):
    print("{} goes first!\n".format(player1.name))
    selection = 1
    return selection
  else:
    print("{} goes first!\n".format(player2.name))
    selection = 2
    return selection


# Logic to put player's shape in a spot and check if there are 3 in a row -------------------------------------
matrix = [["","",""], ["","",""], ["","",""]]
winner = 0
def players_move(player, winner):
  results =[0,0]
  
  position_check =0
  while position_check==0:
    row_check = 0
    column_check = 0
    while row_check==0:
      try:
        player.position[0] = input("{}, what row would you like to place your {} shape? Pick a number between 0-2: ".format(player.name, player.shape))
        if int(player.position[0]) in list(range(0,3)):
          row_check =1
        else:
          print("Invalid row choice. Please select a number between 0-2")
      except ValueError:
        print("Your input needs to be an interger between 0-2, please try again.")

    while column_check ==0:
      try:
        player.position[1] = input("{}, what column would you like to place your {} shape? Pick a number between 0-2: ".format(player.name, player.shape))
        if int(player.position[1]) in list(range(0,3)):
          column_check=1 
        else:
          print("Invalid column choice. Please select a number between 0-2")

      except ValueError:
        print("Your input needs to be an interger between 0-2, please try again.")

    temp_row = int(player.position[0])
    temp_col = int(player.position[1])
    if matrix[temp_row][temp_col] == "":
      matrix[temp_row][temp_col] = str(player.shape)
      position_check = 1
    else:
      print("This space on the board already has a shape, please try again!\n\n")
  
  print(matrix[0])
  print(matrix[1])
  print("{} \n".format(matrix[2]))
  
  #Logic to check if there are 3 in a row that are the same as the player's shape
  for i in matrix:
    player_shape_counter = 0
    for j in i:
      if j == player.shape:
        player_shape_counter+=1
    if player_shape_counter == 3:
      winner = 1 

 #Logic to check if there are 3 in a column that are the same as the player's shape
  for i in list(range(0,3)):
    player_shape_counter = 0
    for j in list(range(0,3)):
      if matrix[j][i] == player.shape:
        player_shape_counter+=1
    if player_shape_counter == 3:
        winner = 1

  # Logic to check diagonals
  player_diag_shape_counter=0
  for index in list(range(0,3)):
    if matrix[index][index] == player.shape:
      player_diag_shape_counter+=1 
  if player_diag_shape_counter == 3:
    winner =1 

  player_diag_shape_counter=0
  row = 2
  for column in list(range(0,3)):
    if matrix[row][column] == player.shape:
      player_diag_shape_counter+=1
      row-=1
  if player_diag_shape_counter == 3:
    winner =1
   
  
  if winner ==1: 
    print("{} is the winner of tic tac toe!!!!!".format(player.name))
  return winner   

#define logic to play tic tac toe 
def play_game(player1, player2):
  
  print("\n\nLet's play tic tac toe!!!!!!!!! \nWe will be playing on a 3x3 board.")
  
  validateP1_name =0
  validateP2_name =0

  while validateP1_name == 0:
    player1.name = input("What is player 1's name: ")
    if type(player1.name) is str:
      validateP1_name = 1
    else:
      print("Not a valid name, please insert a string")

  while validateP2_name == 0:
    player2.name = input("What is player 2's name: ")
    if type(player2.name) is str:
      validateP2_name = 1
    else:
      print("Not a valid name, please insert a string")

  player_sel = coin_toss(player1,player2)
  validate_shape = 0
  if player_sel==1:
    first_player = player1
    second_player= player2
  else:
    first_player = player2
    second_player = player1
  
  while validate_shape == 0:
    first_player.shape = input("Which shape is {} using: \"X\" or \"O\" ".format(first_player.name))
    if first_player.shape == "X":
      second_player.shape = "O"
      print("{}'s shape is {} and {}'s shape is {}, let's begin!".format(first_player.name, first_player.shape, second_player.name, second_player.shape))
      validate_shape = 1
    elif first_player.shape == "O":
      second_player.shape = "X"
      print("{}'s shape is {} and {}'s shape is {}, let's begin!".format(first_player.name, first_player.shape, second_player.name, second_player.shape))
      validate_shape = 1
    else:
      print("Not a valid shape, {} please select either \"X\" or \"O\" ".format(first_player.name))

  #Logic to put shapes in matrix --------------------------------------------
  winner=0
  turn_counter = 0

  print(matrix[0])
  print(matrix[1])
  print("{} \n".format(matrix[2]))
  
  while winner == 0:

    if turn_counter > 8:
      print("The maximum number of turns has been exceeded and there is no winner. Game over.")
      break
    winner = players_move(first_player, winner)
    if winner ==1:
      break
    turn_counter+=1
    if turn_counter > 8:
      print("The maximum number of turns has been exceeded and there is no winner. Game over.")
      break
    winner = players_move(second_player, winner)
    if winner ==1:
      break
    turn_counter+=1
    
    
# Code to call the play game function ----------------------------------------------------------
player1=Player()
player2=Player()

play_game(player1,player2)


