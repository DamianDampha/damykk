# ⚖️ BMI Kalkulačka v Pythonu

## 📌 Popis projektu

Tento program slouží k výpočtu BMI (Body Mass Index). Uživatel zadá svou výšku a váhu a program vypočítá BMI a zařadí ho do příslušné kategorie (podváha, normální váha, nadváha apod.).

---

## ⚙️ Použité technologie

* Python 3
* Základní vstup/výstup (`input`, `print`)
* Podmínky (`if`, `elif`, `else`)

---

## ▶️ Spuštění programu

1. Ujisti se, že máš nainstalovaný Python
2. Spusť soubor:

```bash id="x92k3q"
python bmi_kalkulacka.py
```

---

## 🎮 Jak program používat

1. Zadej svou výšku v centimetrech (např. 180)
2. Zadej svou hmotnost v kilogramech (např. 75)
3. Program vypočítá BMI a zobrazí výsledek

---

## 🧠 Jak program funguje

### 🔹 Vstup od uživatele

```python id="c5x8vr"
Height = float(input("Zadej svou výšku v cm: "))
Weight = float(input("Zadej svou hmotnost v kg: "))
```

* Uživatel zadává hodnoty jako desetinná čísla

---

### 🔹 Převod výšky

```python id="v2m9ld"
Height = Height / 100
```

* Převod z centimetrů na metry

---

### 🔹 Výpočet BMI

```python id="k8z3qn"
BMI = Weight / (Height * Height)
```

* Vzorec: váha / (výška²)

---

### 🔹 Vyhodnocení výsledku

```python id="j7n4pt"
if BMI <= 16:
```

* Velká podváha

```python id="p3x6mb"
elif BMI <= 18.5:
```

* Podváha

```python id="t9v2rc"
elif BMI <= 25:
```

* Normální váha

```python id="y4k7dn"
elif BMI <= 30:
```

* Nadváha

```python id="u8z1lw"
else:
```

* Těžká nadváha

---

## 📊 Kategorie BMI

| BMI hodnota | Kategorie     |
| ----------- | ------------- |
| ≤ 16        | Velká podváha |
| 16 – 18.5   | Podváha       |
| 18.5 – 25   | Norma         |
| 25 – 30     | Nadváha       |
| > 30        | Těžká nadváha |

---

## 🧾 Výstup

Program vypíše:

```id="z7v3kx"
Tvůj body mass index je: XX
```

* odpovídající kategorii

---

## 💡 Možná vylepšení

* Zaokrouhlení BMI (např. na 2 desetinná místa)
* Ošetření špatného vstupu (try/except)
* Přidání doporučení (např. ideální váha)
* Grafické rozhraní (Tkinter)
* Uložení výsledků

---

## 🧪 Příklad použití

```id="q8m1nv"
Zadej svou výšku v cm: 180
Zadej svou hmotnost v kg: 75

Tvůj body mass index je: 23.15
jsi v normě
```

---

## 🧾 Závěr

Projekt ukazuje základní práci se vstupem od uživatele, výpočty a podmínkami v Pythonu. Je ideální pro začátečníky.

---

## 👤 Autor

* Student Pythonu 😄
