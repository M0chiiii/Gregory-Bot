#to-do: go over translated code to fully make it good
#fiddle with user input section to loop until valid input
  #rename input variable to user_input
#this code WILL break as it currently is
#change user input section to work with emojis or smth instead of typing in numbers

def main(self, args) :
  #--variables--
  board = [[None] * (3) for _ in range(3)]
  # X = true, O = false, null = empty

  turn = True
  # turn: true = p1, false = p2

  outcome = 0
  # 1 = p1, 2 = p2, 3 = tie
  #--end variable declartion--



  while (outcome == 0):
  
  # --display--
  self.Display(board) #uses the Display() function, go to the bottom of the code for it
  # --end display--

  # --user input section--
  if (turn): #runs if turn is true, which is player 1
    print("\nPlayer 1\'s", end ="")
  else:
    print("\nPlayer 2\'s", end ="")
  print(" turn:")

  #the part where you physically type the text, can be ignored if emojis
  print("Write the two numbers on the board like it\'s a game of battleship. The first number gets the row, the second gets the column.")
  print("Example: 11 gets topmost left corner, 12 gets row 1 column 2, etc.")
  user_input = input("Input your desired position:")

  #loop until user input is valid (if typing)
  #valid if: 
   
'''
  #--user input check section--
  #  input = 0
  #  while (True) :
  #     while True :
  #     user_input = input()
  #     if(((int(input / 10) < 1 or int(input / 10) > 3) and (input % 10 < 1 or input % 10 > 3)) == False) :
  #      break
  #     if (board[(int(input / 10)) - 1][(input % 10) - 1] != None):
  #       print("There is already an input on row " + str((int(input / 10))) + ", column " + str((input % 10)) + ". Try again.")
  #     else:
  #       break
  #     # end while loop

  #           if (turn) :
  #               board[(int(input / 10)) - 1][(input % 10) - 1] = True
  #               turn = False
  #           else :
  #               board[(int(input / 10)) - 1][(input % 10) - 1] = False
  #               turn = True
  #           # --end user input--
'''

  # --win conditions--
  spotsFilled = 0
  column = 0
  while (column < len(board)):
    row = 0
    while (row < len(board[column])):
      if (spotsFilled == len(board) * len(board)) : outcome = 3
      if (board[row][column] != None):
        spotsFilled += 1
        if (self.CheckWin(board[row][column], column, row, board)) :
          if (board[row][column]):
            outcome = 1
          elif (not board[row][column]):
            outcome = 2
      row += 1
    column += 1
  #--end win conditions--


    self.Display(board)
      if (outcome != 3) :
          print("The winner is", end ="")
          if (outcome == 1) : print(" Player 1.")elif (outcome == 2) : print(" Player 2.")
      else:
        print("The game is a tie.")
    # end main()



def  CheckWin(self, p,  col,  r,  brd) :
  player = p
  column = col
  row = r
  board = brd
  win = False # set true to end game if player wins
    
  inARow = 0 # how many times user has moves in a row
    
  # --checks horizontally--
  i = 0
  while (i < len(board)):
    if (player) : # if p1 at current row column
      if (inARow == 3):
        win = True
        return  win
      elif (board[row][i] != None and board[row][i]):
        inARow += 1
      else:
        inARow = 0
        break

    else: #p2
      if (inARow == 3) :
        win = True
        return  win
      elif (board[row][i] != None and not board[row][i]) : inARow += 1else :
        inARow = 0
        break
      i += 1
    # --end of check horizontally--

    # --checks vertically--
    i = 0
    while (i < len(board)) :
      if (player): # if p1 at current row column
        if (inARow == 3) :
          win = True
          return  win
        elif (board[i][column] != None and board[i][column]):
          inARow += 1
        else:
          inARow = 0
          break
        
        else: #p2
          if (inARow == 3) :
            win = True
            return  win
          elif (board[i][column] != None and not board[i][column]):
            inARow += 1
          else:
            inARow = 0
            break
     i += 1
    # --end of check vertical--
    
    # --check diagonally--
    if (row == 2 and column == 2):
      #do nothing lmao, r2c2 has too many win variations
    elif (row == column): # row 1 column 1 || row 3 column 3
      i = 0
      while (i < len(board)) :
        if (player): # p1 check
          if (inARow == 3) :
            win = True
            return  win
          elif (board[i][i] != None and board[i][i]):
            inARow += 1
          else:
            inARow = 0
          break

        else : # p2 check
          if (inARow == 3) :
            win = True
            return  win
          elif (board[i][i] != None and board[i][i]):
            inARow += 1
          else:
            inARow = 0
            break
        i += 1

    else: # row 1 column 3 || row 3 column 1
      i = 0
      while (i < len(board)): # row 1, 3
        a = 3
        while (a < len(board)): # column 3, 1
          if (player): # p1 check
            if (inARow == 3) :
              win = True
              return  win
            elif (board[i][a] != None and board[i][a]):
              inARow += 1
              else:
                inARow = 0
                break
            else: #p2 check
              if (inARow == 3) :
                win = True
                return  win
            elif (board[i][a] != None and board[i][a]):
              inARow += 1
            else:
              inARow = 0
              break
          a -= 1
        i += 1
    # --end of check diagonal--
  if (inARow == 3) : # emergency button to make win true if the above return wins in the loop doesnt work :')
    win = True

  return  win
  # end CheckWin()

    
def Display(self, brd) :
  board = brd
  
  a = 0
  while (a < len(board)) :
    print("| ", end ="")
    b = 0
    while (b < len(board)) :
      if (board[a][b] == None):
        print("_", end ="")
      elif (board[a][b]):
        print("X", end ="")
      else:
        print("O", end ="")
        print(" | ", end ="")
      b += 1
      print()
   a += 1