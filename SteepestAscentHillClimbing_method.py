class SteepestAscentHillClimbing:
    def __init__(self, initial_board):
        self.initial_board = initial_board

    def steepest_ascent_hill_climbing(self):
        current_state = self.initial_board
        visit_num = 0

        while True:
            children = current_state.next_step()  

            best_child = None
            best_value = float('inf')  

            for child in children:
                value = child.get_heuristic_value()

                if value < best_value: 
                    best_value = value
                    best_child = child

            if best_child is None or best_value >= current_state.get_heuristic_value():
                print("Stop.")
                current_state.print_board()
                break

            current_state = best_child  
            visit_num += 1

        print("\nNumber of Visited States:", visit_num)
        return None
