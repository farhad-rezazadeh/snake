import consts

from cell import Cell


class GameManager:

    def __init__(self, size, screen, sx, sy, block_cells):
        self.size = size
        self.screen = screen
        self.sx = sx
        self.sy = sy
        self.cells = [[(self.sx+x*consts.cell_size, self.sy+y*consts.cell_size) for y in range(self.size)]
                      for x in range(self.size)]
        self.cells_class_build = [[Cell(screen, self.cells[i][j][0], self.cells[i][j][1], consts.back_color)
                                   for j in range(self.size)] for i in range(self.size)]
        self.snakes = []
        self.block_cells = consts.block_cells
        for block_cells in block_cells:
            self.cells_class_build[block_cells[0]][block_cells[1]].set_color(consts.block_color)
        self.turn = 0

    def add_snake(self, snake):
        self.snakes.append(snake)
        self.cells_class_build[snake.get_head()[0]][snake.get_head()[1]].set_color(snake.color)

    def get_cell(self, pos):
        if pos[0] in list(range(0, self.size)) and pos[1] in list(range(0, self.size )):
            return self.cells_class_build[pos[0]][pos[1]]
        else:
            return None

    def kill(self, killed_snake):
        self.snakes.remove(killed_snake)

    def get_next_fruit_pos(self):  # returns tuple (x, y) that is the fruit location
        ret = -1, -1
        mx = -100

        for i in range(0, self.size):
            for j in range(0, self.size):

                mn = 100000000

                for x in range(0, self.size):
                    for y in range(0, self.size):
                        if self.get_cell((x, y)).color != consts.back_color:
                            mn = min(mn, int(abs(x - i) + abs(y - j)))

                if mn > mx:
                    mx = mn
                    ret = i, j

        return ret

    def check_cell(self, pos):
        cell = self.get_cell(pos)
        if cell.color == consts.fruit_color:
            return "fruit"
        elif cell.color == consts.back_color:
            return "empty_cell"
        else:
            return "barrier"

    def handle(self, keys):
        for snake in self.snakes:
            snake.handle(keys)
        for snake in self.snakes:
            snake.next_move()
        self.turn += 1
        if self.turn % 10 == 0:
            fruit_pos = self.get_next_fruit_pos()
            self.cells_class_build[fruit_pos[0]][fruit_pos[1]].set_color(consts.fruit_color)
