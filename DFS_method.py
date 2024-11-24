

# class DFS:
    
#     def __init__(self, initial_doard):
#         self.initial_doard = initial_doard
#         self.visited_boards = set()  

#     def DFS_algorithm(self):
#         stack = [(self.initial_doard, [])]
#         successful_paths = []

#         while stack:
#             current_board, path = stack.pop()

            
#             if current_board.win():
#                 successful_paths.append(path + [current_board])
#                 continue   

            
#             board_tuple = tuple(map(tuple, current_board.board))  
#             if board_tuple in self.visited_boards:
#                 continue
#             else:
#               self.visited_boards.add(board_tuple)

#             for next_game in current_board.next_step():
#                 if  tuple(map(tuple, next_game.board)) not in self.visited_boards:
#                     stack.append((next_game, path + [current_board]))

#         if successful_paths:
#             print("winning paths!")
            
#             sum=0
#             for  path in successful_paths:
#                 sum += 1
#                 print(f"Winning Path {sum}:")
#                 print("___________")
#                 step_sum=0
                
#                 for step in path:
#                     step_sum +=1
#                     print(f"Step {step_sum}:")
#                     step.print_board()
#             return True
#         else:
#             print("Game over.")
        
    

class DFS:
    def __init__(self, initial_board):
        self.initial_board = initial_board
        self.visited_boards = set()
        self.successful_paths = []

    def DFS_recursive(self, current_board, path):
        if current_board.win():
            self.successful_paths.append(path + [current_board])
            return

        board_tuple = tuple(map(tuple, current_board.board))

        if board_tuple in self.visited_boards:
            return

        self.visited_boards.add(board_tuple)

        for next_game in current_board.next_step():
            if tuple(map(tuple, next_game.board)) not in self.visited_boards:
                self.DFS_recursive(next_game, path + [current_board])

    def find_all_successful_paths(self):
        self.DFS_recursive(self.initial_board, [])
        return self.successful_paths
