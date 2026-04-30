# Správa knihovny knih

## Popis
Tato jednoduchá aplikace v Pythonu umožňuje uživateli spravovat kolekci knih. Uživatel může:
- přidávat nové knihy,
- mazat knihy podle názvu,
- vyhledávat knihy podle části názvu nebo podle autora,
- zobrazovat všechny knihy uložené v paměti během běhu programu.

## Jak to funguje
Program je složen ze tří hlavních částí:
1. `Book` - model knihy se třemi atributy: `title`, `author`, `year`.
2. `Library` - třída, která drží seznam knih a poskytuje metody pro práci s ním.
3. `main()` - uživatelské menu, které běží v nekonečném cyklu.

### `Book`
- `__init__(self, title, author, year)` vytvoří novou knihu.
- `__str__(self)` vrací hezky formátovaný řetězec, který se zobrazí v seznamu.

### `Library`
- `self.books = []` drží všechny knihy v seznamu.
- `add_book(self, book)` přidá objekt `Book` do seznamu a vypíše zprávu.
- `remove_book(self, title)` prochází knihy a porovnává názvy bez ohledu na velká/malá písmena.
  - Pokud najde shodu, knihu odstraní a vrátí `True`.
  - Pokud nenajde, vrátí `False`.
- `search_by_title(self, title)` vrací seznam knih, jejichž název obsahuje hledaný text.
- `search_by_author(self, author)` vrací seznam knih, jejichž autor obsahuje hledaný text.
- `display_all_books(self)` vytiskne všechny knihy nebo informaci, že je knihovna prázdná.

### `main()`
Funkce spouští tyto kroky:
1. Vytvoří instanci `Library`.
2. Přidá tři ukázkové knihy do knihovny.
3. Zobrazí uživatelské menu s možnostmi 1 až 6.
4. Čte volbu pomocí `input()` a dle volby provádí akce.

Uživatelské vstupy jsou zpracovány takto:
- Při volbě `1` se zadá název, autor a rok. Rok se převádí na číslo pomocí `int()`.
- Při volbě `2` program vyzve k názvu knihy k odstranění.
- Při volbě `3` nebo `4` program hledá knihy podle textu zadaného uživatelem.
- Při volbě `5` zobrazí všechny knihy.
- Při volbě `6` ukončí program.
- Pokud uživatel zadá něco jiného než číslo 1–6, vypíše se chyba.

## Detailní vysvětlení
- `input().strip()` odstraní mezery na začátku a konci, aby volba nebo název knihy fungovala i když uživatel omylem napíše mezeru.
- `title.lower()` a `author.lower()` zajistí, že vyhledávání a mazání funguje bez ohledu na velká a malá písmena.
- Seznam knih je uložen pouze v paměti programu, takže při ukončení aplikace se data vymažou.
- Kontrola `if __name__ == "__main__":` zajistí, že `main()` poběží pouze při přímém spuštění souboru, ne při importu do jiného programu.

## Jak spustit
1. Ujistěte se, že máte nainstalovaný Python 3.x.
2. Otevřete příkazový řádek v adresáři `Projekt`.
3. Spusťte příkaz:
   ```bash
   python projekt.py
   ```

## Příklad interakce
- Vyberte `1` pro přidání nové knihy.
- Vyberte `3` a zadejte `1984` pro vyhledání knihy podle názvu.
- Vyberte `5` pro zobrazení všech knih.
- Vyberte `6` pro ukončení programu.

## Autor
Vytvořeno pomocí GitHub Copilot, 2026-04-30.