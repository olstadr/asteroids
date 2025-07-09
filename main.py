# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
Player.containers = (updatable, drawable)

def main():

    print("""
Starting Asteroids!
Screen width: 1280
Screen height: 720
""")

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    last_keys = pygame.key.get_pressed()
    running = True

    while running:
        screen.fill("black")
        current_keys = pygame.key.get_pressed()
        updatable.update(dt, current_keys, last_keys)

        for asteroid in asteroids:
            if player.collide(asteroid) == True:
                print("Game Over!")
                sys.exit()
            for shot in shots:
                if shot.collide(asteroid) == True:
                    shot.kill()
                    asteroid.split()

        for drawable_object in drawable:
            drawable_object.draw(screen)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        last_keys = current_keys
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
