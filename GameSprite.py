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
    # Hold all bullets from plane in a group:
    bullets = pygame.sprite.Group()
    def __init__(self,screen):
        #Call the initial method of Sprite.
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('asset/hero1.png') #100 * 124

        #Get the object of rectangle based on image cause every collision is about rectangles.
        self.rect = self.image.get_rect()
        #Get the position of rectangle.
        self.rect.topleft = [Manage.bg_size[0] / 2 - 100 / 2, 600]

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
            # Hold all bullets from the player in the group
            HeroPlane.bullets.add(bullet)

    def update(self):
        self.key_control()
        self.display()

    def display(self):
        # 5 Combine the plane and background
        self.screen.blit(self.image, (self.rect.left, self.rect.top))
        #The update method from group() will update the position of every bullet in the list.
        self.bullets.update()
        # Every bullet need to be displayed on the screen.
        # It like iterates every bullet.
        self.bullets.draw(self.screen)

    @classmethod
    def clear_bullets(cls):
        # clear bullets
        #The empty method  will help us clear all object in Sprite group.
        cls.bullets.empty()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        pygame.sprite.Sprite.__init__(self)
        #Load an image
        self.image = pygame.image.load('asset/bullet.png')#22 * 22

        #Get the object of rectangle based on the image
        self.rect = self.image.get_rect()
        self.rect.topleft = [x + 100/2 - 22/2, y - 22 ]

        self.screen = screen
        self.speed = 10

    def update(self):
        #Change the position of every bullet
        self.rect.top -= self.speed
        # If the bullet moves out of the screen, delete the bullet
        if self.rect.top < -22:
            self.kill()

class EnemyPlane(pygame.sprite.Sprite):
    #All bullets from enemy
    enemy_bullets = pygame.sprite.Group()
    def __init__(self,screen):
        # Call the initial method of Sprite.
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('asset/enemy0.png')  #51*39
        # Get the object of rectangle based on the image cause every collision is about rectangles.
        self.rect = self.image.get_rect()
        #Choose the random numbers below the width of screen.
        x = random.randrange(1, Manage.bg_size[0],50)
        # Get the position of rectangle.
        self.rect.topleft = [x, 0]

        self.speed = 5
        # Show it into the screen
        self.screen = screen
        # This method returns a list.
        self.bullets = pygame.sprite.Group()
        self.direction = 'right'

    def display(self):
        # # 5 Combine the plane and background
        self.screen.blit(self.image, self.rect)
        #Every bullet need to be displayed on the screen.
        self.bullets.update()
        # Every bullet need to be displayed on the screen.
        # It like iterates every bullet.
        self.bullets.draw(self.screen)

    def auto_move(self):
        if self.direction == 'right':
            self.rect.right += self.speed
        elif self.direction == 'left':
            self.rect.right -= self.speed

        if self.rect.right > Manage.bg_size[0] - 51:
            self.direction = 'left'
        elif self.rect.right < 0:
            self.direction = 'right'

        self.rect.bottom += self.speed

    def auto_fire(self):
        random_num = random.randint(1,20)
        if random_num == 8:
            bullet = EnemyBullets(self.screen, self.rect.left, self.rect.top )
            self.bullets.add(bullet)
            #Add  the enemy bullets  to a group
            EnemyPlane.enemy_bullets.add(bullet)

    @classmethod
    def clear_bullets(cls):
        # clear bullets
        cls.enemy_bullets.empty()

    def update(self):
        self.auto_move()
        self.auto_fire()
        self.display()

#The enemy bullets:
class EnemyBullets(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        pygame.sprite.Sprite.__init__(self)
        #Load an image
        self.image = pygame.image.load('asset/bullet1.png')#9 * 22

        #Get the object of rectangle based on the image
        self.rect = self.image.get_rect()
        self.rect.topleft = [x + 50/2 - 10/2, y + 39 ]

        self.screen = screen
        self.speed = 10

    def update(self):
        #Change the position of every bullet
        self.rect.bottom += self.speed
        # If the bullet moves out of the screen, delete the bullet
        if self.rect.top > Manage.bg_size[1]:
            self.kill()

class GameSound():
    def __init__(self):
        #initialize the music module
        pygame.mixer.init()
        pygame.mixer.music.load('asset/bg2.ogg')
        #Load the voice of bomb.
        self.__bomb = pygame.mixer.Sound('asset/bomb.wav')
        #Set the volume level
        pygame.mixer.music.set_volume(0.5)

    def playBackgroundMusic(self):
        #Indefinite loop.
        pygame.mixer.music.play(-1)

    def playBombSound(self):
        pygame.mixer.Sound.play(self.__bomb)

class Bomb():
    def __init__(self, screen, type):
        self.screen = screen
        if type == 'enemy':
            #Load the bomb resource of enemies
            self.mImages = [pygame.image.load('asset/enemy0_down' + str(v) +'.png') for v in range(1, 5)]
        else:
            # Load the bomb resource of the hero
            self.mImages = [pygame.image.load('asset/hero_blowup_n' + str(v) +'.png') for v in range(1,  5)]

        #Set the index of bomb
        self.mIndex = 0
        #Set the position of bomb
        self.mPos = [0,0]
        #Visible
        self.mVisible = False

    def action(self, rect):
        #The position of bomb
        self.mPos[0] = rect.left
        self.mPos[1] = rect.top
        #Trigger the bomb
        self.mVisible = True

   #Show the bomb
    def draw(self):
        if not self.mVisible:
            return
        self.screen.blit(self.mImages[self.mIndex], (self.mPos[0], self.mPos[1]))
        self.mIndex += 1
        if self.mIndex >= len(self.mImages):
            #If the index is out of scope, that means bomb ending
            #Then reset the index
            self.mIndex = 0
            self.mVisible = False

class GameBackground():
    def __init__(self, screen):
        self.bImage1 = pygame.image.load('asset/background.png')
        self.bImage2 = pygame.image.load('asset/background.png')
         #We also need a screen
        self.screen = screen
        self.y1 = 0
        self.y2 = -Manage.bg_size[1]
        self.speed = 2

   #Move the background:
    def move(self):
        self.y1 += self.speed
        self.y2 += self.speed
        if self.y1 >= Manage.bg_size[1]:
            #Once the first picture moves to the bottom, then back to the start immediately.
            self.y1 = 0
        if self.y2 >= 0:
            self.y2 = -Manage.bg_size[0]

   # Just stick two backgrounds:
    def draw(self):
        self.screen.blit(self.bImage1, (0,self.y1))
        self.screen.blit(self.bImage2, (0,self.y2))

class Manage():
    bg_size = (480, 852)
    # The timer of game
    game_over_id = 10
    #Create the timer ID of enemy
    create_enemy_id = 11

    #the game is over or not:
    is_game_over = False
    #Countdown time.
    over_time = 3
    def __init__(self):
        #Initialize the font
        pygame.init()
        # Creat a window
        self.screen = pygame.display.set_mode(Manage.bg_size, 0, 32)
        #Load the picture of background
        self.background = pygame.image.load('asset/background.png') #(800, 600)
        self.map = GameBackground(self.screen)
        #Initialize a group to hold sprites about the hero or enemies.
        self.players = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        #Initialize an object about the hero ane enemies blowing up
        self.players_bomb = Bomb(self.screen, 'player')
        self.enemies_bomb = Bomb(self.screen, 'enemy')
        #Initialize an object about Voice
        self.sound = GameSound()

    def exit(self):
        print("Exit!!!")
        pygame.quit()
        exit()

    def show_over_text(self):
        #Game over , restart after countdown time.
        self.drawText('Game Over %d'%Manage.over_time,100, Manage.bg_size[1]/2, textheight=50, fontcolor=[255,0,0])

    def game_over_time(self):
        #Show the text about game over
        self.show_over_text()
        #Every time execute this method, the  countdown time will -1
        Manage.over_time -= 1
        #When the countdown time gets 0:
        if Manage.over_time == 0:
            #Stop the timer.
            pygame.time.set_timer(Manage.game_over_id, 0)
            #After countdown time, restart
            Manage.over_time = 3
            Manage.is_game_over = False
            self.start_game()

    def start_game(self):
        #Restart game, clear some objects:
        EnemyPlane.clear_bullets()
        HeroPlane.clear_bullets()
        #Creat a new object of class Manage and execute it.
        manage = Manage()
        manage.main()

    def new_player(self):
        #Create the objects of airplanes and add them to the player's group
        player = HeroPlane(self.screen)
        self.players.add(player)

    def new_enemy(self):
    # Create the objects of enemies and add them to the player's group
        enemy = EnemyPlane(self.screen)
        self.enemies.add(enemy)

    #Show words:
    def drawText(self, text, x, y, textheight=30, fontcolor=(255, 0, 0), backgroudcolor=None):
        #Get the object of font.
        font_obj = pygame.font.Font('asset/baddf.ttf', textheight)
        #Define the style of words we want to show:
        text_obj = font_obj.render(text, True, fontcolor, backgroudcolor)
        #Get the rectangle of words
        text_rect = text_obj.get_rect()
        #Set the position of words
        text_rect.topleft = (x, y)
        #Define the words into a special area:
        self.screen.blit(text_obj, text_rect)

    def main(self):
        self.sound.playBackgroundMusic()
        self.new_player()
        #Start the timer of enemy planes:
        #Every 1000 milliseconds, the program will automatically create an enemy plane.
        pygame.time.set_timer(Manage.create_enemy_id,1000)

        while True:
            # self.screen.blit(self.background, (0, 0))
            self.map.move()
            #show them into the screen.
            self.map.draw()

            self.drawText('HP:100', 0,0)
            #When the game is over, show the over text:
            if Manage.is_game_over:
                self.show_over_text()

            for event in pygame.event.get():
                # Give feedbacks to every event;
                # Its a list to get events cause there are a lot of events will happen at the same time.
                if event.type == pygame.QUIT:
                    self.exit()
                elif event.type == Manage.create_enemy_id:
                    #Creat an enemy
                    self.new_enemy()
                elif event.type == Manage.game_over_id:
                    #The timer triggers some events:
                    self.game_over_time()

            #Call the object of bomb
            self.players_bomb.draw()
            self.enemies_bomb.draw()

            if self.players.sprites():
                #Tips: Here is the sprite of hero and the group of bullets from enemies.
                isover = pygame.sprite.spritecollide(self.players.sprites()[0], EnemyPlane.enemy_bullets, True)
                if isover:
                    Manage.is_game_over = True
                    pygame.time.set_timer(Manage.game_over_id, 1000)
                    print("Plane hit by enemies")
                    #Show the special effects of bomb:
                    self.players_bomb.action(self.players.sprites()[0].rect)
                    #Remove hero from sprite group
                    self.players.remove(self.players.sprites()[0])
                    #Call the voice
                    self.sound.playBombSound()

                #If impact happen:
                #Double True means if an impact happened, remove the players and enemies.
                #This method will back a dictionary:
                iscollide = pygame.sprite.groupcollide(self.players, self.enemies, True, True)
                if iscollide:
                    #Set the game over:
                    Manage.is_game_over = True
                    #Start the countdown timer
                    pygame.time.set_timer(Manage.game_over_id, 1000)
                    # The list() function is used to convert the dictionary items to a list,
                    # and [0] is used to get the first (and only) item from the list.
                    items = list(iscollide.items())[0]
                    print(items)
                    #x is assigned the key sprite from the first group that collided with an enemy,
                    # and y is assigned the first enemy sprite from the list of sprites that collided with the key sprite.
                    x = items[0]
                    # since items[1] is a list of sprites, [0] is used to get the first sprite from that list:
                    y = items[1][0]
                    #The blast of the hero:
                    self.players_bomb.action(x.rect)
                    # The blast of the enemies:
                    self.enemies_bomb.action(y.rect)
                    # The voice of bomb
                    self.sound.playBombSound()

                # The bullets from a player collide enemies.
                collide_enemies = pygame.sprite.groupcollide(HeroPlane.bullets, self.enemies, True, True)
                if collide_enemies:
                    items = list(collide_enemies.items())[0]
                    y = items[1][0]
                    #The blast of the enemies:
                    self.enemies_bomb.action(y.rect)
                    # The voice of bomb
                    self.sound.playBombSound()

            #Display the hero and bullets
            self.players.update()
            self.enemies.update()

            pygame.display.update()
            time.sleep(0.01)

if __name__ == '__main__':
    manage = Manage()
    manage.main()








