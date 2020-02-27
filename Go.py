import pygame, time, random


# Set up game
pygame.init()
mainClock = pygame.time.Clock()

# Color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
MUSTARD = (255, 173, 1)

# Screen Setting
WINDOWWIDTH = 600
WINDOWHEIGHT = 600


def main():
    screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('9 x 9 Go Game')
    screen.fill(BLACK)

    # Draw Go board
    pygame.draw.rect(screen, MUSTARD, (50, 50, 500, 500))

    pygame.draw.line(screen, BLACK, (100, 100), (100, 500), 3)
    pygame.draw.line(screen, BLACK, (150, 100), (150, 500), 1)
    pygame.draw.line(screen, BLACK, (200, 100), (200, 500), 1)
    pygame.draw.line(screen, BLACK, (250, 100), (250, 500), 1)
    pygame.draw.line(screen, BLACK, (300, 100), (300, 500), 1)
    pygame.draw.line(screen, BLACK, (350, 100), (350, 500), 1)
    pygame.draw.line(screen, BLACK, (400, 100), (400, 500), 1)
    pygame.draw.line(screen, BLACK, (450, 100), (450, 500), 1)
    pygame.draw.line(screen, BLACK, (500, 100), (500, 500), 3)

    pygame.draw.line(screen, BLACK, (100, 100), (500, 100), 3)
    pygame.draw.line(screen, BLACK, (100, 150), (500, 150), 1)
    pygame.draw.line(screen, BLACK, (100, 200), (500, 200), 1)
    pygame.draw.line(screen, BLACK, (100, 250), (500, 250), 1)
    pygame.draw.line(screen, BLACK, (100, 300), (500, 300), 1)
    pygame.draw.line(screen, BLACK, (100, 350), (500, 350), 1)
    pygame.draw.line(screen, BLACK, (100, 400), (500, 400), 1)
    pygame.draw.line(screen, BLACK, (100, 450), (500, 450), 1)
    pygame.draw.line(screen, BLACK, (100, 500), (500, 500), 3)

    pygame.draw.circle(screen, BLACK, (200, 200), 5)
    pygame.draw.circle(screen, BLACK, (400, 400), 5)
    pygame.draw.circle(screen, BLACK, (300, 300), 5)
    pygame.draw.circle(screen, BLACK, (200, 400), 5)
    pygame.draw.circle(screen, BLACK, (400, 200), 5)

    pygame.display.update()

    # Main loop(it stops screen for now to check)
    count = 1
    play_game = True
    while play_game:

        if count == 40:
            play_game = False

        if count % 2 == 0:
            mainClock.tick(3)
            pygame.draw.circle(screen, BLACK, (random.randrange(100, 500, 50), random.randrange(100, 500, 50)), 25)
            count = count + 1

        else :
            mainClock.tick(3)
            pygame.draw.circle(screen, WHITE, (random.randrange(100, 500, 50), random.randrange(100, 500, 50)), 25)
            count = count + 1

        pygame.display.update()
        mainClock.tick(60)





#pygame.display.flip()
#mainClock.tick(200)

main()