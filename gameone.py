import copy
from DFS_R_method import DFS_R
from DFS_method import DFS
from BFS_method import BFS
from UCS_method import UCS
from astar import AStar



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
        new_board = self.board
        new_board = copy.deepcopy(self.board)  # عمل نسخة عميقة من اللوحة
        ZeroSquaresGame.previous_boards.append(copy.deepcopy(self.board))
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
                if cell in {'GY', 'GR', 'GB', 'GC', 'GR,Y', 'GY,R', 'GY,B', 'GY,C', 'GR,C', 'GR,B', 'GB,Y', 'GB,R', 'GB,C'}:
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
                for x in self.next_step():
                         for row in x:
                                print(*row)  
                         print()
                
                  
            elif move == 'DFS':
                    dfs = DFS(self)
                    if dfs.DFS_algorithm():
                      break

            elif move == 'BFS':
                    bfs = BFS(self)
                    if bfs.BFS_algorithm():
                      break 


            elif move == 'DFS_R':
                    dfs_r = DFS_R(self)
                    if dfs_r.DFS_recursive(self):
                      break
                    if dfs_r.find_all_successful_paths():
                      break

            elif move == 'UCS':
                    ucs = UCS(self)
                    if ucs.ucs_algorithm():
                      break 

            elif move == 'star':
                    star = AStar(self)
                    if star.a_star_algorithm():
                      break              
        

            elif move == 'i':   
                for i in previous_boards:
                    for row in i:
                        print(*row)
                    print()                   
                continue  
            
            else:
                print("Invalid move")
            continue

        
    def next_step(self):
                out_next_step = []
                zzz = []

                for x in range(self.n):
                    for y in range(self.n):
                        if self.board[x][y] not in {'X', 'GR', 'GB', 'GY', 'GC', '.'}:
                            zzz.append([x, y])

                for i in zzz:
                    if self.can_move_up(i[0], i[1]):
                        new_step = self.move(-1, 0)
                        out_next_step.append(new_step)

                    if self.can_move_down(i[0], i[1]):
                        new_step = self.move(1, 0)
                        out_next_step.append(new_step)

                    if self.can_move_right(i[0], i[1]):
                        new_step = self.move(0, 1)
                        out_next_step.append(new_step)

                    if self.can_move_left(i[0], i[1]):
                        new_step = self.move(0, -1)
                        out_next_step.append(new_step)

                return out_next_step
    

    def remaining_steps_to_win(self):
        goals = {"GY", "GR", "GB", "GC"}
        colored_squares = {"Y", "R", "B", "C"}
        total_distance = 0

        for x in range(self.n):
            for y in range(self.n):
                if self.board[x][y] in colored_squares:
                    closest_goal_distance = float("inf")
                    for i in range(self.n):
                        for j in range(self.n):
                            if self.board[i][j] in goals:
                                distance = abs(x - i) + abs(y - j)
                                closest_goal_distance = min(
                                    closest_goal_distance, distance
                                )
                    total_distance += closest_goal_distance

        return total_distance