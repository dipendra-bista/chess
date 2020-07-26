import pygame

# initialize all the pygame modules
pygame.init()

# Set not to exit the window
done = False
# setting title of the window
pygame.display.set_caption("Chess Game")
# setting height and width of the window
screen = pygame.display.set_mode((400, 400))

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

    pygame.display.flip()
