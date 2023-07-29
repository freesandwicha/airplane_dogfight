import pygame
from pygame import *
import time


def main():
#1 Creat a window to display the game
    screen = pygame.display.set_mode((480,852), 0, 32)
#2 Get a picture to be the background
    background = pygame.image.load('asset/background.png')
#4 Get a picture to be the player
    player = pygame.image.load('asset/hero1.png')
    x = 480 / 2 - 100 / 2
    y = 600
    speed = 5



# display the content
    while True:
        # 3 Combine the screen and background
        screen.blit(background, (0, 0))
        # 5 Combine the plane and background
        screen.blit(player, (x, y))

        for event in pygame.event.get():
            # Give feedbacks to every event;
            # Its a list to get events cause there are a lot of events will happen at the same time.
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # Listen the keyboard: if a user keep pressing keyboard, the program can process this.
        key_pressed = pygame.key.get_pressed()

        if key_pressed[K_w] or key_pressed[K_UP]:
            y -= speed
            print("wwwww")
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            x -= speed
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            y += speed
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            x += speed
        if key_pressed[K_SPACE]:
            print("space")

        pygame.display.update()
        time.sleep(0.01)


if __name__ == '__main__':
    main()


