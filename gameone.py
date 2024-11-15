import copy


class ZeroSquaresGame:
    
    previous_boards = []

    def __init__(self, n, board):
        self.n = n
        self.board = board
        ZeroSquaresGame.previous_boards.append(self.board)

    def print_board(self):
        for row in self.board:
            print(" ".join(row))
        print()

        

    def is_valid_move(self, x, y, dx, dy):
        if 0 <= x + dx < self.n and 0 <= y + dy < self.n:
            return self.board[x + dx][y + dy] in {'.', 'GY', 'GR', 'GB', 'GC'}
        return False

    def can_move_right(self, x, y):
        return self.is_valid_move(x, y, 0, 1)

    def can_move_left(self, x, y):
        return self.is_valid_move(x, y, 0, -1)

    def can_move_up(self, x, y):
        return self.is_valid_move(x, y, -1, 0)

    def can_move_down(self, x, y):
        return self.is_valid_move(x, y, 1, 0)

    def move(self, dx, dy):
        new_board = [row[:] for row in self.board]

        for x in range(self.n):
            for y in range(self.n):
                if self.board[x][y] not in {'X', 'GR', 'GB', 'GY', 'GC', '.'}:
                    nx, ny = x, y
                    while self.is_valid_move(nx, ny, dx, dy):
                        nx += dx
                        ny += dy
                        if new_board[x][y] == "Y" and self.board[nx][ny] == 'GY':
                            new_board[x][y] = '.'
                            new_board[nx][ny] = '.'
                            
                        if new_board[x][y] == "R" and self.board[nx][ny] == 'GR':
                            new_board[x][y] = '.'
                            new_board[nx][ny] = '.'
                            
                        if new_board[x][y] == "B" and self.board[nx][ny] == 'GB':
                            new_board[x][y] = '.'
                            new_board[nx][ny] = '.'

                        if new_board[x][y] == "C" and self.board[nx][ny] == 'GC':
                            new_board[x][y] = '.'
                            new_board[nx][ny] = '.'    

                    
                    while new_board[nx][ny] == "." and new_board[nx + dx][ny + dy] == ".":
                        nx += dx
                        ny += dy

                    if new_board[nx][ny] == "."  and new_board[x][y] in ["Y","R","B","C"]: 
                         new_board[x][y], new_board[nx][ny] = '.', new_board[x][y]

                    if new_board[nx][ny] == "GY" and new_board[x][y] in ["R","B","C"] :    
                         new_board[x][y], new_board[nx][ny] = '.', "GY,"+new_board[x][y]    

                              ####################       
                    if new_board[nx][ny] == "GB" and new_board[x][y] in ["R","Y","C"] :    
                         new_board[x][y], new_board[nx][ny] = '.', "GB,"+new_board[x][y]     
        
  
                            #####################      
                    if new_board[nx][ny] == "GR" and new_board[x][y] in ["Y","B","C"] :    
                         new_board[x][y], new_board[nx][ny] = '.', "GR,"+new_board[x][y]     
                            ####################  
                    if new_board[nx][ny] == "GC" and new_board[x][y] in ["R","B","Y"] :    
                         new_board[x][y], new_board[nx][ny] = '.', "GY,"+new_board[x][y]      
                     
                                  #####################                              
                    if new_board[nx][ny] == "." and new_board[x][y] in ["GY,R","GY,B","GY,C"] :
                        new_board[x][y], new_board[nx][ny] = 'GY', new_board[x][y].split(",")[1]  
                        ###################### 

                    if new_board[nx][ny] == "." and new_board[x][y] in ["GR,Y","GR,B","GR,C"] :
                        new_board[x][y], new_board[nx][ny] = 'GR', new_board[x][y].split(",")[1]         
                              ################# 

                    if new_board[nx][ny] == "." and new_board[x][y] in ["GB,Y","GB,R","GB,C"] :
                        new_board[x][y], new_board[nx][ny] = 'GB', new_board[x][y].split(",")[1]       
                            #################

                    if new_board[nx][ny] == "." and new_board[x][y] in ["GC,B","GC,R","GC,Y"] :
                            new_board[x][y], new_board[nx][ny] = 'GC', new_board[x][y].split(",")[1]  

        return ZeroSquaresGame(self.n, new_board)

    def win(self):
        for row in self.board:
            for cell in row:
                if cell in {"GY", "GR", "GB", "GR,Y", "GY,R", "GY,B", "GR,B", "GB,Y", "GB,R"}:
                    return False
        return True

  
    def play(self):
        previous_boards = [self.board]
        self.print_board()
                
        while True:
            if self.win():
                print("Congratulations! You are the winner!")
                break

            move = input("Enter move (w/a/s/d) or enter (h) to view the next state: ")
            if move == 'w':
                
                self = self.move(-1, 0)
                self.print_board()
                previous_boards.append(self.board)
            elif move == 's':
               
                self = self.move(1, 0)
                self.print_board()
                previous_boards.append(self.board)
            elif move == 'a':
                
                self = self.move(0, -1)
                self.print_board()
                previous_boards.append(self.board)
            elif move == 'd':
               
                self = self.move(0, 1)
                self.print_board()
                previous_boards.append(self.board)

            elif move == 'h':
                # for x in self.next_step():
                #          for row in x:
                #                 print(*row)  
                #          print()
                for x in self.next_step():
                      x.print_board()
                       
                        


                

                for x in self.next_step():
                         for row in x:
                                print(*row)  
                         print()
            elif move == 'i':   
                for i in previous_boards:
                    for row in i:
                        print(*row)
                    print()                   
                continue  
            
    
    



    def has_moved_before(self, new_board):
        for previous_board in ZeroSquaresGame.previous_boards:
            if previous_board == new_board:
                return True
        return False


    def next_step(self):
        out_next_step=[]
        print("Your valid next steps are:")         
        zzz = []
        for x in range(self.n):
            for y in range(self.n): 
                if self.board[x][y] not in {'X', 'GR', 'GB', 'GY', 'GC', '.'}:
                    zzz.append([x, y])

        for i in zzz:
            if self.can_move_up(i[0], i[1]) :
                
                out_next_step.append(self.move(-1,0))
                break
        for i in zzz:        
            if self.can_move_down(i[0], i[1]) :
                
                out_next_step.append(self.move(1,0))
                break
        for i in zzz:        
            if self.can_move_right(i[0], i[1]):
                
                out_next_step.append(self.move(0,1))
                break
        for i in zzz:        
            if self.can_move_left(i[0], i[1]) :
                
                out_next_step.append(self.move(0,-1))
                break

        return  out_next_step

