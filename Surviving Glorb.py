import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1920, 1080
FPS = 60


# Create a player class
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.walk_frames = {
            'up': [
                pygame.image.load('Backward/Backwards walking left foot.png'),
                pygame.image.load('Backward/Backwards walking right foot.png'),
            ],
            'down': [
                pygame.image.load('Forward/Forward walking left foot.png'),
                pygame.image.load('Forward/Forward walking right foot.png'),
            ],
            'left': [
                pygame.image.load('Left/Left walking left foot.png'),
                pygame.image.load('Left/Left walking right foot.png'),
            ],
            'right': [
                pygame.image.load('Right/Right walking right foot.png'),
                pygame.image.load('Right/Right walking left foot.png'),
            ],
        }

        self.stand_frames = {
            'up': pygame.image.load('Backward/Backwards standing.png'),
            'down': pygame.image.load('Forward/Forward Standing.png'),
            'left': pygame.image.load('Left/Left standing.png'),
            'right': pygame.image.load('Right/Right standing.png'),
        }

        self.direction = 'down'  # Initial direction
        self.frame_index = 0
        self.image = self.stand_frames[self.direction]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 5
        self.animation_speed = 0.1
        self.last_update = pygame.time.get_ticks()

    def update_animation(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.animation_speed * 1000:
            self.last_update = now
            self.frame_index = (self.frame_index + 1) % len(self.walk_frames[self.direction])
            self.image = self.walk_frames[self.direction][self.frame_index]

    def update_standing_image(self):
        self.image = self.stand_frames[self.direction]

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.direction = 'left'
            self.rect.x -= self.speed
        elif keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.direction = 'right'
            self.rect.x += self.speed
        elif keys[pygame.K_UP] and self.rect.top > 0:
            self.direction = 'up'
            self.rect.y -= self.speed
        elif keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.direction = 'down'
            self.rect.y += self.speed
        else:
            # Stop moving, use the standing image
            self.update_standing_image()
            return  # Early return to avoid updating animation when standing

        self.update_animation()

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)


# Main game loop
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Player Movement with Directional Animations and Standing Image Example")

    clock = pygame.time.Clock()

    player = Player(WIDTH // 2, HEIGHT // 2)

    # Load your map image
    map_image = pygame.image.load('Background_1.png')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        player.move(keys)

        screen.blit(map_image, (0, 0))  # Draw the map image
        player.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
