# airplane_dogfight

Thanks to this teacher for his instructional videos, which allowed me to experience the process and fun of developing games with Python.
The instructional videos : https://www.bilibili.com/video/BV1xM4y1A7gh?p=1&vd_source=ed000ea92e40b552a93415078608918f

HeroPlane is a simple version which lets me know the process of the overall framework, but I have a chance to feel the power and convenience of Sprite in GameSprite file.

There are something I can learn about Sprite from those codes:
(1) By calling some methods of sprites, we can load images, obtain the matrix of images for positioning and collision detection, update the position of images, and clear objects, etc.
(2) By using the group method of sprites, we can manage many sprites at once without the need to iterate through the group. It is very convenient and efficient.


Game Logic:
（1）Game Initialization: Initialize the game using pygame.

（2）Character Definitions:
    HeroPlane: Represents the player's airplane.
    Bullet: Represents the bullets fired by the player.
    EnemyPlane: Represents the enemy planes.
    EnemyBullets: Represents the bullets fired by enemy planes.
    Dynamic Background: The GameBackground class is used for the dynamic scrolling background.
    Sound Effects: The GameSound class is used for playing background music and explosion sounds.
    Explosion Effect: The Bomb class is used to represent the explosion effect when the plane is hit.

（3）Game Main Loop:
    Update the background.
    Check player's actions.
    Check collisions with enemy planes or bullets.
    Display player, enemy planes, and bullets.
    Update the display.
    Game Over: The game ends when the player's plane collides with an enemy plane or an enemy bullet.



This project was an enlightening experience. 
It bridged the gap between theoretical knowledge from my academic studies and practical implementation in a fun, interactive manner.
Not only did it enhance my understanding of game development but also solidified my grasp on Python programming and OOP principles. 

Thanks again to the teacher.

The main window:

<img width="466" alt="the main window" src="https://github.com/freesandwicha/airplane_dogfight/assets/100746570/eb3eb1b7-0ab0-447a-a8b6-94a0a1a3637a">

Hit the enemy:

<img width="485" alt="Hit the enemy" src="https://github.com/freesandwicha/airplane_dogfight/assets/100746570/c0ff6846-9038-45e1-82ae-c05f35cad2a3">

Collision:

<img width="480" alt="collision" src="https://github.com/freesandwicha/airplane_dogfight/assets/100746570/7c24a5cd-7d86-4d2b-8a9c-02a7d0eb038b">

Hit by enemy:

<img width="466" alt="hit by enemy" src="https://github.com/freesandwicha/airplane_dogfight/assets/100746570/f4ea0f32-4a63-4636-91ce-77e38fcb9927">

Restart:

<img width="478" alt="restart" src="https://github.com/freesandwicha/airplane_dogfight/assets/100746570/95db422c-a5c0-4582-89b8-e721768c30ed">
