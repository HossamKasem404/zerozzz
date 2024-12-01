import heapq


class AStar:
    def init(self, initial_board):
        self.initial_board = initial_board
        self.visited_boards = set()
        self.priority_queue = []
        self.successful_paths = []

    def heuristic(self, current_board):

        return current_board.remaining_steps_to_win()

    def a_star_algorithm(self):
        heapq.heappush(
            self.priority_queue,
            (
                0 + self.heuristic(self.initial_board),
                0,
                id(self.initial_board),
                self.initial_board,
                [],
            ),
        )

        while self.priority_queue:
            total_cost, cost, _, current_board, path = heapq.heappop(
                self.priority_queue
            )
            board_tuple = tuple(map(tuple, current_board.board))

            if board_tuple in self.visited_boards:
                continue

            self.visited_boards.add(board_tuple)

            if current_board.win():
                self.successful_paths.append(path + [current_board])

            for next_game, weight in self.generate_nextsteps_with_weights(
                current_board
            ):
                if tuple(map(tuple, next_game.board)) not in self.visited_boards:
                    g_cost = cost + weight
                    h_cost = self.heuristic(next_game)
                    total_cost = g_cost + h_cost
                    heapq.heappush(
                        self.priority_queue,
                        (
                            total_cost,
                            g_cost,
                            id(next_game),
                            next_game,
                            path + [current_board],
                        ),
                    )

        if self.successful_paths:
            print("Winning paths found using A*!")
            for i, path in enumerate(self.successful_paths, start=1):
                print(f"Winning Path {i}:")
                for step in path:
                    step.printtheboard()
        else:
            print("Game over. No winning paths found using A*.")

    def generate_nextsteps_with_weights(self, current_board):

        nextsteps = []
        for next_board in current_board.next_step():
            weight = self.calculate_weight(current_board, next_board)
            nextsteps.append((next_board, weight))
        return nextsteps

    def calculate_weight(self, current_board, next_board):

        current_distance = current_board.remaining_steps_to_win()
        next_distance = next_board.remaining_steps_to_win()

        weight = 1 + abs(current_distance - next_distance)
        print(weight)
        return max(1, weight)