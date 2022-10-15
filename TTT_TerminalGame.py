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




# define logic to randomly seect who goes first -------------------------------------
def coin_toss(player1, player2):
  validate_P1 = 0
  validate_P2 = 0
  #make validate player choice into a function that lives outside coin_toss to reduce lines of code 
  print("We will now select a number between 1-5 to decide who goes first. The person who picks a number closest to the random number selection goes first! \n")
  while validate_P1 == 0: 
    player1.choice = input("{} select a number between 1-5: \n".format(player1.name))
    if int(player1.choice) in list(range(1,6)):
      validate_P1 = 1
    else:
      print("Invalid number, {} please input a number between 1-5!!!!!!!\n".format(player1.name))
      
      
  while validate_P2 == 0: 
    player2.choice = input("{} select a number between 1-5: \n".format(player2.name))
    if int(player2.choice) in list(range(1,6)):
      validate_P2 = 1
    else:
      print("Invalid number, {} please input a number between 1-5!!!!!!!\n".format(player2.name))
      

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

#test logic : 
# samp1 = Player("Jorge")
# samp2 = Player("Sam")
# x = coin_toss(samp1,samp2)
# print(x)


# create a variable that for a while loop if false the game keeps repeating so less code and once true it will announce the player 
#define logic to play tic tac toe 
def play_game(player1, player2):
  matrix = [["","",""], ["","",""], ["","",""]]
  print("Let's play tic tac toe!!!!!!!!! \nWe will be playing on a 3x3 board.")
  
  validateP1_name =0
  validateP2_name =0

  #make validate name into a function that lives outside play_game to reduce lines of code 
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
  validateP1_shape = 0
  validateP2_shape = 0
  
  #Make validate shape into a function to reduce number of lines of code 
  if player_sel == 1:
    while validateP1_shape == 0:
      player1.shape = input("Which shape is {} using: \"X\" or \"O\" ".format(player1.name))
      if player1.shape == "X":
        player2.shape = "O"
        print("{}'s shape is {} and {}'s shape is {}, let's begin!".format(player1.name,player1.shape, player2.name, player2.shape))
        validateP1_shape = 1
      elif player1.shape == "O":
        player2.shape = "X"
        print("{}'s shape is {} and {}'s shape is {}, let's begin!".format(player1.name,player1.shape, player2.name, player2.shape))
        validateP1_shape = 1
      else:
        print("Not a valid shape, {} please select either \"X\" or \"O\" ".format(player1.name))
  else:
    while validateP2_shape == 0:
      player2.shape = input("Which shape is {} using: \"X\" or \"O\" ".format(player2.name))
      if player2.shape == "X":
        player1.shape = "O"
        print("{}'s shape is {} and {}'s shape is {}, let's begin!\n\n".format(player1.name,player1.shape, player2.name, player2.shape))
        validateP2_shape = 1
      elif player2.shape == "O":
        player1.shape = "X"
        print("{}'s shape is {} and {}'s shape is {}, let's begin!\n\n".format(player1.name,player1.shape, player2.name, player2.shape))
        validateP2_shape = 1
      else:
        print("Not a valid shape, {} please select either \"X\" or \"O\" ".format(player2.name))



  #Logic to put shapes in matrix --------------------------------------------
  winner=0
  if player_sel==1:
    first_player = player1
    second_player= player2
  else:
    first_player = player2
    second_player = player1
  print(matrix[0])
  print(matrix[1])
  print("{} \n".format(matrix[2]))
  while winner == 0:
    
    row_check = 0
    column_check = 0
    while row_check==0 :
      first_player.position[0] = input("{}, what row would you like to place your {} shape? Pick a number between 0-2: ".format(first_player.name,first_player.shape))
      if int(first_player.position[0]) in list(range(0,3)):
        row_check =1
      else:
        print("Invalid row choice. Please select a number between 0-2")

    while column_check ==0:
      first_player.position[1] = input("{}, what column would you like to place your {} shape? Pick a number between 0-2: ".format(first_player.name,first_player.shape))
      if int(first_player.position[1]) in list(range(0,3)):
        column_check=1 
      else:
        print("Invalid column choice. Please select a number between 0-2")

    temp_row1 = int(first_player.position[0])
    temp_col1 = int(first_player.position[1])
    matrix[temp_row1][temp_col1] = str(first_player.shape) 
    print(matrix[0])
    print(matrix[1])
    print("{} \n".format(matrix[2]))
    for i in matrix:
      first_player_shape_counter = 0
      for j in i:
        if j == first_player.shape:
          first_player_shape_counter+=1
      if first_player_shape_counter == 3:
        winner = 1
      if winner == 1:
        print("{} is the winner of tic tac toe!!!!!".format(first_player.name))
        break

    # break out of while loop if winner has been found 
    if winner == 1:
      break

 
    for i in list(range(0,3)):
      first_player_shape_counter = 0
      for j in list(range(0,3)):
        if matrix[j][i] == first_player.shape:
          first_player_shape_counter+=1
      if first_player_shape_counter == 3:
          winner = 1
      if winner == 1:
        print("{} is the winner of tic tac toe!!!!!".format(first_player.name))
        break

    # break out of while loop if winner has been found 
    if winner == 1:
      break


    # insert logic to check diagonals
    first_player_diag_shape_counter=0
    for index in list(range(0,3)):
      if matrix[index][index] == first_player.shape:
        first_player_diag_shape_counter+=1 
    if first_player_diag_shape_counter == 3:
      winner =1
      print("{} is the winner of tic tac toe!!!!!".format(first_player.name))
    if winner == 1:
      break

    first_player_diag_shape_counter=0
    row = 2
    for column in list(range(0,3)):
      if matrix[row][column] == first_player.shape:
        first_player_diag_shape_counter+=1
        row-=1
    if first_player_diag_shape_counter == 3:
      winner =1
      print("{} is the winner of tic tac toe!!!!!".format(first_player.name))
    if winner == 1:
      break    
      
  
    #add logic that checks if their choice was between 0-2
    row_check = 0
    column_check = 0
    while row_check==0 :
      second_player.position[0] = input("{}, what row would you like to place your {} shape? Pick a number between 0-2: ".format(second_player.name,second_player.shape))
      if int(second_player.position[0]) in list(range(0,3)):
        row_check =1
      else:
        print("Invalid row choice. Please select a number between 0-2")

    while column_check ==0:
      second_player.position[1] = input("{}, what column would you like to place your {} shape? Pick a number between 0-2: ".format(second_player.name,second_player.shape))
      if int(second_player.position[1]) in list(range(0,3)):
        column_check=1 
      else:
        print("Invalid column choice. Please select a number between 0-2")


    temp_row2 = int(second_player.position[0])
    temp_col2 = int(second_player.position[1]) 
    matrix[temp_row2][temp_col2] = str(second_player.shape) 
    print(matrix[0])
    print(matrix[1])
    print("{} \n".format(matrix[2]))
    for i in matrix:
      second_player_shape_counter = 0
      for j in i:
        if j == second_player.shape:
          second_player_shape_counter+=1
      if second_player_shape_counter == 3:
        winner = 1
      if winner == 1:
        print("{} is the winner of tic tac toe!!!!!".format(second_player.name))
        break

    # break out of while loop if winner has been found 
    if winner == 1:
      break

 
    for i in list(range(0,3)):
      second_player_shape_counter = 0
      for j in list(range(0,3)):
        if matrix[j][i] == second_player.shape:
          second_player_shape_counter+=1
      if second_player_shape_counter == 3:
          winner = 1
      if winner == 1:
        print("{} is the winner of tic tac toe!!!!!".format(second_player.name))
        break

    # break out of while loop if winner has been found 
    if winner == 1:
      break


    # insert logic to check diagonals
    second_player_diag_shape_counter = 0
    for index in list(range(0,3)):
      if matrix[index][index] == second_player.shape:
        second_player_diag_shape_counter+=1 
    if second_player_diag_shape_counter == 3:
      winner =1
      print("{} is the winner of tic tac toe!!!!!".format(second_player.name))
    if winner == 1:
      break

    row = 2
    second_player_diag_shape_counter = 0
    for column in list(range(0,3)):
      if matrix[row][column] == second_player.shape:
        second_player_diag_shape_counter+=1
        row-=1
    if second_player_diag_shape_counter == 3:
      winner =1
      print("{} is the winner of tic tac toe!!!!!".format(second_player.name))
    if winner == 1:
      break


player1=Player()
player2=Player()

play_game(player1,player2)


