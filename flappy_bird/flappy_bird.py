# Udělám flappy bird hru pomocí knihovny pygame

import pygame
import random

# Inicializace pygame
pygame.init()

# Nastavení obrazovky
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Hodiny pro kontrolu FPS
clock = pygame.time.Clock()
FPS = 60

# Barvy
SKY_BLUE = (135, 206, 235)
BIRD_COLOR = (255, 255, 0)
PIPE_COLOR = (0, 128, 0)
GROUND_COLOR = (139, 69, 19)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Konstanty pro hru
GRAVITY = 0.5
BIRD_JUMP = -8
PIPE_WIDTH = 70
PIPE_GAP = 150
PIPE_SPEED = 4
GROUND_HEIGHT = 100

# Třída pro ptáka
class Bird:
    def __init__(self):
        self.x = 50
        self.y = HEIGHT // 2
        self.velocity = 0
        self.radius = 15

    def jump(self):
        # Pták skočí nahoru
        self.velocity = BIRD_JUMP

    def update(self):
        # Aktualizace pozice ptáka s gravitací
        self.velocity += GRAVITY
        self.y += self.velocity

    def draw(self, screen):
        # Nakreslení ptáka jako kruh
        pygame.draw.circle(screen, BIRD_COLOR, (self.x, int(self.y)), self.radius)

# Třída pro trubky
class Pipe:
    def __init__(self, x):
        self.x = x
        self.height = random.randint(50, HEIGHT - GROUND_HEIGHT - PIPE_GAP - 50)
        self.passed = False

    def update(self):
        # Pohyb trubky doleva
        self.x -= PIPE_SPEED

    def draw(self, screen):
        # Nakreslení horní a dolní trubky
        pygame.draw.rect(screen, PIPE_COLOR, (self.x, 0, PIPE_WIDTH, self.height))
        pygame.draw.rect(screen, PIPE_COLOR, (self.x, self.height + PIPE_GAP, PIPE_WIDTH, HEIGHT - self.height - PIPE_GAP - GROUND_HEIGHT))

    def collide(self, bird):
        # Kontrola kolize s ptákem
        bird_rect = pygame.Rect(bird.x - bird.radius, bird.y - bird.radius, bird.radius * 2, bird.radius * 2)
        top_pipe = pygame.Rect(self.x, 0, PIPE_WIDTH, self.height)
        bottom_pipe = pygame.Rect(self.x, self.height + PIPE_GAP, PIPE_WIDTH, HEIGHT - self.height - PIPE_GAP - GROUND_HEIGHT)
        return bird_rect.colliderect(top_pipe) or bird_rect.colliderect(bottom_pipe)

# Funkce pro kreslení země
def draw_ground():
    pygame.draw.rect(screen, GROUND_COLOR, (0, HEIGHT - GROUND_HEIGHT, WIDTH, GROUND_HEIGHT))

# Funkce pro zobrazení skóre
def draw_score(score):
    font = pygame.font.SysFont(None, 36)
    text = font.render(f"Skóre: {score}", True, WHITE)
    screen.blit(text, (10, 10))

# Funkce pro zobrazení game over obrazovky
def game_over_screen(score):
    font = pygame.font.SysFont(None, 48)
    text = font.render("Game Over", True, BLACK)
    score_text = font.render(f"Skóre: {score}", True, BLACK)
    restart_text = font.render("Stiskni SPACE pro restart", True, BLACK)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - 100))
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 - 50))
    screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2))

# Hlavní funkce hry
def main():
    bird = Bird()
    pipes = []
    score = 0
    running = True
    game_over = False
    countdown = 0  # Počítadlo pro odpocet při restartu

    # Vytvoření první trubky
    pipes.append(Pipe(WIDTH))

    while running:
        screen.fill(SKY_BLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if game_over and countdown == 0:
                        # Zahájení odpocetu při restartu - pták se nastaví do výchozí pozice
                        bird = Bird()
                        countdown = 3 * FPS  # 3 sekundy při 60 FPS
                    elif not game_over:
                        bird.jump()

        if countdown > 0:
            # Odpocet - nezaktualizujeme hru
            countdown -= 1
            if countdown == 0:
                # Konec odpocetu - restart hry (trubky a skóre)
                pipes = [Pipe(WIDTH)]
                score = 0
                game_over = False
        elif not game_over:
            # Aktualizace ptáka
            bird.update()

            # Aktualizace trubek
            for pipe in pipes:
                pipe.update()

            # Odstranění trubek mimo obrazovku
            pipes = [pipe for pipe in pipes if pipe.x > -PIPE_WIDTH]

            # Přidání nové trubky
            if pipes[-1].x < WIDTH - 200:
                pipes.append(Pipe(WIDTH))

            # Kontrola kolize s trubkami
            for pipe in pipes:
                if pipe.collide(bird):
                    game_over = True

            # Kontrola kolize se zemí nebo stropem
            if bird.y + bird.radius >= HEIGHT - GROUND_HEIGHT or bird.y - bird.radius <= 0:
                game_over = True

            # Aktualizace skóre
            for pipe in pipes:
                if not pipe.passed and pipe.x + PIPE_WIDTH < bird.x:
                    pipe.passed = True
                    score += 1

        # Kreslení
        bird.draw(screen)
        for pipe in pipes:
            pipe.draw(screen)
        draw_ground()
        draw_score(score)

        if game_over and countdown == 0:
            game_over_screen(score)

        # Zobrazení odpocetu pokud probíhá
        if countdown > 0:
            countdown_seconds = (countdown // FPS) + 1  # Zobrazení 3, 2, 1
            font = pygame.font.SysFont(None, 72)
            text = font.render(str(countdown_seconds), True, BLACK)
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

# Spuštění hry
if __name__ == "__main__":
    main()