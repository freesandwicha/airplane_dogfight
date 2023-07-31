# -*- coding = utf-8 -*-
# Worker : HAN XIA
# Motto : Practice makes perfect.
# Time : 31/7/2023 8:54 pm

# -*- coding = utf-8 -*-
# Worker : HAN XIA
# Motto : Practice makes perfect.
# Time : 29/7/2023 3:10 pm
import random
import pygame
from pygame import *
import time


class HeroPlane(pygame.sprite.Sprite):
    def __init__(self,screen):
        #Call the initial method of Sprite.
        pygame.sprite.Sprite.__init__(self)
        self.player = pygame.image.load('asset/hero1.png') #100 * 124
        #Get the object of rectangle based on image cause every collision is about rectangles.
        self.rect = self.image.get_rect()
        #Get the position of rectangle.
        self.rect.topleft = [480 / 2 - 100 / 2, 600]
        self.speed = 5
        #Show it into the screen
        self.screen = screen
        #This method returns a list.
        self.bullets = pygame.sprite.Group()

    def key_control(self):
        # Listen the keyboard: if a user keep pressing keyboard, the program can process this.
        key_pressed = pygame.key.get_pressed()

        if key_pressed[K_w] or key_pressed[K_UP]:
            self.rect.top -= self.speed
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            self.rect.left -= self.speed
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            self.rect.bottom += self.speed
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            self.rect.right += self.speed
        if key_pressed[K_SPACE]:
            bullet = Bullet(self.screen, self.rect.left, self.rect.top)
            #Here, using the parameters to define the position of every bullet, which related with the hero plane.
            #Common processing method is to use a list to store each bullet object, as there can be numerous bullets.
            # Add method from Group() to instead of append.
            self.bullets.add(bullet)

    def update(self):
        self.key_control()
        self.display()


    def display(self):
        # 5 Combine the plane and background
        self.screen.blit(self.player, (self.rect.left, self.rect.top))
        #The update method from group() will update the position of every bullet in the list.
        self.bullets.update()
        # Every bullet need to be displayed on the screen.
        # It like iterates every bullet.
        self.bullets.draw(self.screen)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        self.x = x + 100/2 - 22/2
        self.y = y - 22
        self.image = pygame.image.load('asset/bullet.png') #22 * 22
        self.screen = screen
        self.speed = 10

    def display(self):
        #5. Combine the bullet and background
        self.screen.blit(self.image, (self.x, self.y))

    def auto_move(self):
        self.y -= self.speed


class EnemyPlane(pygame.sprite.Sprite):
    def __init__(self,screen):
        self.player = pygame.image.load('asset/enemy0.png') #51*39
        self.x = 0
        self.y = 0
        self.speed = 5
        #Show them into the screen
        self.screen = screen
        self.bullets = []
        self.direction = 'right'

    def display(self):
        # # 5 Combine the plane and background
        self.screen.blit(self.player, (self.x, self.y))
        #Every bullet need to be displayed on the screen.
        for bullet in self.bullets:
            bullet.auto_move()
            bullet.display()


    def auto_move(self):
        if self.direction == 'right':
            self.x += self.speed
        elif self.direction == 'left':
            self.x -= self.speed

        if self.x > 480 - 51:
            self.direction = 'left'
        elif self.x < 0:
            self.direction = 'right'

    def auto_fire(self):

        random_num = random.randint(1,20 )
        if random_num == 8:
            bullet = EnemyBullets(self.screen, self.x, self.y)
            self.bullets.append(bullet)



#The enemy bullets:
class EnemyBullets(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        self.x = x + 50/2 - 10/2
        #Its better to define the position with integer.
        self.y = y + 39
        self.image = pygame.image.load('asset/bullet1.png') # 9 * 21
        self.screen = screen
        self.speed = 10

    def display(self):
        #5. Combine the bullet and background
        self.screen.blit(self.image, (self.x, self.y))

    def auto_move(self):
        self.y += self.speed


class GameSound():
    def __init__(self):
        #initialize the music module
        pygame.mixer.init()
        pygame.mixer.music.load('asset/bg2.ogg')
        #Set the volume level
        pygame.mixer.music.set_volume(0.5)

    def playBackgroundMusic(self):
        #Indefinite loop.
        pygame.mixer.music.play(-1)


def main():
    # 1 Creat a window to display the game
    screen = pygame.display.set_mode((480, 852), 0, 32)
    # 2 Get a picture to be the background
    background = pygame.image.load('asset/background.png') #480 * 852
    # Creat the plane of player
    player = HeroPlane(screen)
    # Creat the planes of enemy.
    enemy = EnemyPlane(screen)
    # Manage the background music
    sound = GameSound()
    sound.playBackgroundMusic()

    # Display the content
    while True:
        # 3 Combine the screen and background
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            # Give feedbacks to every event;
            # Its a list to get events cause there are a lot of events will happen at the same time.
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        #  Listen the keyboard
        player.key_control()
        # Display the plane
        player.display()
        # Display the enemy
        enemy.display()
        enemy.auto_move()
        enemy.auto_fire()

        pygame.display.update()
        time.sleep(0.01)


if __name__ == '__main__':
    main()
