# Paměťová hra - Dokumentace

## Přehled projektu

Tento projekt je jednoduchá textová paměťová hra v Pythonu. Hráč musí zopakovat postupně prodlužující se číselnou sekvenci v přesném pořadí.

## Požadavky

- Python 3.x
- Standardní knihovny: `os`, `random`, `time`

## Jak hra funguje

1. Hra spustí první úroveň se sekvencí jedné číslice.
2. Hráč si sekvenci prohlédne, stiskne Enter a obrazovka se vyčistí.
3. Hráč zadá sekvenci zpět.
4. Pokud je odpověď správná, hráč postupuje na další úroveň a sekvence se prodlouží o jedno číslo.
5. Pokud hráč zadá nesprávnou sekvenci, hra končí.

## Funkce v kódu

### `clear_screen()`
Vyčistí konzoli pro Windows i unixové systémy.

### `generate_sequence(length)`
Vytvoří náhodnou číselnou sekvenci délky `length`.

### `show_sequence(sequence)`
Zobrazí sekvenci hráči, nechá ho secvičit paměť a pak vyčistí obrazovku.

### `get_player_answer(length)`
Vyžádá si od hráče odpověď stejné délky jako současná sekvence a ověří, že jde o platný numerický vstup.

### `display_results(level, highest)`
Zobrazí hráči aktuální úroveň a nejlepší dosaženou úroveň.

### `main()`
Hlavní průběh hry, který spouští úrovně až do chybného zadání.

## Spuštění

Spusťte program v příkazové řádce:

```
python pameti_hra/pameti_hra.py
```

## Tipy pro rozšíření

- Přidat možnost úrovní s písmeny nebo barvami.
- Přidat časový limit pro zadání odpovědi.
- Ukládat nejlepší skóre mezi jednotlivými spuštěními.
