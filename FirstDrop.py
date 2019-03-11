import pygame
import random

pygame.init()

win = pygame.display.set_mode((500, 700))

pygame.display.set_caption("First Drop")

bg = pygame.image.load('BG.png')
TITLE = pygame.image.load('TITLE.png')
char = pygame.image.load('STANDING:STOP.png')#('STANDING:STOP.png')
downchar = pygame.image.load('MOVE:DOWN.png')
SWchar = pygame.image.load('MOVE:SOUTHWEST.png')
SEchar = pygame.image.load('MOVE:SOUTHEAST.png')
FASTSW = pygame.image.load('FASTSW.png')
FASTSE = pygame.image.load('FASTSE.png')

jump = pygame.image.load('Jump1-25x25.png')
tree = pygame.image.load('TREE1-15x25.png')

dead = pygame.image.load('DEAD.png')

clock = pygame.time.Clock()


class Skier(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.score = 0

        self.vel = 0
        self.SW = False
        self.SE = False
        self.FSW = False
        self.FSE = False
        self.Down = True
        self.Up = False
        self.x_list = [254]
        self.y_list = [14]
        self.hitbox = (self.x, self.y, 10, 10)


class Jump(object):

    jump = pygame.image.load('Jump1-25x25.png')

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hitbox = (self.x, self.y, 25, 25)

    def draw(self, win):
        win.blit(self.jump, (self.x, self.y))
        self.hitbox = (self.x, self.y, 25, 25)


class Tree(object):

    tree = pygame.image.load('TREE1-15x25.png')

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hitbox = (self.x, self.y, 15, 25)

    def draw(self, win):
        win.blit(self.tree, (self.x, self.y))
        self.hitbox = (self.x, self.y, 15, 25)


class Jerry(object):

    J_Left = pygame.image.load('JERRY_LEFT.png')
    J_Right = pygame.image.load('JERRY_RIGHT.png')

    def __init__(self, x, y, vel, end):
        self.x = x
        self.y = y
        self.strtx = x
        self.strty = y
        self.end = end
        self.hitbox = (self.x, self.y, 10, 10)
        if self.x > self.end:
            self.path = [self.end, self.x]
        else:
            self.path = [self.x, self.end]
        self.vel = vel

    def draw(self, win):
        self.move()
        if self.vel > 0:
            win.blit(self.J_Right, (self.x, self.y))
        else:
            win.blit(self.J_Left, (self.x, self.y))
        self.hitbox = (self.x, self.y, 10, 10)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
        self.y += 1
        if self.y >= 690:
            self.x = self.strtx
            self.y = self.strty

    def hit(self):
        pass


class Map(object):

    def __init__(self, num_trees, num_jumps):
        self.num_trees = num_trees
        self.num_jumps = num_jumps
        self.jmp_x = []
        self.jmp_y = []
        self.tree_x = []
        self.tree_y = []

    def randomMap(self):

        self.jmp_x = []
        self.jmp_y = []
        self.tree_x = []
        self.tree_y = []
        self.tree_list = []

        for x in range(self.num_trees):
            self.tree_x.append(random.randint(20, 480))
            self.tree_y.append(random.randint(100, 680))

        for x in range(self.num_jumps):
            self.jmp_x.append(random.randint(20, 480))
            self.jmp_y.append(random.randint(100, 680))


skiman = Skier(250, 10)

jerryman = Jerry(490, 110, 3, 300)
jerryman2 = Jerry(50, 150, 3, 490)

jerryman3 = Jerry(40, 290, 1, 10)
jerryman4 = Jerry(100, 210, 1, 400)

jerryman5 = Jerry(390, 125, 2, 20)
jerryman6 = Jerry(100, 140, 2, 490)

jerryman7 = Jerry(460, 100, 4, 200)
jerryman8 = Jerry(10, 111, 4, 490)

jerryman9 = Jerry(210, 75, 1, 250)

jerrylist = [jerryman, jerryman2, jerryman3, jerryman4, jerryman5, jerryman6,
             jerryman7, jerryman8, jerryman9]

new_map = Map(30, 10) # number of trees, jumps

new_map.randomMap()

#tree_list = []
jump_list = []

for i in range(new_map.num_trees):
    new_map.tree_list.append(Tree(new_map.tree_x[i], new_map.tree_y[i]))

for i in range(new_map.num_jumps):
    jump_list.append(Jump(new_map.jmp_x[i], new_map.jmp_y[i]))



def text_objects(text, font):
    textSurface = font.render(text, True, (100, 10, 10))
    return textSurface, textSurface.get_rect()


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(win, ac, (x, y, w, h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(win, ic, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    win.blit(textSurf, textRect)


def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        win.blit(TITLE, (0, 0))
        largeText = pygame.font.Font('freesansbold.ttf', 55)
        TextSurf, TextRect = text_objects(" First_Drop", largeText)
        TextRect.center = ((500 / 2), (700 / 2))
        win.blit(TextSurf, TextRect)

        largeText2 = pygame.font.Font('freesansbold.ttf', 25)
        TextSurf2, TextRect2 = text_objects("CONTROLS:", largeText2)
        TextRect2.center = (((500/2)/2), (600))
        win.blit(TextSurf2, TextRect2)

        TextSurf3, TextRect3 = text_objects("Arrow keys to ski", largeText2)
        TextRect3.center = (((500/2)/2), (630))
        win.blit(TextSurf3, TextRect3)

        TextSurf4, TextRect4 = text_objects("'P' to pause game", largeText2)
        TextRect4.center = (((500/2)/2), (660))
        win.blit(TextSurf4, TextRect4)

        largeText3 = pygame.font.Font('freesansbold.ttf', 15)
        TextSurf5, TextRect5 = text_objects("RULES:", largeText2)
        TextRect5.center = ((((500 / 2) / 2)*3), (600))
        win.blit(TextSurf5, TextRect5)

        TextSurf6, TextRect6 = text_objects("Hit a Jerry (-50 points)", largeText3)
        TextRect6.center = ((((500 / 2) / 2)*3), (620))
        win.blit(TextSurf6, TextRect6)

        TextSurf7, TextRect7 = text_objects("Hit a Tree (Reset score!)", largeText3)
        TextRect7.center = ((((500 / 2) / 2)*3), (635))
        win.blit(TextSurf7, TextRect7)

        TextSurf8, TextRect8 = text_objects("Hit a Jump (+50 points)", largeText3)
        TextRect8.center = ((((500 / 2) / 2)*3), (650))
        win.blit(TextSurf8, TextRect8)

        TextSurf9, TextRect9 = text_objects("Reach the bottom (+100 points)", largeText3)
        TextRect9.center = ((((500 / 2) / 2)*3), (665))
        win.blit(TextSurf9, TextRect9)

        button("SHRED!", 200, 450, 100, 25, (100, 100, 100), (253, 192, 47), gameloop)#(200, 200, 200), gameloop)
        button("Quit", 200, 500, 100, 25, (100, 100, 100), (253, 192, 47), quit)

        pygame.display.update()
        clock.tick(15)


def redraw_window(self):
    win.blit(bg, (0, 0))

    jerryman.draw(win)
    jerryman2.draw(win)
    jerryman3.draw(win)
    jerryman4.draw(win)
    jerryman5.draw(win)
    jerryman6.draw(win)
    jerryman7.draw(win)
    jerryman8.draw(win)
    jerryman9.draw(win)

    for i in range(len(jump_list)):
        jump_list[i].draw(win)

    for i in range(len(new_map.tree_list)):
        new_map.tree_list[i].draw(win)

    for i in range(len(new_map.tree_x)):
        win.blit(tree, (new_map.tree_x[i], new_map.tree_y[i]))

    if skiman.SW:
        win.blit(SWchar, (skiman.x, skiman.y))

    elif skiman.SE:
        win.blit(SEchar, (skiman.x, skiman.y))

    elif skiman.Down:
        win.blit(downchar, (skiman.x, skiman.y))

    elif skiman.FSE:
        win.blit(FASTSE, (skiman.x, skiman.y))

    elif skiman.FSW:
        win.blit(FASTSW, (skiman.x, skiman.y))

    elif skiman.Up:
        win.blit(char, (skiman.x, skiman.y))

    else:
        win.blit(char, (skiman.x, skiman.y))

    skiman.x_list.append(skiman.x+3)
    skiman.y_list.append(skiman.y+3)

    self.hitbox = (self.x, self.y, 10, 10)
    #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    for i in range(len(skiman.x_list)):

        if i != 0:

            pygame.draw.line(win, (0, 0, 0), (skiman.x_list[i], skiman.y_list[i]),
                                             (skiman.x_list[i - 1], skiman.y_list[i - 1]), 1)
            pygame.draw.line(win, (0, 0, 0), (skiman.x_list[i] + 3, skiman.y_list[i]),
                                             (skiman.x_list[i - 1] + 3, skiman.y_list[i - 1]), 1)


    #pygame.draw.rect(win, (0,0,0), (350,10,130,80), 3)
    largeText2 = pygame.font.Font('freesansbold.ttf', 25)
    TextSurf2, TextRect2 = text_objects("POINTS:", largeText2)
    TextRect2.center = ((410), (20))
    win.blit(TextSurf2, TextRect2)


    TextSurf3, TextRect3 = text_objects(str(skiman.score), largeText2)
    TextRect3.center = ((430), (50))
    win.blit(TextSurf3, TextRect3)

    pygame.display.update()


def gameloop():

    run = True

    while run:

        clock.tick(27)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for i in jerrylist:
            if skiman.y+5 < i.hitbox[1] + i.hitbox[3] and skiman.y+5 > i.hitbox[1]:
                if skiman.x+5 > i.hitbox[0] and skiman.x+5 < i.hitbox[0] + i.hitbox[2]:
                    skiman.x = 250
                    skiman.y = 10
                    skiman.x_list = []
                    skiman.y_list = []
                    skiman.score -= 50
                    jerryman.hit()

                    # new_map.randomMap()

        for i in jump_list:
            if skiman.y+5 < i.hitbox[1] + i.hitbox[3] and skiman.y+5 > i.hitbox[1]:
                if skiman.x+5 > i.hitbox[0] and skiman.x+5 < i.hitbox[0] + i.hitbox[2]:
                    skiman.y += 15
                    skiman.score += 50


        for i in new_map.tree_list:
            if skiman.y+5 < i.hitbox[1] + i.hitbox[3] and skiman.y+5 > i.hitbox[1]:
                if skiman.x+5 > i.hitbox[0] and skiman.x+5 < i.hitbox[0] + i.hitbox[2]:
                    skiman.x = 250
                    skiman.y = 10
                    skiman.x_list = []
                    skiman.y_list = []
                    new_map.num_trees = 30
                    skiman.score = 0
                    # new_map.randomMap()



        keys = pygame.key.get_pressed()

        if skiman.x == 250 and skiman.y == 10:
            skiman.SW = False
            skiman.SE = False
            skiman.FSW = False
            skiman.FSE = False
            skiman.Down = False
            skiman.Up = True
            skiman.vel = 0

        else:
            skiman.SW = False
            skiman.SE = False
            skiman.FSW = False
            skiman.FSE = False
            skiman.Down = True
            skiman.Up = False

        if keys[pygame.K_p]:
            game_intro()

        if keys[pygame.K_LEFT] and skiman.x > skiman.vel and skiman.y < 690:
            skiman.SW = True
            skiman.SE = False
            skiman.FSW = False
            skiman.FSE = False
            skiman.Down = False
            skiman.Up = False
            skiman.vel = 3
            skiman.x -= skiman.vel
            skiman.y += 1

        if keys[pygame.K_RIGHT] and skiman.x < (500 - 10) and skiman.y < 690:
            skiman.SW = False
            skiman.SE = True
            skiman.FSW = False
            skiman.FSE = False
            skiman.Down = False
            skiman.Up = False
            skiman.vel = 3
            skiman.x += skiman.vel
            skiman.y += 1

        if keys[pygame.K_RIGHT and pygame.K_DOWN] and skiman.x < (490 - skiman.vel) and skiman.y < 690:
            skiman.SW = False
            skiman.SE = False
            skiman.FSW = False
            skiman.FSE = True
            skiman.Down = False
            skiman.Up = False
            skiman.vel = 3
            skiman.x += 4
            skiman.y += 1

        if keys[pygame.K_LEFT and pygame.K_DOWN] and skiman.x > skiman.vel and skiman.y < 690:
            skiman.SW = False
            skiman.SE = False
            skiman.FSW = True
            skiman.FSE = False
            skiman.Down = False
            skiman.Up = False
            skiman.vel = 3
            skiman.x -= 4
            skiman.y += 1

        if keys[pygame.K_RIGHT and pygame.K_UP] and skiman.x < (490 - skiman.vel) and skiman.y < 690:
            skiman.SW = False
            skiman.SE = False
            skiman.FSW = False
            skiman.FSE = False
            skiman.Down = False
            skiman.Up = False
            skiman.vel = 3
            skiman.y -= 1
            skiman.x += 4

        if keys[pygame.K_LEFT and pygame.K_UP] and skiman.x < (490 - skiman.vel) and skiman.y < 690:
            skiman.SW = False
            skiman.SE = False
            skiman.FSW = False
            skiman.FSE = False
            skiman.Down = False
            skiman.Up = False
            skiman.vel = 3
            skiman.x -= 4
            skiman.y -= 1

        if keys[pygame.K_DOWN] and skiman.y < 690:
            skiman.SW = False
            skiman.SE = False
            skiman.FSW = False
            skiman.FSE = False
            skiman.Down = True
            skiman.Up = False
            skiman.vel = 3
            skiman.y += 1

        if keys[pygame.K_UP] and skiman.y < 690:
            skiman.SW = False
            skiman.SE = False
            skiman.FSW = False
            skiman.FSE = False
            skiman.Down = False
            skiman.Up = True
            skiman.vel = 3
            skiman.y -= 1

        if skiman.y < 690:
            skiman.y += skiman.vel  # continuously move down screen

        if skiman.y >= 690:  # restart player at top of screen

            skiman.score += 100
            #new_map.num_trees += 5

            skiman.vel += 100

            skiman.x = 250
            skiman.y = 10
            skiman.x_list = [254]
            skiman.y_list = [14]

            new_map.randomMap()
            for i in range(new_map.num_trees):
                new_map.tree_list.append(Tree(new_map.tree_x[i], new_map.tree_y[i]))
            #for i in range(5):
            #    tree_list.append(Tree(random.randint(20, 480), random.randint(20, 480)))


        redraw_window(skiman)


game_intro()
gameloop()
pygame.quit()
