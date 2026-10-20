class Graph:
    def __init__(self):
        self.nodes = {}
    
    def add_edge(self, node1, node2):
        if node1 not in self.nodes:
            self.nodes[node1] = []
        if node2 not in self.nodes:
            self.nodes[node2] = []
        self.nodes[node1].append(node2)
    
    def display(self):
        for node in self.nodes:
            print(node, "->", self.nodes[node])


class SnakeAndLadder:
    def __init__(self):
        self.graph = Graph()
        self.board_size = 100
        self.snakes = {
            99: 54,
            70: 55,
            52: 42,
            25: 2,
            95: 72
        }
        self.ladders = {
            6: 25,
            11: 40,
            60: 85,
            46: 90,
            17: 69
        }

    def create_board(self):
        for position in range(1, self.board_size):
            for dice in range(1, 7):
                next_position = position + dice

                if next_position > self.board_size:
                    continue

                if next_position in self.snakes:
                    next_position = self.snakes[next_position]
                elif next_position in self.ladders:
                    next_position = self.ladders[next_position]

                self.graph.add_edge(position, next_position)

    def play(self):
        position = 1

        while position < self.board_size:
            input("Press Enter to roll the dice...")
            import random
            dice = random.randint(1, 6)
            print("You rolled:", dice)

            if position + dice > self.board_size:
                print("You need an exact roll to reach 100.")
                continue

            position += dice

            if position in self.snakes:
                print("Snake! Going down to", self.snakes[position])
                position = self.snakes[position]
            elif position in self.ladders:
                print("Ladder! Climbing up to", self.ladders[position])
                position = self.ladders[position]

            print("Current position:", position)

        print("Congratulations! You won!")


game = SnakeAndLadder()
game.create_board()
game.play()