# Raketka / Space Dodge - Dokumentace

## Popis projektu
Tento projekt je jednoduchá hra vytvořená v Pythonu pomocí knihovny `pygame`. Hráč ovládá červenou raketu, která se pohybuje horizontálně dole na obrazovce a snaží se vyhnout padajícím meteorům.

## Hlavní vlastnosti
- Herní okno s pevným rozlišením 1000×800 pixelů.
- Pozadí načtené ze souboru `bg.jpeg`.
- Hráč může jet doleva a doprava pomocí kurzorových kláves.
- Meteority padají shora dolů a postupně se zrychlují.
- Pokud raketu zasáhne meteorit, hra skončí a zobrazí se zpráva o prohře.

## Závislosti
- `pygame`
- `time` (standardní knihovna Pythonu)
- `os` (standardní knihovna Pythonu)
- `random` (standardní knihovna Pythonu)

## Souborová struktura
- `raketka.py` - vlastní herní logika včetně inicializace, vykreslování, generování meteorů a detekce kolizí.
- `bg.jpeg` - obrázek pozadí, který se v herním okně vykresluje pod herními objekty.
- `raketka_projekt.md` - dokumentace projektu.

## Popis hlavních částí kódu

### Inicializace
- `pygame.font.init()` - inicializuje modul pro práci s fonty.
- `WIDTH`, `HEIGHT` - rozměry herního okna.
- `WIN = pygame.display.set_mode((WIDTH, HEIGHT))` - vytvoření okna.
- `pygame.display.set_caption("Space Dodge")` - nastavení titulku okna.
- `BG_PATH` - absolutní cesta k souboru `bg.jpeg`.
- `BG = pygame.transform.scale(pygame.image.load(BG_PATH), (WIDTH, HEIGHT))` - načtení a změna velikosti obrázku pozadí.

### Konstanty pro herní objekty
- `PLAYER_WIDTH`, `PLAYER_HEIGHT` - rozměry hráčova objektu.
- `PLAYER_VEL` - rychlost pohybu hráče.
- `STAR_WIDTH`, `STAR_HEIGHT`, `STAR_VEL` - rozměry a rychlost meteorů.
- `FONT` - font použitý pro vykreslení textu.

### Funkce `draw(player, elapsed_time, stars)`
Funkce vykresluje aktuální herní stav:
- pozadí (`BG`)
- uplynulý čas v sekundách
- hráčovu raketu
- všechny meteority
- aktualizuje displej pomocí `pygame.display.update()`

### Funkce `main()`
Funkce obsahuje hlavní herní smyčku a logiku ovládání:
- vytvoření hráčova objektu jako `pygame.Rect`
- nastavení `clock` pro řízení FPS
- spuštění odpočtu času
- generování meteorů každých několik milisekund
- zpracování události `pygame.QUIT`
- čtení stavu kláves a pohyb hráče vlevo/vpravo
- aktualizace pozice meteorů a odstranění těch, které spadnou pod okraj
- detekce kolize meteoritu s hráčem
- zobrazení zprávy "You Lost!" v případě zásahu
- ukončení hry voláním `pygame.quit()`

### Generování meteorů
- `star_count` sčítá čas v milisekundách každým tikem `clock.tick(60)`.
- když `star_count` překročí hodnotu `star_add_increment`, vytvoří se tři nové meteority.
- `star_add_increment` se postupně snižuje až na minimálně 200, takže meteority se generují častěji.

### Detekce kolizí
- Každý meteor se posouvá dolů pomocí `star.y += STAR_VEL`.
- Meteor se odstraní, když opustí spodní okraj obrazovky.
- Pokud meteor narazí do hráče (`star.colliderect(player)`), nastaví se příznak `hit = True` a hra končí.

## Ovládání
- šipka vlevo: pohyb hráče doleva
- šipka vpravo: pohyb hráče doprava

## Doporučení pro úpravy
- přidat skóre nebo počítadlo času
- zvýšit variabilitu meteorů (různé velikosti, rychlosti)
- přidat restartovací obrazovku po prohře
- zlepšit vzhled herních objektů pomocí sprites místo `pygame.draw.rect`
