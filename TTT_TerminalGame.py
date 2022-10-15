import random 

# define baseball player class ----------------------------------------------------
class Player:
  def __init__(self, input_name = "N/A", input_shape=""):
    self.name = input_name
    self.shape = input_shape
    self.position=[0,0]
    self.choice = 0

  def __repr__(self):
    return "Player name is {} and their shape is {}".format(self.name, self.shape)




# define logic to randomly seect who goes first -------------------------------------
def coin_toss(player1, player2):
  validate_P1 = 0
  validate_P2 = 0
  #make validate player choice into a function that lives outside coin_toss to reduce lines of code 
  while validate_P1 == 0: 
    player1.choice = input("Player 1 select a number between 1-5: \n")
    if int(player1.choice) in list(range(1,6)):
      validate_P1 = 1
    else:
      print("Please input a number between 1-5!!!!!!!\n")
      
      
  while validate_P2 == 0: 
    player2.choice = input("Player 2 select a number between 1-5: \n")
    if int(player2.choice) in list(range(1,6)):
      validate_P2 = 1
    else:
      print("Please input a number between 1-5\n")
      

  chance = random.randint(1,9)
  print(chance)
  selection = 0
  if (abs((chance - int(player1.choice))) > abs((chance - int(player2.choice)))):
    print("Player 1 goes first!\n")
    selection = 1
    return selection
  else:
    print("Player 2 goes first!\n")
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
  print("Let's play tic tac toe!!!!!!!!!")
  
  validateP1_name =0
  validateP2_name =0

  #make validate name into a function that lives outside play_game to reduce lines of code 
  while validateP1_name == 0:
    player1.name = input("What is player 1's name: ")
    if type(player1.name) is string:
      validateP1_name = 1
    else:
      print("Not a valid name, please insert a string")

  while validateP2_name == 0:
    player2.name = input("What is player 2's name: ")
    if type(player2.name) is string:
      validateP2_name = 1
    else:
      print("Not a valid name, please insert a string")


  player_sel = coin_toss(player1,player2)
  validateP1_shape = 0
  validateP2_shape = 0
  
  #Make validate shape into a function to reduce number of lines of code 
  if player_sel == 1:
    while validateP1_shape == 0:
      player1.shape = input("Which shape is player 1 using: \"X\" or \"O\" ")
      if player1.shape == "X":
        player2.shape = "O"
        print("Player 1's shape is {} and Player 2's shape is {}, let's begin!".format(player1.shape, player2.shape))
        validateP1_shape = 1
      elif player1.shape == "O":
        player2.shape = "X"
        print("Player 1's shape is {} and Player 2's shape is {}, let's begin!".format(player1.shape, player2.shape))
        validateP1_shape = 1
      else:
        print("Not a valid shape, please select either \"X\" or \"O\" ")
  else:
    while validateP2_shape == 0:
      player2.shape = input("Which shape is player 1 using: \"X\" or \"O\" ")
      if player2.shape == "X":
        player1.shape = "O"
        print("Player 1's shape is {} and Player 2's shape is {}, let's begin!".format(player1.shape, player2.shape))
        validateP2_shape = 1
      elif player2.shape == "O":
        player1.shape = "X"
        print("Player 1's shape is {} and Player 2's shape is {}, let's begin!".format(player1.shape, player2.shape))
        validateP2_shape = 1
      else:
        print("Not a valid shape, please select either \"X\" or \"O\" ")



  #Logic to put shapes in matrix --------------------------------------------
  winner=0
  if player_sel==1:
    first_player = player1
    second_player= player2
  else:
    first_player = player2
    second_player = player1
  
  while winner == 0:
    #add logic that checks if their choice was between 0-2
    first_player.position[0] = input("{}, what row would you like to place your {} shape? Pick a number between 0-2".format(first_player.name,first_player.shape))
    first_player.position[1] = input("{}, what column would you like to place your {} shape? Pick a number between 0-2".format(first_player.name,first_player.shape))
    matix[first_player.position[0],first_player.position[1]] = first_player.shape 

    for i in matrix:
      first_player_shape_counter = 0
      for j in i:
        if j == first_player.shape:
          first_player_shape_counter+=1
      if first_player_shape_counter == 3:
        winner = 1
        break
      if winner == 1:
        print("{} is the winner of tic tac toe!!!!!".format(first_player.name))
        break

    # break out of while loop if winner has been found 
    if winner == 1:
      break

 
    for i in list(range(0,3)):
      for j in list(range(0,3)):
        if matrix[j,i] == first_player.shape:
          first_player_shape_counter+=1
      if first_player_shape_counter == 3:
          winner = 1
          break
      if winner == 1:
        print("{} is the winner of tic tac toe!!!!!".format(first_player.name))
        break

    # break out of while loop if winner has been found 
    if winner == 1:
      break


    # insert logic to check diagonals
    for index in list(range(0,3)):
      if matrix[index,index] == first_player.shape:
        first_player_shape_counter+=1 
    if first_player_shape_counter == 3:
      winner =1
      print("{} is the winner of tic tac toe!!!!!".format(first_player.name))
    if winner == 1:
      break

    for column in list(range(0,3)):
      row = 2
      if matrix[row,column] == first_player.shape:
        first_player_shape_counter+=1
        row-=1
    if first_player_shape_counter == 3:
      winner =1
      print("{} is the winner of tic tac toe!!!!!".format(first_player.name))
    if winner == 1:
      break    
      
  
    #add logic that checks if their choice was between 0-2
    second_player.position[0] = input("{}, what row would you like to place your {} shape".format(second_player.name,second_player.shape))
    second_player.position[1] = input("{}, what column would you like to place your {} shape".format(second_player.name,second_player.shape))
    matix[second_player.position[0],second_player.position[1]] = second_player.shape 

    for i in matrix:
      second_player_shape_counter = 0
      for j in i:
        if j == second_player.shape:
          second_player_shape_counter+=1
      if second_player_shape_counter == 3:
        winner = 1
        break
      if winner == 1:
        print("{} is the winner of tic tac toe!!!!!".format(second_player.name))
        break

    # break out of while loop if winner has been found 
    if winner == 1:
      break

 
    for i in list(range(0,3)):
      for j in list(range(0,3)):
        if matrix[j,i] == second_player.shape:
          second_player_shape_counter+=1
      if second_player_shape_counter == 3:
          winner = 1
          break
      if winner == 1:
        print("{} is the winner of tic tac toe!!!!!".format(second_player.name))
        break

    # break out of while loop if winner has been found 
    if winner == 1:
      break


    # insert logic to check diagonals
    for index in list(range(0,3)):
      if matrix[index,index] == second_player.shape:
        second_player_shape_counter+=1 
    if second_player_shape_counter == 3:
      winner =1
      print("{} is the winner of tic tac toe!!!!!".format(second_player.name))
    if winner == 1:
      break

    for column in list(range(0,3)):
      row = 2
      if matrix[row,column] == second_player.shape:
        second_player_shape_counter+=1
        row-=1
    if second_player_shape_counter == 3:
      winner =1
      print("{} is the winner of tic tac toe!!!!!".format(second_player.name))
    if winner == 1:
      break