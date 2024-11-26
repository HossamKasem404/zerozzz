import heapq 

class UCS:
    def __init__(self, initial_board):
        self.initial_board = initial_board   
        self.visited_boards = set()  
        self.priority_queue = [] 
        self.successful_paths = []  


    def ucs_algorithm(self):

        heapq.heappush(self.priority_queue, (0,id(self.initial_board), self.initial_board, []))
        

        while self.priority_queue:
            cost,_, current_board, path = heapq.heappop(self.priority_queue)

            board_tuple = tuple(map(tuple, current_board.board))

            if board_tuple in self.visited_boards:
                continue

            self.visited_boards.add(board_tuple)

            if current_board.win():
                self.successful_paths.append(path + [current_board])

            
    

            for next_game,weight in self.generate_nextsteps_with_weights(current_board):
                
                if (tuple(map(tuple, next_game.board)) not in self.visited_boards ):
                    
                      heapq.heappush(self.priority_queue, (cost + weight ,id(next_game), next_game, path + [current_board]))

        
         
        
        if self.successful_paths:
                print("winning paths!")
                
                sum=0
                for  path in self.successful_paths:
                    sum += 1
                    print(f"Winning Path {sum}:")
                    print("___________")
                    step_sum=0
                    
                    for step in path:
                        step_sum +=1
                        print(f"Step {step_sum}:")
                        step.print_board()
        else:
                print("Game over.")

    

    def generate_nextsteps_with_weights(self, current_board):
       
        nextsteps = []
        for next_board in current_board.next_step():
            weight = self.calculate_weight(current_board, next_board)
            nextsteps.append((next_board, weight))
        return nextsteps

    def calculate_weight(self, current_board, next_board):
        
        weight = 0
        if current_board.board != next_board.board:
                    weight += 1
        return weight