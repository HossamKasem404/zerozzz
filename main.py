from gameone import ZeroSquaresGame

    

def main():  
      


  board1 = [
    ['X', 'X', 'X', 'X', 'X'],
    ['X', 'Y', '.', '.', 'X'],
    ['X', '.', 'GY', '.', 'X'],
    ['X', '.', '.', 'X', 'X'],
    ['.', 'X', 'X', 'X', '.']
  ]


  board2 = [
    ['X', 'X', 'X', 'X','X', 'X', 'X'],
    ['X', 'GB', 'X', 'GY','X', 'GR', 'X'],
    ['X', '.', '.', '.','.', '.', 'X'],
    ['X', 'Y', '.', '.','.', '.', 'X'],
    ['X', 'X', '.', '.','.', '.', 'X'],
    ['X', 'X', '.', 'R','.', 'B', 'X'],
    ['X', 'X', 'X', 'X','X', 'X', 'X'],
    ['X', 'X', 'X', 'X','X', 'X', 'X'],
  ]

  board3 = [
    ['X', 'X', 'X', 'X','X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'Y', 'R', 'B','C', '.', '.', '.', '.', '.', 'X'],
    ['X', '.', '.', '.','.', '.', 'GY', '.', '.', '.', 'X'],
    ['X', 'X', '.', '.','.', 'GC', '.', '.', '.', '.', 'X'],
    ['X', 'X', '.', '.','GB', '.', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', '.', 'GR','.', '.', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X','X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X','X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X','X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X','X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X','X', 'X', 'X', 'X', 'X', 'X', 'X'],
    
  ]

# اختيار اللوح

  choose = input("Choose The Board You prefer To Play (1/2/3): ")
  if choose == '1':
    game = ZeroSquaresGame(5, board1)

    game.play()
  elif choose == '2':
    game = ZeroSquaresGame(7, board2)
    
    game.play()
  elif choose == '3':
    game = ZeroSquaresGame(11, board3)
    game.play()
  else:
    print("Invalid choice")



if __name__ == "__main__":
    main()