import heapq
import copy

class ASTAR:
    def __init__(self, initial_board):
        self.initial_board = initial_board
        self.priority_queue = []
        self.visited = {}
        self.states = []
        self.current_state = None

    def hash_board(self, board):
       
        return str(board)

    def A_STAR_algorithm(self):
        parent_map = {}
        depth = 0
        visit_num = 0

        heapq.heappush(self.priority_queue, (0, self.initial_board))
        cost_map = {self.hash_board(self.initial_board.board): 0}

        while self.priority_queue:
            _, self.current_state = heapq.heappop(self.priority_queue)
            board_hash = self.hash_board(self.current_state.board)

            if self.current_state.win():
                self.visited[board_hash] = True
                visit_num += 1
                self.states.append(self.current_state)

                while board_hash in parent_map:
                    depth += 1
                    self.current_state = parent_map[board_hash]
                    self.states.append(self.current_state)
                    board_hash = self.hash_board(self.current_state.board)

                print("Path to solution:")
                for index, state in enumerate(reversed(self.states)):
                    print(f"Board_Number: -{index}-")
                    state.print_board()
                    print()

                print(f"The depth of A* search: {depth + 1}")
                break

            if board_hash not in self.visited:
                self.visited[board_hash] = True
                visit_num += 1

                children = self.current_state.next_step()
                for child in children:
                    child_hash = self.hash_board(child.board)

                    cost_to_child = cost_map[board_hash] + child.get_move_cost()

                    heuristic_value = child.get_heuristic_value()

                    priority = cost_to_child + heuristic_value

                    if child_hash not in cost_map or cost_to_child < cost_map[child_hash]:
                        heapq.heappush(self.priority_queue, (priority, child))
                        cost_map[child_hash] = cost_to_child
                        parent_map[child_hash] = copy.deepcopy(self.current_state)

        print("\nNumber of Visited:")
        print(visit_num)
        print("\nThe Cost Of Goal:")
        print(cost_to_child)
        return None
