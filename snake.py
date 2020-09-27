import consts


class Snake:

    def __init__(self, keys, game, pos, color, direction):
        self.control_keys = keys
        self.cells = [pos]
        self.game_manager = game
        self.color = color
        self.game_manager.add_snake(self)
        self.direction = direction

    def get_head(self):
        return self.cells[-1]

    def next_move(self):
        temp = self.go(self.direction)
        temp = [((temp[0] - consts.sx) // consts.cell_size), ((temp[1] - consts.sy) // consts.cell_size)]
        situation = self.game_manager.check_cell(temp)
        if situation == "fruit":
            self.cells.append(temp)
            self.game_manager.cells_class_build[temp[0]][temp[1]].set_color(self.color)
        elif situation == "empty_cell":
            self.cells.append(temp)
            self.game_manager.cells_class_build[temp[0]][temp[1]].set_color(self.color)
            last_cell = self.cells.pop(0)
            self.game_manager.cells_class_build[last_cell[0]][last_cell[1]].set_color(consts.back_color)
        else:
            self.game_manager.kill(self)
            
    def handle(self, keys):
        for key in keys:
            if key in self.control_keys:
                key = self.control_keys[key]
                if key == "UP" and self.direction != "DOWN":
                    self.direction = key
                    break
                elif key == "DOWN" and self.direction != "UP":
                    self.direction = key
                    break
                elif key == "RIGHT" and self.direction != "LEFT":
                    self.direction = key
                    break
                elif key == "LEFT" and self.direction != "RIGHT":
                    self.direction = key
                    break

# ---------------------------------------function_for_moving_cell----------------------------------------

    def go_right(self):
        pos = [self.get_head()[0], self.get_head()[1]]
        if pos[0]+1 > consts.table_size-1:
            temp_pos = self.game_manager.cells[0][pos[1]]
        else:
            temp_pos = self.game_manager.cells[pos[0]+1][pos[1]]
        return temp_pos

    def go_left(self):
        pos = [self.get_head()[0], self.get_head()[1]]
        if pos[0]-1 < 0:
            temp_pos = self.game_manager.cells[consts.table_size-1][pos[1]]
        else:
            temp_pos = self.game_manager.cells[pos[0]-1][pos[1]]
        return temp_pos

    def go_up(self):
        pos = [self.get_head()[0], self.get_head()[1]]
        if pos[1]-1 < 0:
            temp_pos = self.game_manager.cells[pos[0]][consts.table_size-1]
        else:
            temp_pos = self.game_manager.cells[pos[0]][pos[1]-1]
        return temp_pos

    def go_down(self):
        pos = [self.get_head()[0], self.get_head()[1]]
        if pos[1]+1 > consts.table_size-1:
            temp_pos = self.game_manager.cells[pos[0]][0]
        else:
            temp_pos = self.game_manager.cells[pos[0]][pos[1]+1]
        return temp_pos

    def go(self, _dir):
        if _dir == "UP":
            return self.go_up()
        elif _dir == "DOWN":
            return self.go_down()
        elif _dir == "RIGHT":
            return self.go_right()
        elif _dir == "LEFT":
            return self.go_left()
