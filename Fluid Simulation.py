import pygame, sys

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Fluid Simulation")
screen_width, screen_height = screen.get_size()

#objects
ball = pygame.Rect(0, 0, 50, 50)

#colors
black = (10, 10, 10)
red = (230, 10, 10)

#gameloop
simulation = True
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                simulation = False

    #simulation-loop-part
    if simulation:
        screen.fill(black)

        #draw things
        pygame.draw.ellipse(screen, red, ball)
    

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
