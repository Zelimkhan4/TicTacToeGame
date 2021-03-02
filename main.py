import pygame


class Board:
    def __init__(self, width, height, left, top, cell_size):
        self.width = width
        self.height = height
        self.left = left
        self.top = top
        self.cell_size = cell_size
        # Cписок с цветами
        self.player = 'x'
        self.board = [[0] * self.width for i in range(self.height)]
        self.player_dict = {'x': 'o', 'o': 'x'}

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for row in range(self.height):
            for col in range(self.width):
                rect = pygame.Rect(self.left + (col * self.cell_size), self.top + (row * self.cell_size), self.cell_size, self.cell_size)
                # Рисую белую границу
                pygame.draw.rect(screen, pygame.Color("white"), rect, 1)
                if self.board[row][col] == 'x':
                    self.draw_x((row, col))
                elif self.board[row][col] == 'o':
                    self.draw_o((row, col))
                
    
    def interface(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.add_into_map(cell)
        # Дальше всё ограничивается только фантазией

    def get_cell(self, mouse_pos):
        for row in range(self.height):
            for col in range(self.width):
                upper_left = (self.left + (col * self.cell_size), (self.top + (row * self.cell_size)))
                if upper_left[0] < mouse_pos[0] < upper_left[0] + self.cell_size and\
                    upper_left[1] < mouse_pos[1] < upper_left[1] + self.cell_size:
                    # Возвращаю значение в виде (строка, столбец)
                    return row, col

    def draw_x(self, cell):
        row, col = cell
        point1 = (self.left + self.cell_size * col + 2, self.top + self.cell_size * row + 2)
        point2 = (self.left + self.cell_size * col + self.cell_size, self.top + self.cell_size * row + self.cell_size)
        
        point3 = (self.left + self.cell_size * col + self.cell_size - 2, self.top + self.cell_size * row - 2)
        point4 = (self.left + self.cell_size * col - 2, self.top + self.cell_size * row + self.cell_size - )
        #pygame.draw.line(screen, (0, 0, 255), point1, point2, 2)                                              
        pygame.draw.line(screen, (0, 0, 255), point3, point4, 2)
    
    def draw_o(self, cell):
        row, col = cell
        center = (self .left + col * self.cell_size + self.cell_size // 2,
                 self.top + row * self.cell_size + self.cell_size // 2)
        radius = self.cell_size // 2 - 4
        pygame.draw.circle(screen, (255, 0, 0), center, radius, 2)

    def add_into_map(self, cell):
        row, col = cell
        if not self.board[row][col]:
            self.board[row][col] = self.player
            self.change_player()

    def change_player(self):
        self.player = self.player_dict[self.player]

if __name__ == '__main__':
    running = True
    size = 500, 500
    screen = pygame.display.set_mode(size)
    board = Board(10, 7, 10, 10,  50)
    while running:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                running = False
            elif ev.type == pygame.MOUSEBUTTONDOWN:
                board.interface(ev.pos)
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()