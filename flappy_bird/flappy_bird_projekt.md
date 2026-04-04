# Flappy Bird Hra - Dokumentace

## Úvod

Tento projekt implementuje jednoduchou verzi hry Flappy Bird pomocí knihovny Pygame v jazyce Python. Hra obsahuje ptáka, který musí procházet mezi trubkami, skákáním pomocí mezerníku. Cílem je dosáhnout co nejvyššího skóre bez kolize s trubkami nebo zemí.

## Požadované knihovny

- **pygame**: Knihovna pro tvorbu her v Pythonu, stará se o grafiku, zvuky a vstupy.
- **random**: Standardní knihovna Pythonu pro generování náhodných čísel (používá se pro výšku trubek).

## Konstanty a proměnné

### Nastavení obrazovky
- `WIDTH, HEIGHT = 400, 600`: Rozměry herního okna v pixelech.
- `FPS = 60`: Počet snímků za sekundu pro plynulý běh hry.

### Barvy
- `SKY_BLUE = (135, 206, 235)`: Barva oblohy.
- `BIRD_COLOR = (255, 255, 0)`: Barva ptáka (žlutá).
- `PIPE_COLOR = (0, 128, 0)`: Barva trubek (zelená).
- `GROUND_COLOR = (139, 69, 19)`: Barva země (hnědá).
- `WHITE = (255, 255, 255)`: Bílá barva pro text.
- `BLACK = (0, 0, 0)`: Černá barva pro text.

### Herní konstanty
- `GRAVITY = 0.5`: Síla gravitace, která táhne ptáka dolů.
- `BIRD_JUMP = -6`: Síla skoku ptáka nahoru (záporná hodnota znamená nahoru).
- `PIPE_WIDTH = 70`: Šířka trubek v pixelech.
- `PIPE_GAP = 150`: Mezera mezi horní a dolní trubkou.
- `PIPE_SPEED = 4`: Rychlost pohybu trubek doleva.
- `GROUND_HEIGHT = 100`: Výška země na spodku obrazovky.

## Třídy

### Třída Bird (Pták)
Reprezentuje ptáka ve hře.

#### Atributy
- `x`: Horizontální pozice ptáka (vždy 50).
- `y`: Vertikální pozice ptáka (začíná uprostřed obrazovky).
- `velocity`: Rychlost ptáka (mění se gravitací a skoky).
- `radius`: Poloměr ptáka (15 pixelů).

#### Metody
- `__init__()`: Inicializuje ptáka na výchozí pozici.
- `jump()`: Nastaví rychlost ptáka na hodnotu skoku (nahoru).
- `update()`: Aktualizuje pozici ptáka na základě gravitace.
- `draw(screen)`: Nakreslí ptáka jako žlutý kruh na obrazovku.

### Třída Pipe (Trubka)
Reprezentuje pár trubek (horní a dolní).

#### Atributy
- `x`: Horizontální pozice trubky.
- `height`: Výška horní trubky (náhodně generovaná).
- `passed`: Boolean, zda pták už prošel touto trubkou (pro skóre).

#### Metody
- `__init__(x)`: Inicializuje trubku na pozici x s náhodnou výškou.
- `update()`: Pohybuje trubkou doleva.
- `draw(screen)`: Nakreslí horní a dolní trubku jako zelené obdélníky.
- `collide(bird)`: Kontroluje kolizi ptáka s trubkou pomocí pygame.Rect.

## Funkce

### draw_ground()
Nakreslí zemi na spodku obrazovky jako hnědý obdélník.

### draw_score(score)
Zobrazí aktuální skóre v levém horním rohu obrazovky.

### game_over_screen(score)
Zobrazí "Game Over" obrazovku s konečným skóre a instrukcemi pro restart.

## Hlavní smyčka hry (main())

### Inicializace
- Vytvoří instanci ptáka, prázdný seznam trubek, skóre 0.
- Nastaví `running = True`, `game_over = False`, `countdown = 0`.
- Přidá první trubku.

### Herní smyčka
1. **Vyplnění obrazovky**: Nastaví pozadí na modrou barvu.
2. **Zpracování událostí**:
   - Klávesa SPACE: Pokud hra skončila a není countdown, spustí countdown a resetuje ptáka na výchozí pozici.
   - Během hry: Pták skočí.
3. **Aktualizace hry** (pokud není game_over a není countdown):
   - Aktualizuje ptáka (gravitace).
   - Aktualizuje všechny trubky (pohyb doleva).
   - Odstraňuje trubky mimo obrazovku.
   - Přidává nové trubky.
   - Kontroluje kolize s trubkami a zemí/stropem.
   - Aktualizuje skóre při průchodu trubkou.
4. **Countdown**: Pokud probíhá, snižuje čítač a zobrazuje číslo (3, 2, 1).
   - Po skončení countdown resetuje trubky, skóre a ukončí game_over.
5. **Kreslení**:
   - Nakreslí ptáka, trubky, zem, skóre.
   - Pokud game_over a není countdown, zobrazí game over obrazovku.
   - Pokud countdown, zobrazí číslo countdown.
6. **Aktualizace obrazovky**: `pygame.display.flip()`.
7. **Časování**: `clock.tick(FPS)` pro udržení 60 FPS.

## Jak hrát

1. Spusťte hru spuštěním souboru `flappy_bird.py`.
2. Stiskněte mezerník pro skok ptáka nahoru.
3. Vyhněte se kolizi s trubkami a zemí.
4. Po skončení hry stiskněte mezerník pro spuštění 3sekundového countdown a restart.
5. Cílem je dosáhnout co nejvyššího skóre.

## Vylepšení a poznámky

- Hra používá jednoduchou fyziku s konstantní gravitací.
- Trubky se generují náhodně, ale zajišťují průchod.
- Při restartu je 3sekundový countdown, během kterého je pták ve výchozí pozici.
- Kód je komentovaný v češtině pro lepší pochopení.
- Možná vylepšení: Přidat zvuky, animace, lepší grafiku, vysoké skóre uložení.