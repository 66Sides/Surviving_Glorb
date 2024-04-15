import pygame
import sys
import time
import subprocess

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1920, 1080
FPS = 60

# Load background images
menu_background = pygame.image.load('menu_background.png')  # Replace with your menu background image
loading_background = pygame.image.load('loading_background.png')  # Replace with your loading background image


# Create a screen class for the menu
class MenuScreen:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)
        self.title_font = pygame.font.Font(None, 72)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return LoadingScreen()

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(menu_background, (0, 0))
        title_text = self.title_font.render("Game Menu", True, (255, 0, 0))
        self.draw_text_box(screen, title_text, ((WIDTH - title_text.get_width()) // 2, 50))

        text = self.font.render("Press SPACE to start loading", True, (0, 0, 0))
        self.draw_text_box(screen, text, ((WIDTH - text.get_width()) // 2, 200))

    def draw_text_box(self, screen, text_surface, position):
        box_width = text_surface.get_width() + 10
        box_height = text_surface.get_height() + 5
        box_rect = pygame.Rect(position, (box_width, box_height))
        pygame.draw.rect(screen, (255, 255, 255), box_rect)  # Box background color
        screen.blit(text_surface, (position[0] + 5, position[1] + 2))  # Adjust text position inside the box


# Create a screen class for the loading screen
class LoadingScreen:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)
        self.loading_text = self.font.render("Loading...", True, (0, 0, 0))
        time.sleep(5)
        subprocess.run(["Python", "Surviving Glorb.py"])

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        # Loading
        pygame.time.delay(3000)

    def draw(self, screen):
        screen.blit(loading_background, (0, 0))
        self.draw_text_box(screen, self.loading_text, ((WIDTH - self.loading_text.get_width()) // 2, 200))

    def draw_text_box(self, screen, text_surface, position):
        box_width = text_surface.get_width() + 10
        box_height = text_surface.get_height() + 5
        box_rect = pygame.Rect(position, (box_width, box_height))
        pygame.draw.rect(screen, (255, 255, 255), box_rect)  # Box background color
        screen.blit(text_surface, (position[0] + 5, position[1] + 2))  # Adjust text position inside the box


# Main game loop
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Menu and Loading Screens Example")

    clock = pygame.time.Clock()

    current_screen = MenuScreen()

    while True:
        events = pygame.event.get()

        # Handle events specific to the current screen
        next_screen = current_screen.handle_events(events)

        if next_screen:
            current_screen = next_screen

        # Update and draw the current screen
        current_screen.update()
        current_screen.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
