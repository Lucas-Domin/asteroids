from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED
import pygame

class Player(CircleShape):
    def __init__(self, x, y):
        # Call the parent class's constructor
        super().__init__(x, y, PLAYER_RADIUS)
        # Initialize rotation to 0
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        # This is the method you need to implement
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(dt):
        self.rotation += dt * PLAYER_TURN_SPEED  

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            # Rotate left
            self.rotation -= dt * PLAYER_TURN_SPEED

        if keys[pygame.K_d]:
            # Rotate right
            self.rotation += dt * PLAYER_TURN_SPEED