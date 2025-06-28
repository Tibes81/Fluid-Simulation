import pygame, sys, random

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_width, screen_height = screen.get_size()
pygame.display.set_caption("Fluid Simulation")
print (screen_height, screen_width)

#objects
#ball = pygame.Rect(screen_width/2, 100, 20, 20)
balls = []
box = pygame.Rect(0, 0, screen_width * 0.8, screen_height * 0.8 )
box.center = (screen_width/2, screen_height/2)

#colors
black = (10, 10, 10)
white = (230, 230, 230)
red = (230, 10, 10)

#variables
gravity = 0.12
#ball_speed_x = random.uniform(-5, 5) 
#ball_speed_y = random.uniform(-5, 5) 
dampening = 0.04

#functions
def collisions():
    global ball_speed_y, ball_speed_x
    if ball['rect'].bottom > box.bottom and ball['speed_y'] > 0:
        ball['rect'].bottom = box.bottom
        ball['speed_y'] *= -1 + dampening
    if ball['rect'].top < box.top and ball['speed_y'] < 0:
        ball['rect'].top = box.top
        ball['speed_y'] *= -1 - dampening
    if ball['rect'].left < box.left and ball['speed_x'] < 0:
        ball['rect'].left = box.left
        ball['speed_x'] *= -1 - dampening
    if ball['rect'].right > box.right and ball['speed_x'] > 0:
        ball['rect'].right = box.right
        ball['speed_x'] *= -1 + dampening



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
            if event.key == pygame.K_SPACE and simulation == True:
                simulation = False
            elif event.key == pygame.K_SPACE and simulation == False:
                simulation = True
            elif event.key == pygame.K_b:
                for i in range(1000):
                    ball_rect = pygame.Rect(screen_width/2, 100, 20, 20)
                    balls.append({
                        'rect': ball_rect,
                        'speed_x': random.uniform(-5, 5),
                        'speed_y': random.uniform(-5, 5)
                    })
            

    #simulation-loop-part
    if simulation:
        screen.fill(black)
        for ball in balls:
            ball['speed_y'] += gravity
            ball['rect'].x += ball['speed_x']
            ball['rect'].y += ball['speed_y']

            pygame.draw.ellipse(screen, red, ball['rect'])

            collisions()

        #draw things
        pygame.draw.rect(screen, white, box, width = 5)
    

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
