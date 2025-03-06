def xorshift32(s):
    s ^= (s << 13) & 0xFFFFFFFF
    s ^= (s >> 17) & 0xFFFFFFFF
    s ^= (s << 5) & 0xFFFFFFFF
    return s & 0xFFFFFFFF


class RandomGenerator:
    def __init__(self, bits, seed):
        self.bits = bits
        self.state = seed

    def update(self):
        self.state = xorshift32(self.state)
        return self.state

    def random_number(self, n):
        return 1 + (self.update() % n)


class Coordinate:
    def __init__(self, col, row):
        self.col = col
        self.row = row

    def neighbors(self, last_col, last_row):
        offsets = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
        neighbors = []
        for dx, dy in offsets:
            new_col = chr(ord(self.col) + dx)
            new_row = self.row + dy
            if 'A' <= new_col <= last_col and 1 <= new_row <= last_row:
                neighbors.append(Coordinate(new_col, new_row))
        return neighbors


class Cell:
    def __init__(self):
        self.is_mine = False
        self.state = 'covered'


class Minesweeper:
    def __init__(self, last_col, last_row, num_mines, seed):
        self.last_col = last_col
        self.last_row = last_row
        self.num_mines = num_mines
        self.generator = RandomGenerator(32, seed)
        self.board = {}
        self.mines_placed = False
        self.init_board()

    def init_board(self):
        for col in range(ord('A'), ord(self.last_col) + 1):
            for row in range(1, self.last_row + 1):
                self.board[(chr(col), row)] = Cell()

    def place_mines(self, first_move):
        forbidden = set((n.col, n.row) for n in first_move.neighbors(self.last_col, self.last_row))
        forbidden.add((first_move.col, first_move.row))
        mines = set()
        while len(mines) < self.num_mines:
            col = chr(ord('A') + (self.generator.random_number(ord(self.last_col) - ord('A') + 1) - 1))
            row = self.generator.random_number(self.last_row)
            coord = (col, row)
            if coord not in forbidden and not self.board[coord].is_mine:
                self.board[coord].is_mine = True
                mines.add(coord)
        self.mines_placed = True

    def count_adjacent_mines(self, col, row):
        count = 0
        for neighbor in Coordinate(col, row).neighbors(self.last_col, self.last_row):
            if self.board.get((neighbor.col, neighbor.row)) and self.board[(neighbor.col, neighbor.row)].is_mine:
                count += 1
        return count

    def reveal(self, col, row):
        if (col, row) not in self.board or self.board[(col, row)].state != 'covered':
            return True
        self.board[(col, row)].state = 'uncovered'
        if self.board[(col, row)].is_mine:
            return False
        if self.count_adjacent_mines(col, row) == 0:
            for neighbor in Coordinate(col, row).neighbors(self.last_col, self.last_row):
                self.reveal(neighbor.col, neighbor.row)
        return True

    def toggle_flag(self, col, row):
        if (col, row) in self.board:
            cell = self.board[(col, row)]
            if cell.state == 'covered':
                cell.state = 'flagged'
            elif cell.state == 'flagged':
                cell.state = 'covered'

    def game_won(self):
        return all(cell.state == 'uncovered' or cell.is_mine for cell in self.board.values())

    def count_flags(self):
        return sum(1 for cell in self.board.values() if cell.state == 'flagged')

    def display(self, reveal_mines=False):
        print(f"[Flags {self.count_flags()}/{self.num_mines}]")
        print(' ' + ''.join(chr(c) for c in range(ord('A'), ord(self.last_col) + 1)))
        for row in range(1, self.last_row + 1):
            line = f"{str(row).zfill(2)}|"
            for col in range(ord('A'), ord(self.last_col) + 1):
                cell = self.board[(chr(col), row)]
                if cell.state == 'covered':
                    line += '#'
                elif cell.state == 'flagged':
                    line += '@'
                elif cell.is_mine and reveal_mines:
                    line += 'X'
                else:
                    count = self.count_adjacent_mines(chr(col), row)
                    line += str(count) if count > 0 else ' '
            print(line)


def minas(last_col, last_row, num_mines, seed, moves):
    game = Minesweeper(last_col, last_row, num_mines, seed)
    game.display()
    for coord, action in moves:
        col, row = coord[0], int(coord[1:])
        if not game.mines_placed:
            game.place_mines(Coordinate(col, row))
        if action == 'L':
            if not game.reveal(col, row):
                print(f"BOOM! You hit a mine at {coord}!")
                game.display(reveal_mines=True)
                return False
        elif action == 'M':
            game.toggle_flag(col, row)
        game.display()
        if game.game_won():
            print("VICTORY!!!")
            return True
    print("Game over. No more moves.")
    return False


if __name__ == "__main__":
    # insert the moves you want
    test_moves = [('M03', 'L'), ('V01', 'M'), ('W01', 'L')]
    minas('Z', 5, 6, 2, test_moves)
