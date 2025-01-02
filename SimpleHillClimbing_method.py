class SimpleHillClimbing:
    def __init__(self, initial_doard):
        self.initial_doard = initial_doard

    def simplehillclimbing_algorithm(self):
        current_state = self.initial_doard
        visit_num = 0

        while True:
            children = current_state.next_step()

            if not children:
                print("No neighbors to evaluate, terminating.")
                break

            next_state = children[0]
            next_value = next_state.get_heuristic_value()

            if next_value < current_state.get_heuristic_value():
                current_state = next_state
                visit_num += 1
            else:
                print("Stop.")
                current_state.print_board()
                break

        print(f"\nNumber of Visited States: {visit_num}\n")
        return None
