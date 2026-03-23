# 🎰 Slot Machine v Pythonu

## 📌 Popis projektu

Tento program simuluje jednoduchý automat (slot machine), kde hráč sází peníze na řádky a snaží se vyhrát kombinací stejných symbolů. Program pracuje v terminálu a využívá náhodné generování.

---

## ⚙️ Použité technologie

* Python 3
* Knihovna `random` (pro generování symbolů)

---

## ▶️ Spuštění programu

1. Ujisti se, že máš nainstalovaný Python
2. Spusť soubor:

```bash id="x7g2lm"
python slot_machine.py
```

---

## 🎮 Jak hrát

1. Zadáš, kolik peněz chceš vložit 💰
2. Vybereš počet řádků (1–3)
3. Zadáš sázku na jeden řádek
4. Automat se roztočí 🎰
5. Pokud jsou symboly na řádku stejné → vyhráváš

---

## 🧠 Jak program funguje

### 🔹 Symboly a jejich hodnoty

```python id="1wq8cl"
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
```

* Určuje, kolikrát se symbol objeví (pravděpodobnost)

```python id="m3k2xs"
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}
```

* Určuje výhru za symbol

---

### 🔹 Generování slotu

```python id="l2v8df"
get_slot_machine_spin()
```

* Vytvoří náhodnou kombinaci symbolů (3x3)

---

### 🔹 Výpis slotu

```python id="g8n1pz"
print_slot_machine()
```

* Vypíše automat do konzole ve formátu:

```
A | B | C
D | A | B
C | C | C
```

---

### 🔹 Kontrola výhry

```python id="t5m9ka"
check_winnings()
```

* Kontroluje, zda jsou symboly na řádku stejné
* Pokud ano → hráč vyhrává

---

### 🔹 Sázky

* Minimální sázka: `$1`
* Maximální sázka: `$100`
* Max počet řádků: `3`

---

### 🔹 Funkce `spin()`

* Provádí jedno otočení automatu
* Vypočítá výhru nebo ztrátu

---

### 🔹 Hlavní smyčka

```python id="j9v3xk"
main()
```

* Umožňuje hrát opakovaně
* Aktualizuje zůstatek hráče

---

## 💰 Výpočet výhry

Výhra se počítá:

```
výhra = hodnota symbolu × sázka
```

Například:

* Symbol A (hodnota 5)
* Sázka $10
  → Výhra = $50

---

## 🧾 Výstup

Program vypisuje:

* aktuální zůstatek
* vsazené částky
* výsledek spinu
* výhru a výherní řádky

---

## 💡 Možná vylepšení

* Grafické rozhraní (Tkinter) 🎨
* Více symbolů
* Jackpot 💎
* Animace točení
* Ukládání skóre

---

## 🧪 Příklad hry

```
Kolik chceš vložit? $100
Momentální zůstatek: $100
Na kolik řádků chceš vsadit? (1-3)? 2
Kolik chceš vsadit na každý řádek? $10

A | B | C
A | A | A
D | C | B

Vyhráls $50.
Vyhráls na řádcích: 2
```

---

## 🧾 Závěr

Projekt ukazuje práci s funkcemi, podmínkami, cykly a náhodností v Pythonu. Je vhodný pro pokročilejší začátečníky.

---

