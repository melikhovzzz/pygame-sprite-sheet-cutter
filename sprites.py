import pygame

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Spritesheets')

sprite_sheet_image = pygame.image.load('PATH_TO_YOUR_SPRITESHEET_IMAGE').convert_alpha()

BG = (50, 50, 50)
BLACK = (0, 0, 0)

def get_image(sheet, width, height, scale, colour):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet, (0, 0), (0, 0, width, height))
    image = pygame.transform.scale(image, (width * scale, height * scale))
    image.set_colorkey(colour)
    return image

frame_0 = get_image(sprite_sheet_image, 22, 32, 4, BLACK)

run = True
while run:

    #update background
    screen.fill(BG)

    #show frame image
    screen.blit(frame_0, (0, 0))

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
