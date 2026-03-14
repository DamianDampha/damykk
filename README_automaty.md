# Dokumentace programu – Automat na sloty (Python)
1. Název programu

Slot Machine (automat na výherní symboly)

Program je napsaný v jazyce Python a simuluje jednoduchý hrací automat, kde hráč může vsadit peníze na několik řádků a pokusit se vyhrát.

2. Popis programu

Program simuluje automat s 3×3 polem symbolů.
Hráč:

vloží peníze

vybere počet řádků

zvolí sázku

automat vygeneruje symboly

program zkontroluje výhru

Pokud jsou na řádku stejné symboly, hráč vyhrává.

3. Konstanty programu

Tyto hodnoty nastavují pravidla hry.

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1

MAX_LINES – maximální počet řádků, na které lze vsadit

MAX_BET – maximální sázka

MIN_BET – minimální sázka

ROWS = 3
COLS = 3

počet řádků

počet sloupců automatu

4. Symboly

Symboly mají různou pravděpodobnost výskytu.

symbol_count = {
"A": 2,
"B": 4,
"C": 6,
"D": 8
}

Čím vyšší číslo, tím častěji se symbol objeví.

5. Hodnota symbolů
symbol_value = {
"A": 5,
"B": 4,
"C": 3,
"D": 2
}

A má nejvyšší výhru

D má nejnižší výhru

6. Funkce programu
check_winnings()

Kontroluje, zda hráč vyhrál.

Parametry:

columns – symboly automatu

lines – počet sázených řádků

bet – výše sázky

values – hodnota symbolů

Funkce:

porovnává symboly na jednotlivých řádcích

pokud jsou stejné → hráč vyhrává

Vrací:

celkovou výhru

seznam výherních řádků

get_slot_machine_spin()

Generuje náhodné symboly pro automat.

Používá knihovnu random.

Postup:

vytvoří seznam všech symbolů

náhodně vybírá symboly

vytvoří sloupce automatu

Výstup:

seznam symbolů v automatu

print_slot_machine()

Vypíše automat do konzole.

Příklad výstupu:

A | C | D
B | A | C
D | D | B
deposit()

Ptá se hráče, kolik chce vložit peněz.

Kontroluje:

zda je vstup číslo

zda je větší než 0

Vrací:

vloženou částku

get_number_of_lines()

Zjišťuje počet řádků, na které chce hráč vsadit.

Podmínka:

1 <= lines <= MAX_LINES
get_bet()

Zjišťuje výši sázky na jeden řádek.

Podmínka:

MIN_BET <= bet <= MAX_BET
spin()

Simuluje jedno otočení automatu.

Kroky:

hráč vybere řádky

zadá sázku

zkontroluje se, zda má dost peněz

vygeneruje se automat

vypíší se symboly

spočítá se výhra

Vrací:

zisk nebo ztrátu hráče

7. Hlavní funkce
main()

Řídí celý program.

Postup:

hráč vloží peníze

zobrazí se aktuální zůstatek

hráč může:

hrát (Enter)

ukončit hru (q)

program běží v cyklu dokud hráč neukončí hru

8. Ukončení programu

Po ukončení se vypíše:

Odešel jsi s $X

kde X je konečný zůstatek hráče.

9. Shrnutí

Program simuluje jednoduchý výherní automat, který:

používá náhodné generování symbolů

kontroluje výherní kombinace

pracuje s peněžním zůstatkem hráče

využívá funkce a cykly v Pythonu
