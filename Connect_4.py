# Program: "Connect-4". This program runs the Connect-4 game which is a 2 player game where each player takes turns placing chips into columns.The winner is the first to connect four chips vertically, horizontally, or diagonally.
# Author: Somaya Tamer Magdy Shoaib     ID: 20231225    
# Version: v5.0
# Date: 29/2/2024


# create a 2d list 
grid = [ #0   #1   #2   #3   #4   #5   #6    #7
        ['F', "#", "#", "#", "#", "#", "#", "#"],  # row0
        ['E', "#", "#", "#", "#", "#", "#", "#"],  # row1
        ['D', "#", "#", "#", "#", "#", "#", "#"],  # row2
        ['C', "#", "#", "#", "#", "#", "#", "#"],  # row3
        ['B', "#", "#", "#", "#", "#", "#", "#"],  # row4
        ['A', "#", "#", "#", "#", "#", "#", "#"],  # row5
        [' ',   1,   2,   3,   4,   5,   6,   7]   # row6
    ]

rows = 7
columns = 8
# Function to allow the 2D list to be organized under not next to each other
def game_board():
 print(" ** CONNECT-4 **")
 for i in range(rows):
     for j in range(columns):
         block=grid[i][j]
         print(block,end=" ")
     print("")    


# Function to put the user's input on game board 
def user_input(x,letter): # The purpose of the variable 'letter' is to append either 'X' or 'O', depending on whether it is player 1 or player 2
  choice = 'X' if letter == 1 else 'O'
  for i in range(rows):
    if grid[i][x]=="#":
       if grid[5][x]=="#":
          grid[5][x]=choice
          game_board()
          return True,5 # returning the number of row as well because it will be used in the horizontal function
       elif grid[4][x]=="#":
          grid[4][x]=choice
          game_board()
          return True,4
       elif grid[3][x]=="#":
          grid[3][x]=choice
          game_board()
          return True,3
       elif grid[2][x]=="#":
          grid[2][x]=choice
          game_board()
          return True ,2
       elif grid[1][x]=="#":
          grid[1][x]=choice
          game_board()
          return True ,1   
       elif grid[0][x]=="#":
          grid[0][x]=choice
          game_board()
          return True ,0   
  return False,None # because if i dont return none there will be an error later in the main game function when i ask for the boolean value         

# To check if the user is entering a vlid input or not
def Postive_integer_or_not(numb):
  if str(numb).isdigit() :
     int_numb= int(numb)
     if int_numb> 0 :
        return True
     elif int_numb <= 0 :
        return False
  else : 
     return False

# Function to check of vertical wins
    
def vertical_win(column_numb,letter): 
 choice = 'X' if letter == 1 else 'O'
 result = []
 for i in range(len(grid)):
      result.append(grid[i][column_numb])
 result.pop(6)   # dont include elements from row 6 

 count = 0
 for y in range(len(result)):
      if result[y] == choice:
         count += 1
      if count >= 4:
         for i in range(len(result) - 3): # Subtract by 3 to limit the loop iteration to stop at  the third  element in result list
            if result[i:i + 4] == [choice, choice, choice, choice]: # result[i:i + 4] that first i is not included
                  return True

 return False  

# Function to check of Horizontal wins
def Horizontal_win(row_numb,letter):
 choice = 'X' if letter == 1 else 'O'
 result = []
 for j in range(len(grid)):
      result.append(grid[row_numb][j]) # Bigest diffrence between the previous function is row number not column is inputed
 result.pop(0)   # dont include elements from column 0

 count = 0
 for y in range(len(result)):
      if result[y] == choice:
         count += 1
      if count >= 4:
         for i in range(len(result) - 3):
            if result[i:i + 4] == [choice, choice, choice, choice]: # result[i:i + 4] that first i is not included
                  return True

 return False

# Function to check of postive diagonal wins
def Postive_slop_diagonal_win(letter):
  
  all_diagonals_up = []
  for i in range(rows): # the logic behind it is simmilar to the shapes pattrens logic and the fact that in every diagonal there is a pattern of subtractig 1 from row  index and adding 1 to column index to obtain the next diagonal element
          column = 0
          diagonals = []
          while i >= 0:
              diagonals.append(grid[i][column])
              i -= 1
              column += 1
          diagonals.pop(0) # remove first column
          all_diagonals_up.append(diagonals)
  

  all_diagonals_lower = []
  for x in range(1, columns):
          diagonals_2 = []
          column_2 = x 
          rows_2= rows-1 
          while rows_2 >= 0 and column_2 < columns:
              diagonals_2.append(grid[rows_2][column_2])
              rows_2 -= 1
              column_2 += 1
          all_diagonals_lower.append(diagonals_2)    
      
  All= all_diagonals_up + all_diagonals_lower
  All.pop(0) # removing lists that contain less than 4 elements
  All.pop(12)
  All.pop(0)
  All.pop(10)
  All.pop(0)
  All.pop(8)
  All.pop(0)
  
  choice = 'X' if letter == 1 else 'O'

  for diagonal in All:
      count = 0
      for y in range(len(diagonal)):
          if diagonal[y] == choice:
              count += 1
          if count >= 4:
              for i in range(len(diagonal) - 3):
                  if diagonal[i:i + 4] == [choice, choice, choice, choice]:
                      return True
  return False   


# Function to check of Negative diagonal wins
def Negative_slop_diagonal_win(letter):
 new_grid = [row[1:] for row in grid] # remove first column from grid

 rows_1=6 # since size change after removing first column
 columns_1=7# since size change after removing first column

 reversed_grid=[] # reversing the grid 
 for i in range(len(new_grid)):
        reversed_grid.append(new_grid[i][::-1])
 reversed_grid.pop(6)        
      

 all_diagonals_up = []
 for i in range(rows_1):
              column = 0
              diagonals = []
              while i >= 0:
                  diagonals.append(reversed_grid[i][column])
                  i -= 1
                  column += 1

              all_diagonals_up.append(diagonals)


 all_diagonals_lower = []
 for x in range(1, columns_1):
              diagonals_2 = []
              column_2 = x 
              rows_2= rows_1-1 
              while rows_2 >= 0 and column_2 < columns_1:
                  diagonals_2.append(reversed_grid[rows_2][column_2])
                  rows_2 -= 1
                  column_2 += 1
              all_diagonals_lower.append(diagonals_2)    
     
 All= all_diagonals_up + all_diagonals_lower
 All.pop(0)
 All.pop(10)
 All.pop(0)
 All.pop(8)
 All.pop(0)
 All.pop(6)


 choice = 'X' if letter == 1 else 'O'
 for diagonal in All:
          count = 0
          for y in range(len(diagonal)):
              if diagonal[y] == choice:
                  count += 1
              if count >= 4:
                  for i in range(len(diagonal) - 3):
                      if diagonal[i:i + 4] == [choice, choice, choice, choice]:
                          return True
 return False  

# A Function to reset the game board if user doesnt exit the game and plays more than once 
def Reset_board(grid):
    for i in range(6):
        for j in range(1, 8):
            grid[i][j] = "#"
    return grid


def Draw_or_not(grid):
    for row in grid:
        if '#' in row:
            return True
    return False

# Main Game Loop 
def Main_Game():
 while True:
   Reset_board(grid)

   print('** Welcome to "Connect-4" Game! **')
   print("A) Play")
   print("B) How to play")
   print("C) Exit")
   option = input("Please enter your choice (A/B/C):")

   if option == 'A' or option== 'a': 
      game_board()
      
      #Player 1's turn  
      
      while True:
          player_1=input("Player 1 enter number of column :")
 
          if not Postive_integer_or_not(player_1):
             print ("** Invalid, please insert a valid number between (1-7) **")
             continue
          elif int(player_1) <= 0 or int(player_1)>7:
             print ("** Invalid, please insert a valid number between (1-7) **")
             continue
          else:
               boolean, index =user_input(int(player_1),1) 

          if boolean == True:
                if vertical_win(int(player_1),1):
                    print("PLAYER 1 WON !!!")
                    break
                elif Horizontal_win(index,1):
                    print("PLAYER 1 WON !!!")
                    break
                elif Postive_slop_diagonal_win(1):
                    print("PLAYER 1 WON !!!")
                    break
                elif Negative_slop_diagonal_win(1):
                    print("PLAYER 1 WON !!!")
                    break
          elif boolean== False:
                     print("** Invalid.The column is full, please choose another column **")
                     continue
          
          while True:
                 break_of_both=0
                 # Player 2's turn
                 player_2=input("Player 2 enter number of column :")
                 if not Postive_integer_or_not(player_2):
                   print ("** Invalid, please insert a valid number between (1-7) **")
                   continue
                 elif int(player_2) <= 0 or int(player_2)>7:
                   print ("** Invalid, please insert a valid number between (1-7) **")
                   continue
                 else: 
                    boolean, index =user_input(int(player_2),2)
                 
                 if boolean==True:
                   if vertical_win(int(player_2),2):
                     print("PLAYER 2 WON !!!")
                     break_of_both= 1
                     break
                   elif Horizontal_win(index,2):
                     print("PLAYER 2 WON !!!")
                     break_of_both= 1
                     break
                   elif Postive_slop_diagonal_win(2):
                     print("PLAYER 2 WON !!!")
                     break_of_both= 1
                     break
                   elif Negative_slop_diagonal_win(2):
                     print("PLAYER 2 WON !!!")
                     break_of_both= 1
                     break   
                   else:
                       break_of_both= 0
                       break                
                 elif boolean==False: 
                        print("** Invalid.The column is full, please choose another column **")
                        continue
          
          if break_of_both== 1: # to break out of both loops
                 break
          if not Draw_or_not(grid):
              print("IT'S A DRAW")
              break

                 
   elif option == 'B' or option=='b':
     # Display game instructions
     print('** How to play: **\n"Connect-4" is a two-player game where each player takes turns placing chips into columns.\nAs the name suggests, the objective is to connect 4 chips either vertically, horizontally, or diagonally.\nThe player who connect 4 chips first is the winner.')
   elif option == 'C' or option== 'c':
     # Break loop to exit game
     print("** Game Exited **")
     break 
   else:
     print("** Invalid, Please enter A or B or C **")

if __name__ == '__main__':
    Main_Game()