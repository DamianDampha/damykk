
import os
import pygame
import time
import random
pygame.font.init()  # Inicializace modulu fontů pro Pygame

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # Vytvoření herního okna
pygame.display.set_caption("Space Dodge")  # Nastavení názvu okna

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))  # Adresář se skriptem
BG_PATH = os.path.join(SCRIPT_DIR, "bg.jpeg")  # Cesta k obrázku pozadí
BG = pygame.transform.scale(pygame.image.load(BG_PATH), (WIDTH, HEIGHT))  # Načtení a změna velikosti pozadí

PLAYER_WIDTH = 40  # Šířka hráčova objektu
PLAYER_HEIGHT = 60  # Výška hráčova objektu

PLAYER_VEL = 5  # Rychlost pohybu hráče
STAR_WIDTH = 10  # Šířka meteoritu
STAR_HEIGHT = 20  # Výška meteoritu
STAR_VEL = 3  # Rychlost pádu meteoritu

FONT = pygame.font.SysFont("comicsans", 30)  # Font pro texty ve hře


def draw(player, elapsed_time, stars):
    WIN.blit(BG, (0, 0))  # Vykreslení pozadí

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))  # Zobrazení uplynulého času

    pygame.draw.rect(WIN, "red", player)  # Vykreslení hráče

    for star in stars:
        pygame.draw.rect(WIN, "white", star)  # Vykreslení meteorů

    pygame.display.update()  # Aktualizace displeje


def main():
    run = True  # Příznak pro hlavní smyčku hry

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT,
                         PLAYER_WIDTH, PLAYER_HEIGHT)  # Hráčův objekt
    clock = pygame.time.Clock()  # Hodiny pro nastavení FPS
    start_time = time.time()  # Čas spuštění hry
    elapsed_time = 0  # Uložený uběhlý čas

    star_add_increment = 2000  # Interval pro generování nových meteorů
    star_count = 0  # Čítač uplynulých milisekund

    stars = []  # Seznam aktuálních meteorů
    hit = False  # Příznak zásahu hráče meteoritem

    while run:
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT,
                                   STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)

            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False  # Uživatel zavřel okno
                break

        keys = pygame.key.get_pressed()  # Zjisti stisknuté klávesy
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL  # Pohyb hráče doleva
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL  # Pohyb hráče doprava

        for star in stars[:]:
            star.y += STAR_VEL  # Pád meteoritu dolů
            if star.y > HEIGHT:
                stars.remove(star)  # Odeber meteor, když zmizí za okrajem
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True  # Hráč byl zasažen
                break

        if hit:
            lost_text = FONT.render("You Lost!", 1, "white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()  # Zobrazení zprávy o prohře
            pygame.time.delay(4000)  # Pauza před ukončením
            break

        draw(player, elapsed_time, stars)

    pygame.quit()


if __name__ == "__main__":
    main()