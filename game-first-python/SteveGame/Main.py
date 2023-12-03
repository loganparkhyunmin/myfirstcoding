import pygame
import sys
import random

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 400
FPS = 60

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (255,255,255)

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Steve Dinosaur Game")
clock = pygame.time.Clock()
 
# Load Background Image
background_image = pygame.image.load("background.jpg").convert()
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
background_x = 0  # Initial x-position of the background

class Dinosaur(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        original_image = pygame.image.load("mario.png").convert_alpha()  # Load mario image
        self.image = pygame.transform.scale(original_image, (50, 50))  # Scale down the image
        self.rect = self.image.get_rect()
        self.rect.center = (100, HEIGHT - 50)  # Initial position of the dinosaur
        self.velocity = pygame.math.Vector2(0, 0)
        self.gravity = 0.8  # You can adjust this value for jumping gravity
        self.is_jumping = False

    def jump(self):
        if not self.is_jumping:
            self.velocity.y = -15  # Adjust the jump height as needed
            self.is_jumping = True

    def update(self):
        self.velocity.y += self.gravity
        self.rect.y += self.velocity.y

        # Simulate ground collision (adjust the value as per your ground level)
        if self.rect.bottom >= HEIGHT - 50:
            self.rect.bottom = HEIGHT - 50
            self.is_jumping = False

    def move_left(self):
        self.rect.x -= 5  # Adjust the movement speed as needed

    def move_right(self):
        self.rect.x += 5  # Adjust the movement speed as needed

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x):
        super().__init__()
        self.image = pygame.Surface((20, 40))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = HEIGHT - 90
        self.passed = False  # Flag to track if the obstacle has been passed by the player

    def update(self):
        self.rect.x -= 5

        # Reset the obstacle when it moves off-screen
        if self.rect.right < 0:
            self.rect.x = WIDTH
            self.passed = False

def game_over(score):
    font = pygame.font.SysFont(None, 48)
    text = font.render("Game Over!", True, BLACK)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(text, text_rect)

    score_text = font.render(f"Score: {score}", True, BLACK)
    score_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(score_text, score_rect)

    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()


def game():
    player = Dinosaur()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    obstacles = pygame.sprite.Group()
    obstacle_frequency = 60
    counter = 0
    player.score = 0  # Initialize player's score

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jump()

        screen.blit(background_image, (0, 0))

        counter += 1
        if counter == obstacle_frequency:
            new_obstacle = Obstacle(WIDTH)
            obstacles.add(new_obstacle)
            all_sprites.add(new_obstacle)
            counter = 0

        obstacles.update()
        for obstacle in obstacles:
            if pygame.sprite.collide_rect(player, obstacle):
                game_over(player.score)

        # Increment score when player successfully jumps over an obstacle
        for obstacle in obstacles:
            if obstacle.rect.right < player.rect.left and not obstacle.passed:
                obstacle.passed = True
                player.score += 1

        player.update()
        player.draw(screen)
        all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

game()