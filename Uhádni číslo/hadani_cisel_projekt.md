# 🎯 Hádej číslo (Python)

## 📌 Popis projektu

Tento program je jednoduchá hra, ve které uživatel hádá náhodně vygenerované číslo. Program uživateli napovídá, zda je jeho tip vyšší nebo nižší než hledané číslo.

---

## ⚙️ Použité technologie

* Python 3
* Knihovna `random` (součást Pythonu)

---

## ▶️ Spuštění programu

1. Ujisti se, že máš nainstalovaný Python
2. Spusť soubor:

```bash
python hadani_cisla.py
```

---

## 🎮 Jak hrát

1. Zadáš maximální číslo (např. 100)
2. Program vygeneruje náhodné číslo od 0 do tohoto čísla
3. Postupně hádáš:

   * Program ti řekne, jestli jsi:

     * nad číslem 🔼
     * pod číslem 🔽
4. Hraješ, dokud číslo neuhodneš

---

## 🧠 Jak program funguje

### 🔹 Vstup od uživatele

```python
top_of_range = input("Napiš číslo: ")
```

* Uživatel zadá maximální hodnotu

---

### 🔹 Kontrola vstupu

```python
if top_of_range.isdigit():
```

* Ověří, že uživatel zadal číslo

```python
if top_of_range <= 0:
```

* Číslo musí být větší než 0

---

### 🔹 Generování čísla

```python
random_number = random.randint(0, top_of_range)
```

* Vygeneruje náhodné číslo

---

### 🔹 Hlavní herní smyčka

```python
while True:
```

* Běží, dokud hráč neuhodne číslo

---

### 🔹 Kontrola tipů

```python
if user_guess == random_number:
```

* Správný tip → konec hry

```python
elif user_guess > random_number:
```

* Tip je moc vysoký

```python
else:
```

* Tip je moc nízký

---

### 🔹 Počet pokusů

```python
guesses += 1
```

* Počítá, kolikrát uživatel hádal

---

## 🧾 Výstup

Po správném uhádnutí program vypíše:

```
Dal jsi to za X pokusů!
```

---

## 💡 Možná vylepšení

* Omezení počtu pokusů
* Přidání obtížností (easy / medium / hard)
* Ukládání nejlepších výsledků
* Grafické rozhraní (Tkinter)
* Nápověda (např. „jsi blízko“)

---

## 🧪 Příklad hry

```
Napiš číslo: 50
Hádej: 25
Byl jsi pod číslem!
Hádej: 40
Byl jsi nad číslem!
Hádej: 32
Dal jsi to!
Dal jsi to za 3 pokusů!
```

---

## 🧾 Závěr

Projekt ukazuje práci se vstupem od uživatele, podmínkami, cykly a generováním náhodných čísel v Pythonu. Je ideální pro začátečníky.

---
