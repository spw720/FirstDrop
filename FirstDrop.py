import pygame

pygame.init()

win = pygame.display.set_mode((500,800))

pygame.display.set_caption("First Drop")

x = 250
y = 10

width = 4
height = 7
vel = 3

R = 0
B = 255
G = 255

run = True

while run:
    pygame.time.delay(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel and y < 790:
        x -= vel
        y += 1

    if keys[pygame.K_RIGHT] and x < (500 - width) and y < 790:
        x += vel
        y += 1

    if keys[pygame.K_DOWN] and y < 490:
        y += 1

    if keys[pygame.K_LEFT and pygame.K_DOWN] and x > vel and y < 790:
        x -= vel
        y += vel

    if keys[pygame.K_RIGHT and pygame.K_DOWN] and x < (500 - width - vel) and y < 790:
        x += vel
        y += vel

    if keys[pygame.K_UP] and y < 490:
        y -= 2

    # win.fill((255,255,255))

    if y < 790:
        y += 2 # continuously move down screen


    pygame.draw.rect(win, (R,B,G), (x,y,width,height))

    pygame.display.update()


pygame.quit()
