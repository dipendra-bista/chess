import pygame


def resize_screen(square_side_len):
    global SQUARE_SIDE
    global screen
    screen = pygame.display.set_mode((8 * square_side_len, 8 * square_side_len), pygame.RESIZABLE)
    SQUARE_SIDE = square_side_len


white_color = [192, 192, 192]
black_color = [128, 128, 128]


# print 8*8 chess board with the given color
def print_board(white_color, black_color):
    for row in range(0, 8):
        for column in range(0, 8):
            if row % 2 == 0:
                if column % 2 == 0:
                    color = white_color
                else:
                    color = black_color

            else:
                if column % 2 == 0:
                    color = black_color
                else:
                    color = white_color
            pygame.draw.rect(screen, color,
                             pygame.Rect(row * SQUARE_SIDE, column * SQUARE_SIDE, SQUARE_SIDE, SQUARE_SIDE))


def setInitialPiecePosition():
    for row in range(0, 8):
        for col in range(0, 8):
            if row == 0:
                screen.blit(pygame.transform.scale(WHITE_ROOK, (SQUARE_SIDE, SQUARE_SIDE)), (0, 0))
                screen.blit(pygame.transform.scale(WHITE_KNIGHT, (SQUARE_SIDE, SQUARE_SIDE)), (SQUARE_SIDE, 0))
                screen.blit(pygame.transform.scale(WHITE_BISHOP, (SQUARE_SIDE, SQUARE_SIDE)), (2 * SQUARE_SIDE, 0))
                screen.blit(pygame.transform.scale(WHITE_KING, (SQUARE_SIDE, SQUARE_SIDE)), (3 * SQUARE_SIDE, 0))
                screen.blit(pygame.transform.scale(WHITE_QUEEN, (SQUARE_SIDE, SQUARE_SIDE)), (4 * SQUARE_SIDE, 0))
                screen.blit(pygame.transform.scale(WHITE_BISHOP, (SQUARE_SIDE, SQUARE_SIDE)), (5 * SQUARE_SIDE, 0))
                screen.blit(pygame.transform.scale(WHITE_KNIGHT, (SQUARE_SIDE, SQUARE_SIDE)), (6 * SQUARE_SIDE, 0))
                screen.blit(pygame.transform.scale(WHITE_ROOK, (SQUARE_SIDE, SQUARE_SIDE)), (7 * SQUARE_SIDE, 0))
            elif row == 1:
                screen.blit(pygame.transform.scale(WHITE_PAWN, (SQUARE_SIDE, SQUARE_SIDE)),
                            (col * SQUARE_SIDE, SQUARE_SIDE))
                screen.blit(pygame.transform.scale(WHITE_PAWN, (SQUARE_SIDE, SQUARE_SIDE)),
                            (col * SQUARE_SIDE, SQUARE_SIDE))
                screen.blit(pygame.transform.scale(WHITE_PAWN, (SQUARE_SIDE, SQUARE_SIDE)),
                            (col * SQUARE_SIDE, SQUARE_SIDE))
                screen.blit(pygame.transform.scale(WHITE_PAWN, (SQUARE_SIDE, SQUARE_SIDE)),
                            (col * SQUARE_SIDE, SQUARE_SIDE))
                screen.blit(pygame.transform.scale(WHITE_PAWN, (SQUARE_SIDE, SQUARE_SIDE)),
                            (col * SQUARE_SIDE, SQUARE_SIDE))
                screen.blit(pygame.transform.scale(WHITE_PAWN, (SQUARE_SIDE, SQUARE_SIDE)),
                            (col * SQUARE_SIDE, SQUARE_SIDE))
                screen.blit(pygame.transform.scale(WHITE_PAWN, (SQUARE_SIDE, SQUARE_SIDE)),
                            (col * SQUARE_SIDE, SQUARE_SIDE))
                screen.blit(pygame.transform.scale(WHITE_PAWN, (SQUARE_SIDE, SQUARE_SIDE)),
                            (col * SQUARE_SIDE, SQUARE_SIDE))
            elif row == 6:
                screen.blit(pygame.transform.scale(BLACK_PAWN, (SQUARE_SIDE, SQUARE_SIDE)),
                            (col, row * SQUARE_SIDE))
                screen.blit(pygame.transform.scale(BLACK_PAWN, (SQUARE_SIDE, SQUARE_SIDE)),
                            (SQUARE_SIDE, row * SQUARE_SIDE))
                screen.blit(pygame.transform.scale(BLACK_PAWN, (SQUARE_SIDE, SQUARE_SIDE)),
                            (col * SQUARE_SIDE, row * SQUARE_SIDE))
                screen.blit(pygame.transform.scale(BLACK_PAWN, (SQUARE_SIDE, SQUARE_SIDE)),
                            (col * SQUARE_SIDE, row * SQUARE_SIDE))
                screen.blit(pygame.transform.scale(BLACK_PAWN, (SQUARE_SIDE, SQUARE_SIDE)),
                            (col * SQUARE_SIDE, row * SQUARE_SIDE))
                screen.blit(pygame.transform.scale(BLACK_PAWN, (SQUARE_SIDE, SQUARE_SIDE)),
                            (col * SQUARE_SIDE, row * SQUARE_SIDE))
                screen.blit(pygame.transform.scale(BLACK_PAWN, (SQUARE_SIDE, SQUARE_SIDE)),
                            (col * SQUARE_SIDE, row * SQUARE_SIDE))
                screen.blit(pygame.transform.scale(BLACK_PAWN, (SQUARE_SIDE, SQUARE_SIDE)),
                            (col * SQUARE_SIDE, row * SQUARE_SIDE))
            elif row == 7:
                screen.blit(pygame.transform.scale(BLACK_ROOK, (SQUARE_SIDE, SQUARE_SIDE)), (0, 7 * SQUARE_SIDE))
                screen.blit(pygame.transform.scale(BLACK_KNIGHT, (SQUARE_SIDE, SQUARE_SIDE)),
                            (SQUARE_SIDE, 7 * SQUARE_SIDE))
                screen.blit(pygame.transform.scale(BLACK_BISHOP, (SQUARE_SIDE, SQUARE_SIDE)),
                            (2 * SQUARE_SIDE, 7 * SQUARE_SIDE))
                screen.blit(pygame.transform.scale(BLACK_KING, (SQUARE_SIDE, SQUARE_SIDE)),
                            (3 * SQUARE_SIDE, 7 * SQUARE_SIDE))
                screen.blit(pygame.transform.scale(BLACK_QUEEN, (SQUARE_SIDE, SQUARE_SIDE)),
                            (4 * SQUARE_SIDE, 7 * SQUARE_SIDE))
                screen.blit(pygame.transform.scale(BLACK_BISHOP, (SQUARE_SIDE, SQUARE_SIDE)),
                            (5 * SQUARE_SIDE, 7 * SQUARE_SIDE))
                screen.blit(pygame.transform.scale(BLACK_KNIGHT, (SQUARE_SIDE, SQUARE_SIDE)),
                            (6 * SQUARE_SIDE, 7 * SQUARE_SIDE))
                screen.blit(pygame.transform.scale(BLACK_ROOK, (SQUARE_SIDE, SQUARE_SIDE)),
                            (7 * SQUARE_SIDE, 7 * SQUARE_SIDE))


# each square size of the board
SQUARE_SIDE = 50

pygame.init()
# setting up title
pygame.display.set_caption("Chess Game")
# setting up icon
pygame.display.set_icon(pygame.image.load('images/chess_icon.ico'))
# setting width and height of window and making it resizable
screen = pygame.display.set_mode((SQUARE_SIDE * 8, SQUARE_SIDE * 8), pygame.RESIZABLE)

'''
preparing images...
'''
# loading black piece images
BLACK_KING = pygame.image.load('images/black_king.png')
BLACK_QUEEN = pygame.image.load('images/black_queen.png')
BLACK_ROOK = pygame.image.load('images/black_rook.png')
BLACK_BISHOP = pygame.image.load('images/black_bishop.png')
BLACK_KNIGHT = pygame.image.load('images/black_knight.png')
BLACK_PAWN = pygame.image.load('images/black_pawn.png')
BLACK_JOKER = pygame.image.load('images/black_joker.png')

# loading white piece images
WHITE_KING = pygame.image.load('images/white_king.png')
WHITE_QUEEN = pygame.image.load('images/white_queen.png')
WHITE_ROOK = pygame.image.load('images/white_rook.png')
WHITE_BISHOP = pygame.image.load('images/white_bishop.png')
WHITE_KNIGHT = pygame.image.load('images/white_knight.png')
WHITE_PAWN = pygame.image.load('images/white_pawn.png')
WHITE_JOKER = pygame.image.load('images/white_joker.png')

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.VIDEORESIZE:
            if screen.get_height() != event.h:
                resize_screen(int(event.h / 8.0))
            else:
                resize_screen(int(event.w / 8.0))
    # clear default black background and make screen fill with white background
    screen.fill((255, 255, 255))

    print_board(white_color, black_color)
    setInitialPiecePosition()
    pygame.display.update()
    pygame.display.flip()
