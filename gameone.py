import copy
from DFS_R_method import DFS_R
from DFS_method import DFS
from BFS_method import BFS
from SimpleHillClimbing_method import SimpleHillClimbing
from SteepestAscentHillClimbing_method import SteepestAscentHillClimbing
from UCS_method import UCS
from ASTAR_method import ASTAR



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
            return self.board[x + dx][y + dy] in {'.', 'GY', 'GR', 'GB', 'GC','GO','E','W'}
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
       
        for x in range(self.n):
            for y in range(self.n):
                if self.board[x][y] not in {'X', 'GR', 'GB', 'GY', 'GC','GO', '.'}:
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
                        
                        if new_board[x][y] == "O" and self.board[nx][ny] == 'GO':
                            new_board[x][y] = '.'
                            new_board[nx][ny] = '.' 


                    if new_board[nx][ny] == "W":
                        if new_board[x][y] == "R":
                            if new_board[nx + dx][ny + dy] == "X":
                                new_board[nx][ny] = "GR,R"
                                new_board[x][y] = "."
                            else:
                                new_board[nx][ny] = "GR"
                        
                        if new_board[x][y] == "O":
                            if new_board[nx + dx][ny + dy] == "X":
                                new_board[nx][ny] = "GO,O"
                                new_board[x][y] = "."
                            else:
                                new_board[nx][ny] = "GO"

                        if new_board[x][y] == "B":
                            if new_board[nx + dx][ny + dy] == "X":
                                new_board[nx][ny] = "GB,B"
                                new_board[x][y] = "."
                            else:
                                new_board[nx][ny] = "GB"

                        if new_board[x][y] == "Y":
                            if new_board[nx + dx][ny + dy] == "X":
                                new_board[nx][ny] = "GY,Y"
                                new_board[x][y] = "."
                            else:
                                new_board[nx][ny] = "GY"

                        if new_board[x][y] == "C":
                            if new_board[nx + dx][ny + dy] == "X":
                                new_board[nx][ny] = "GC,C"
                                new_board[x][y] = "."
                            else:
                                new_board[nx][ny] = "GC"
                        elif new_board[nx][ny] == "GC":
                            new_board[nx][ny] = "."

                    elif (
                        (new_board[nx][ny] == "GR" and new_board[x][y] == "R") or
                        (new_board[nx][ny] == "GB" and new_board[x][y] == "B") or
                        (new_board[nx][ny] == "GY" and new_board[x][y] == "Y") or
                        (new_board[nx][ny] == "GC" and new_board[x][y] == "C") or
                        (new_board[nx][ny] == "GO" and new_board[x][y] == "O")
                    ):
                        new_board[nx][ny] = "."
                        


                                

                    while new_board[nx][ny] == "." and new_board[nx + dx][ny + dy] == ".":
                        nx += dx
                        ny += dy

                     

                    if new_board[nx][ny] == "."  and new_board[x][y] in ["Y","R","B","C","O"]: 
                         new_board[x][y], new_board[nx][ny] = '.', new_board[x][y]

                         #################### اندماج

#####################
                    if new_board[nx][ny] == "GY" and new_board[x][y] in ["R","B","C","O"] :    
                         new_board[x][y], new_board[nx][ny] = '.', "GY,"+new_board[x][y]    

                                     
                    if new_board[nx][ny] == "GB" and new_board[x][y] in ["R","Y","C","O"] :    
                         new_board[x][y], new_board[nx][ny] = '.', "GB,"+new_board[x][y]     
             
                    if new_board[nx][ny] == "GR" and new_board[x][y] in ["R","Y","C","O"] :    
                         new_board[x][y], new_board[nx][ny] = '.', "GR,"+new_board[x][y]     
                              
                    if new_board[nx][ny] == "GC" and new_board[x][y] in ["R","Y","C","O",'C'] :    
                         new_board[x][y], new_board[nx][ny] = '.', "GY,"+new_board[x][y]

                    if new_board[nx][ny] == "GO" and new_board[x][y] in ["R","Y","C","B"] :    
                         new_board[x][y], new_board[nx][ny] = '.', "GY,"+new_board[x][y]            
                     
                                  #####################     انفصال                         
                    if new_board[nx][ny] == "." and new_board[x][y] in ["GY,R","GY,B","GY,C","GY,O","GY,Y"] :
                        new_board[x][y], new_board[nx][ny] = 'GY', new_board[x][y].split(",")[1]  
                         

                    if new_board[nx][ny] == "." and new_board[x][y] in ["GR,Y","GR,B","GR,C","GR,O","GR,R"] :
                        new_board[x][y], new_board[nx][ny] = 'GR', new_board[x][y].split(",")[1]         
                               

                    if new_board[nx][ny] == "." and new_board[x][y] in ["GB,Y","GB,R","GB,C","GB,O","GB,B"] :
                        new_board[x][y], new_board[nx][ny] = 'GB', new_board[x][y].split(",")[1]       
                            

                    if new_board[nx][ny] == "." and new_board[x][y] in ["GC,B","GC,R","GC,Y","GC,O","GC,C"] :
                            new_board[x][y], new_board[nx][ny] = 'GC', new_board[x][y].split(",")[1]
                            
                    if new_board[nx][ny] == "." and new_board[x][y] in ["GO,B","GO,R","GO,Y","GB,O","GO,O"] :
                            new_board[x][y], new_board[nx][ny] = 'GO', new_board[x][y].split(",")[1]           
                            ################
                            #القواعد الجديدة 
                    if new_board[nx][ny] == "E" and new_board[x][y] in ["C","R","Y","B","O"] :
                        new_board[x][y], new_board[nx][ny] = '.','.' 

                     #####################################
                    


        return ZeroSquaresGame(self.n, new_board)

    def win(self):
        for row in self.board:
            for cell in row:
                if cell in {'GY', 'GR', 'GB', 'GC','GO', 'GR,Y', 'GR,C', 'GR,B' , 'GR,O','GR,R','GY,R', 'GY,B', 'GY,C','GY,O','GY,Y', 'GB,Y', 'GB,R', 'GB,C','GB,O','GB,B','GO,Y', 'GO,R', 'GO,C','GO,O','GO,B','GC,Y', 'GC,C', 'GC,B' , 'GC,O','GC,R','C','R','B','Y','O'}:
                    
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

            elif move == 'A':
                    astar = ASTAR(self)
                    if astar.A_STAR_algorithm():
                      break 

            elif move == 'S':
                    simplehillclimbing = SimpleHillClimbing(self)
                    if simplehillclimbing.simplehillclimbing_algorithm():
                      break      

            elif move == 'ST':
                    steepestascenthillclimbing = SteepestAscentHillClimbing(self)
                    if steepestascenthillclimbing.steepest_ascent_hill_climbing():
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

    
    
    def get_heuristic_value(self):
            score = 0

            targets = { 
                'B': 'GB',
                'R': 'GR',
                'Y': 'GY',
                'C': 'GC',
                

                'GR,Y': 'GY',
                'GC,Y': 'GY',
                'GB,Y': 'GY',
                'GY,Y': 'GY',

                'GB,C': 'GC',
                'GR,C': 'GC',
                'GY,C': 'GC',
                'GC,C': 'GC',

                'GY,R': 'GR',
                'GC,R': 'GR',
                'GB,R': 'GR',
                'GR,R': 'GR',

                'GC,B': 'GB',
                'GY,B': 'GB',
                'GR,B': 'GB',
                'GB,B': 'GB',

                
            }

            locations = {}
            for x in range(self.n):
                for y in range(len(self.board[x])):
                    cell = self.board[x][y]
                    if cell in targets or cell in targets.values():
                        locations[cell] = (x, y)

            for box, goal in targets.items():
                if box in locations and goal in locations:
                    box_location = locations[box]
                    goal_location = locations[goal]
                    distance = abs(box_location[0] - goal_location[0]) + abs(box_location[1] - goal_location[1])
                    score += distance

            return score



    def get_move_cost(self):
        directions = [
            (0, 1),   # Right
            (0, -1),  # Left
            (-1, 0),  # Up
            (1, 0)    # Down
        ]

        total_cost = 0

        for x in range(self.n):
            for y in range(self.n):
                if self.board[x][y] not in {'X', 'GR', 'GB', 'GY', 'GC', '.'}:
                    for dx, dy in directions:
                        new_x = x + dx
                        new_y = y + dy

                        if (0 <= new_x < self.n and 0 <= new_y < len(self.board[new_x])
                                and self.is_valid_move(x, y, dx, dy)):
                            total_cost += 1

        return total_cost


