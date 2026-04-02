# Dokumentace projektu Tic-Tac-Toe

## Přehled projektu

Tento projekt implementuje klasickou hru Tic-Tac-Toe (křížky a kolečka) pomocí Pythonu s grafickým rozhraním vytvořeným pomocí knihovny Tkinter. Hra podporuje dva hráče, kteří se střídají v tahu, a sleduje skóre vítězství, proher a remíz.

## Požadavky

- Python 3.x
- Knihovny:
  - tkinter (součást standardní knihovny Pythonu)
  - numpy

## Instalace

1. Ujistěte se, že máte nainstalovaný Python 3.x.
2. Nainstalujte numpy pomocí pip:
   ```
   pip install numpy
   ```
3. Stáhněte nebo naklonujte tento projekt.
4. Spusťte hru spuštěním souboru `idk.py`:
   ```
   python idk/idk.py
   ```

## Použití

Po spuštění se otevře okno s herní deskou 3x3. Hráči se střídají v klíknutí na prázdná pole:
- První hráč používá X (červená)
- Druhý hráč používá O (modrá)

Hra končí, když jeden hráč získá tři symboly v řadě (horizontálně, vertikálně nebo diagonálně), nebo když je deska plná (remíza). Po skončení hry se zobrazí skóre a možnost hrát znovu kliknutím kamkoli.

## Struktura kódu

### Globální proměnné

- `size_of_board`: Velikost herní desky v pixelech (600)
- `symbol_size`: Velikost symbolů X a O
- `symbol_thickness`: Tloušťka čar symbolů
- `symbol_X_color`: Barva pro X ('#EE4035' - červená)
- `symbol_O_color`: Barva pro O ('#0492CF' - modrá)
- `Green_color`: Barva pro skóre ('#7BC043' - zelená)

### Třída Tic_Tac_Toe

Hlavní třída obsahující všechnu logiku hry.

#### Inicializační funkce

- `__init__(self)`: Inicializuje okno, plátno, vazby událostí a stav hry.
- `mainloop(self)`: Spustí hlavní smyčku Tkinter.
- `initialize_board(self)`: Nakreslí mřížku na plátně.
- `play_again(self)`: Resetuje desku pro novou hru a střídá začínajícího hráče.

#### Kreslicí funkce

- `draw_O(self, logical_position)`: Nakreslí symbol O na zadané logické pozici.
- `draw_X(self, logical_position)`: Nakreslí symbol X na zadané logické pozici.
- `display_gameover(self)`: Zobrazí konec hry, skóre a možnost hrát znovu.

#### Logické funkce

- `convert_logical_to_grid_position(self, logical_position)`: Převede logickou pozici (0-2) na pixelové souřadnice.
- `convert_grid_to_logical_position(self, grid_position)`: Převede pixelové souřadnice na logickou pozici.
- `is_grid_occupied(self, logical_position)`: Zkontroluje, zda je pole obsazené.
- `is_winner(self, player)`: Zkontroluje, zda zadaný hráč vyhrál.
- `is_tie(self)`: Zkontroluje, zda je remíza.
- `is_gameover(self)`: Zkontroluje konec hry a nastaví příznaky vítězství.

#### Funkce pro zpracování kliknutí myši

- `click(self, event)`: Zpracuje kliknutí myši, umístí symbol a zkontroluje konec hry.

### Stav hry

- `board_status`: 3x3 numpy pole reprezentující stav desky (0 = prázdné, -1 = X, 1 = O)
- `player_X_turns`: Boolean určující, zda je řada na X
- `reset_board`: Boolean pro reset desky
- `gameover`, `tie`, `X_wins`, `O_wins`: Příznaky stavu hry
- `X_score`, `O_score`, `tie_score`: Počítadla skóre

## Architektura

Hra používá MVC-like architekturu:
- **Model**: Stav hry (board_status, skóre)
- **View**: Tkinter plátno pro zobrazení
- **Controller**: Funkce click() pro zpracování vstupu

Kód je rozdělen do sekcí podle funkcí s komentáři v češtině pro lepší srozumitelnost.

## Možná vylepšení

- Přidat AI protihráče
- Podpora pro síťovou hru
- Vlastní nastavení velikosti desky
- Animace a zvuky
- Uložení skóre do souboru

## Licence

Tento projekt je open-source a může být volně používán a upravován.
