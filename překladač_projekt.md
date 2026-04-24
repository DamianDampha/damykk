
# Dokumentace projektu: Překladač.py

Tento projekt je jednoduchá konzolová aplikace v jazyce Python, která slouží k automatickému překladu textu pomocí rozhraní Google Translate.

## Funkcionalita
- **Automatická detekce jazyka:** Program sám pozná, v jakém jazyce je vstupní text napsán.
- **Překlad:** Primárně nastaven pro překlad libovolného textu do angličtiny.
- **Jednoduché ovládání:** Interaktivní rozhraní v příkazové řádce.

## Požadavky
Pro spuštění projektu je vyžadován Python 3.x a knihovna `googletrans`.

### Instalace závislostí
Knihovnu nainstalujete pomocí správce balíčků pip:
```bash
pip install googletrans==4.0.0-rc1
```

## Použití
1. Spusťte skript příkazem `python překladač.py`.
2. Napište libovolné slovo nebo větu.
3. Program vypíše detekovaný zdrojový jazyk a výsledný překlad.
4. Pro ukončení programu napište slovo `konec`.
