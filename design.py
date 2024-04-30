import pygame

pygame.init()


class Square(pygame.sprite.Sprite):
    def __init__(self, x_id, y_id, number):
        super().__init__()
        self.width = 120
        self.height = 120
        self.x = x_id * self.width
        self.y = y_id * self.height
        self.content = " "
        self.number = number
        self.image = blank_image
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = (self.x, self.y)


def Update():
    win.blit(bg, (0, 0))
    square_group.draw(win)
    square_group.update()
    pygame.display.update()


WIDTH = 500
HEIGHT = 500

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
clock = pygame.time.Clock()

blank_image = pygame.image.load('Blank.png')
X_image = pygame.image.load('x.png')
O_image = pygame.image.load('o.png')
bg = pygame.image.load('background.png')

bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

square_group = pygame.sprite.Group()
squares = []

num = 1
for y in range(1, 4):
    for x in range(1, 4):
        sq = Square(x, y, num)
        square_group.add(sq)
        squares.append(sq)

        num += 1

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    Update()