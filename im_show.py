import pygame
def show():
    pygame.init()

    display_width = 640
    display_height = 480

    gameDisplay = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('Plot')

    black = (0, 0, 0)
    white = (255, 255, 255)

    clock = pygame.time.Clock()
    crashed = False
    plotImg = pygame.image.load('plot.png')

    def car(x, y):
        gameDisplay.blit(plotImg, (x, y))

    x = 0
    y = 0

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

        gameDisplay.fill(white)
        car(x, y)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

