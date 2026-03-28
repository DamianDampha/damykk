# ♟️ Two-Player Chess (Pygame)

Jednoduchá šachová hra pro dva hráče vytvořená v jazyce Python pomocí knihovny Pygame.

🎮 Popis projektu

Tento projekt implementuje klasické šachy pro dva hráče na jednom počítači.

Hra obsahuje:

plně funkční šachovnici (8x8)
pohyb všech figurek
střídání tahů (bílý / černý)
zobrazování možných tahů
braní figurek
detekci šachu
ukončení hry (výhra)
⚙️ Požadavky
Python 3.x
Pygame

Instalace Pygame:

pip install pygame
▶️ Spuštění programu
python chess.py
🧩 Ovládání
Kliknutí myší = výběr figurky
Kliknutí na políčko = provedení tahu
Hráči se střídají (bílý → černý)
Tlačítko FORFEIT = vzdání hry
ENTER po konci hry = restart
🧠 Jak hra funguje
🏁 Inicializace
Nastavení okna (1000x900)
Načtení obrázků figurek
Inicializace pozic figurek
♟️ Herní logika

Program používá:

seznamy pro ukládání figurek (white_pieces, black_pieces)
seznamy pozic (white_locations, black_locations)
funkce pro kontrolu tahů
🔍 Kontrola tahů

Každá figurka má vlastní funkci:

check_pawn() → pěšec
check_rook() → věž
check_knight() → jezdec
check_bishop() → střelec
check_queen() → královna
check_king() → král
🎨 Vykreslování
draw_board() → šachovnice
draw_pieces() → figurky
draw_valid() → možné tahy
draw_captured() → sebrané figurky
draw_check() → šach
draw_game_over() → konec hry
🔄 Herní smyčka

Program běží ve smyčce:

vykresluje hru
zpracovává kliknutí
aktualizuje tahy
kontroluje výhru
🏆 Konec hry

Hra končí:

sebráním krále
nebo vzdáním (FORFEIT)
