import pygame

# initialize all the pygame modules
pygame.init()
# Set not to exit the window
done = False
# setting title of the window
pygame.display.set_caption("Chess Game")
# setting height and width of the window
screen = pygame.display.set_mode((400, 400))

x = 30
y = 30
is_blue = True

clock = pygame.time.Clock()
''' 
By default windows are not display forever so to make
it display untill user press close event
'''
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.type == pygame.K_SPACE:
            is_blue = not is_blue
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        y -= 3
    if pressed[pygame.K_DOWN]:
        y += 3
    if pressed[pygame.K_LEFT]:
        x -= 3
    if pressed[pygame.K_RIGHT]:
        x += 3
    if is_blue:
        color = [0, 128, 255]
    else:
        color = [255, 100, 0]
    # will block execution utill 1/60 have passed
    clock.tick(60)
    
    # clearing previous frames
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))
    pygame.display.flip()
