import pygame

pygame.init()

win = pygame.display.set_mode((500,700))

pygame.display.set_caption("First Drop")

bg = pygame.image.load('BG.png')
char = pygame.image.load('STANDING:STOP.png')
downchar = pygame.image.load('MOVE:DOWN.png')
SWchar = pygame.image.load('MOVE:SOUTHWEST.png')
SEchar = pygame.image.load('MOVE:SOUTHEAST.png')

jump = pygame.image.load('Jump1-25x25.png')
tree = pygame.image.load('TREE1-15x25.png')

clock = pygame.time.Clock()

x = 250
y = 10

vel = 0

SW = False
SE = False
Down = False
Up = False

x_list = [250]
y_list = [10]

def redraw_window():
    win.blit(bg, (0,0))

    win.blit(jump, (250,350))
    win.blit(tree, (150, 250))
    win.blit(tree, (350, 450))

    if SW:
        win.blit(SWchar, (x, y))
    elif SE:
        win.blit(SEchar, (x, y))
    elif Down:
        win.blit(downchar, (x, y))
    elif Up:
        win.blit(char, (x,y))
    else:
        win.blit(char, (x,y))

    x_list.append(x+3)
    y_list.append(y+3)

    for i in range(len(x_list)):

        if i != 0 and i != len(x_list)-1:
            pygame.draw.line(win, (0, 0, 0), (x_list[i], y_list[i]), (x_list[i-1], y_list[i-1]), 1)
            pygame.draw.line(win, (0, 0, 0), (x_list[i]+3, y_list[i]), (x_list[i-1]+3, y_list[i-1]), 1)

    pygame.display.update()


run = True


while run:

    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    SW = False
    SE = False
    Down = True
    Up = False

    if keys[pygame.K_LEFT] and x > vel and y < 690:

        SW = True
        SE = False
        Down = False
        Up = False

        vel = 3

        x -= vel
        y += 1

    if keys[pygame.K_RIGHT] and x < (500 - 10) and y < 690:

        SW = False
        SE = True
        Down = False
        Up = False

        vel = 3

        x += vel
        y += 1

    if keys[pygame.K_DOWN] and y < 690:

        SW = False
        SE = False
        Down = True
        Up = False

        vel = 3

        y += 1

    if keys[pygame.K_LEFT and pygame.K_DOWN] and x > vel and y < 690:

        SW = False
        SE = False
        Down = True
        Up = False

        vel = 3

        x -= 4
        y += 1

    if keys[pygame.K_RIGHT and pygame.K_DOWN] and x < (500 - 10 - vel) and y < 690:

        SW = False
        SE = False
        Down = True
        Up = False

        vel = 3

        x += 4
        y += 1

    if keys[pygame.K_RIGHT and pygame.K_UP] and x < (500 - 10 - vel) and y < 690:

        SW = False
        SE = False
        Down = False
        Up = False

        vel = 3

        y -= 1
        x += 4

    if keys[pygame.K_RIGHT and pygame.K_UP] and x < (500 - 10 - vel) and y < 690:

        SW = False
        SE = False
        Down = False
        Up = False

        vel = 3

        x -= 4
        y -= 1


    if keys[pygame.K_UP] and y < 690:

        SW = False
        SE = False
        Down = False
        Up = True

        vel = 3

        y -= 1

    if y < 690:
        y += vel # continuously move down screen

    if y >= 690: # restart player at top of screen
        y = 10
        x = 250

    redraw_window()


pygame.quit()
