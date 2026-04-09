# Jednoduchý kalkulačka - Dokumentace

## Úvod

Tento projekt implementuje jednoduchou kalkulačku v jazyce Python. Kalkulačka umožňuje základní matematické operace: sčítání, odčítání, násobení a dělení. Program běží v konzoli a interaguje s uživatelem prostřednictvím textového rozhraní.

## Funkce

- **Sčítání (+)**: Sečte dvě čísla.
- **Odčítání (-)**: Odečte druhé číslo od prvního.
- **Násobení (*)**: Vynásobí dvě čísla.
- **Dělení (/)**: Vydělí první číslo druhým (s kontrolou dělení nulou).
- **Opakování**: Uživatel může provádět více výpočtů bez restartování programu.
- **Ukončení**: Program lze ukončit zadáním 'k' místo operátoru.

## Jak používat

1. Spusťte program.
2. Zadejte první číslo.
3. Zadejte operátor (+, -, *, /) nebo 'k' pro konec.
4. Pokud jste nezadali 'k', zadejte druhé číslo.
5. Program zobrazí výsledek a umožní další výpočet.

## Příklad použití

```
Vítejte v kalkulačce!
Zadejte první číslo: 10
Zadejte operátor (+, -, *, /) nebo 'k' pro konec: +
Zadejte druhé číslo: 5
Výsledek: 10.0 + 5.0 = 15.0

Zadejte první číslo: 20
Zadejte operátor (+, -, *, /) nebo 'k' pro konec: /
Zadejte druhé číslo: 4
Výsledek: 20.0 / 4.0 = 5.0

Zadejte první číslo: k
Děkujeme za použití kalkulačky!
```

## Technické detaily

- Program používá cyklus while pro opakované výpočty.
- Vstupy jsou převedeny na float pro podporu desetinných čísel.
- Obsahuje kontrolu chyb pro neplatné vstupy a dělení nulou.
- Používá funkce pro organizaci kódu (get_number, get_operator, calculate, main).</content>
<parameter name="filePath">c:\Users\damid\Documents\Python\idk\idk_projekt.md