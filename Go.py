import pygame, random, sys


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


# round up user's click position
def myround(x, base=50):
    return base * round(x/base)


# check if there is other stones on same spot
def check_double(move, x_pos, y_pos):
    double = False

    for x in move:
        if x[0] == x_pos and x[1] == y_pos:
            double = True

    return double


# User's input for exit game or restart the game
def wait_for_player_to_press_key(screen):
    pressed = False
    while not pressed:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()


# Player movement input
def wait_for_player_to_play(screen, move):
    pressed = False
    while not pressed:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if e.type == pygame.MOUSEBUTTONUP:
                x_pos = pygame.mouse.get_pos()[0]
                y_pos = pygame.mouse.get_pos()[1]
                if not check_double(move,x_pos,y_pos):
                    pygame.draw.circle(screen, BLACK, (myround(x_pos), myround(y_pos)), 25)
                    move.append([myround(x_pos), myround(y_pos), 1])
                return


def user_play(screen):
    ev = pygame.event.get()

    for event in ev:
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            pygame.draw.circle(screen, BLACK, pos, 25)


# check if there is other stones on up,down,right,left
def check_next(move, x_pos, y_pos):
    next = False

    for x in move:
        if (x[0] - 50) == x_pos and (x[1]) == y_pos:
            next is True
        if (x[0] + 50) == x_pos and (x[1]) == y_pos:
            next is True
        if (x[0]) == x_pos and (x[1] - 50) == y_pos:
            next is True
        if (x[0]) == x_pos and (x[1] + 50) == y_pos:
            next is True

    return next


# Checking if there is other stones on diagonal position
def check_dia(move, x_pos, y_pos):
    dia = False

    for x in move:
        if (x[0] - 50) == x_pos and (x[1] + 50) == y_pos:
            next is True
        if (x[0] - 50) == x_pos and (x[1] - 50) == y_pos:
            next is True
        if (x[0] + 50) == x_pos and (x[1] - 50) == y_pos:
            next is True
        if (x[0] + 50) == x_pos and (x[1] + 50) == y_pos:
            next is True

    return dia


# Adding AI condition to play on fist few movement
def fist_few_move(screen, move):

    if not check_double(move, 200, 200):
        if not check_next(move, 200, 200):
            if not check_dia(move, 200, 200):
                pygame.draw.circle(screen, WHITE, (200, 200), 25)
                move.append([200, 200, 2])

    elif not check_double(move, 400, 400):
        if not check_next(move, 400, 400):
            if not check_dia(move, 400, 400):
                pygame.draw.circle(screen, WHITE, (400, 400), 25)
                move.append([400, 400, 2])

    elif not check_double(move, 200, 400):
        if not check_next(move, 200, 400):
            if not check_dia(move, 200, 400):
                pygame.draw.circle(screen, WHITE, (200, 400), 25)
                move.append([200, 400, 2])

    elif not check_double(move, 400, 200):
        if not check_next(move, 400, 200):
            if not check_dia(move, 400, 200):
                pygame.draw.circle(screen, WHITE, (400, 200), 25)
                move.append([400, 200, 2])


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
    move = []
    # move contain ( x-coordinate, y-coordinate, identification)
    play_game = True
    while play_game:

        if count == 70:
            play_game = False

        if count % 2 != 0:
            wait_for_player_to_play(screen, move, count)
            count += 1
            pygame.display.update()
            pygame.time.wait(900)

        if count % 2 == 0:

            if count < 5:
                fist_few_move(screen, move, count)
                count += 1
            else:
                ai_x_pos = random.randrange(100, 500, 50)
                ai_y_pos = random.randrange(100, 500, 50)

                if not check_double(move, ai_x_pos, ai_y_pos):
                    pygame.draw.circle(screen, WHITE, (ai_x_pos, ai_y_pos), 25)
                    move.append([ai_x_pos, ai_y_pos, 2])
                    count += 1

        pygame.display.update()
        mainClock.tick(60)

    pygame.display.update()
    wait_for_player_to_press_key(screen)


main()