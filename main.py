import pygame
import random
pygame.init()

display = pygame.display.set_mode((100, 10))

# game loop
running = True
timer = 0
while running:
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_UP:
                pygame.mixer.music.load("sounds/5.mp3")
                pygame.mixer.music.play()
    pygame.display.flip()
    # pygame tick
    pygame.time.delay(1000)
    timer += 1
    if timer == 340:
        timer = 0
        # random int between 1 and 5
        sound = random.randint(1, 5)
        pygame.mixer.music.load("sounds/"+str(sound)+".mp3")
        pygame.mixer.music.play()

pygame.quit()

