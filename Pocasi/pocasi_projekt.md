# Dokumentace k projektu Počasník

## Přehled
`pocasi.py` je jednoduchý simulátor počasí pro několik českých měst. Program generuje fiktivní počasí bez použití API klíčů nebo reálných dat.

## Cíle programu
- zobrazit aktuální počasí pro vybrané město
- zobrazit 5denní předpověď
- porovnat průměrné teploty všech dostupných měst

## Použití
Spusťte soubor přímo v Pythonu:

```bash
python pocasi.py
```

Program se spustí v textovém režimu a nabídne uživateli menu s možnostmi:
1. Aktuální počasí pro město
2. Předpověď na 5 dní
3. Porovnat všechna města
4. Konec

## Dostupná města
V mapě `MESTA` jsou definována následující města:
- Praha
- Brno
- Ostrava
- Plzeň
- Liberec
- Olomouc

## Hlavní komponenty

### `get_rocni_obdobi(mesic: int) -> str`
Určí roční období podle čísla měsíce:
- prosinec, leden, únor → `zima`
- březen, duben, květen → `jaro`
- červen, červenec, srpen → `leto`
- září, říjen, listopad → `podzim`

### `generuj_pocasi(mesto: str, datum: datetime.date) -> dict`
Vygeneruje fiktivní počasí pro zadané město a datum.
Výstup obsahuje:
- `město`
- `datum`
- `teplota`
- `stav`
- `vlhkost`
- `vítr`
- `období`

Teplota se generuje náhodně v rámci hodnot určených pro dané město a roční období.
Stav počasí je vybrán podle vážených pravděpodobností pro aktuální období.

### `vytiskni_pocasi(data: dict)`
Vytiskne formátovaný výstup aktuálního počasí do konzole.

### `predpoved(mesto: str, dni: int)`
Vypíše jednoduchý přehled předpovědi pro ukázkové období. Předpověď zobrazí stav a teplotu pro každý den.

### `porovnej_mesta(dni: int = 1)`
Porovná průměrnou teplotu všech definovaných měst pro zadaný počet dnů a seřadí je od nejteplejšího po nejchladnější.

### `hlavni_menu()`
Interaktivní menu programu. Zpracovává volby uživatele a volá jednotlivé funkce.

## Struktura dat

- `MESTA` - slovník s názvy měst a barem teplot pro roční období.
- `STAVY` - seznam možných stavů počasí.
- `STAVY_VAHA` - váhy pro výběr stavu počasí podle ročního období.

## Příklad použití
1. Spusťte program:
   - `python pocasi.py`
2. Vyberte možnost `1` pro aktuální počasí.
3. Zadejte město, např. `Praha`.
4. Program zobrazí fiktivní počasí pro dnešní datum.

## Poznámky
- Data jsou pouze simulovaná, nejedná se o reálnou předpověď.
- Program používá náhodná čísla, takže opakované spuštění může vrátit odlišné výsledky.
- Jestli chcete program rozšířit, můžete přidat další města, ikony nebo další typy výstupů.
