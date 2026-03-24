# 🌀 Fidget Spinner v Pythonu (Turtle)

## 📌 Popis projektu

Tento program vytváří animovaný fidget spinner pomocí knihovny `turtle`. Spinner se roztočí po stisknutí mezerníku a postupně zpomaluje. Na koncích ramen jsou barevné tečky.

---

## ⚙️ Použité technologie

* Python 3
* Knihovna `turtle` (grafika a animace)

---

## ▶️ Spuštění programu

1. Ujisti se, že máš nainstalovaný Python
2. Spusť soubor:

```bash id="y4k8sd"
python spinner.py
```

---

## 🎮 Ovládání

* **Mezerník (SPACE)** → roztočí spinner

---

## 🧠 Jak program funguje

### 🔹 Stav rotace

```python id="r5n2vd"
state = {'turn': 0}
```

* Uchovává aktuální rychlost otáčení

---

### 🔹 Funkce `spinner()`

```python id="x3c9pl"
def spinner():
```

* Vykreslí spinner
* Využívá rotaci podle hodnoty `turn`

```python id="f9k1zb"
angle = state['turn']/10000
```

* Určuje úhel otáčení

* Spinner má 3 ramena:

  * 🔴 červené
  * 🟢 zelené
  * 🔵 modré

---

### 🔹 Funkce `animate()`

```python id="k7d2mz"
def animate():
```

* Postupně zpomaluje spinner:

```python id="t4m8vn"
state['turn'] -= 1
```

* Opakuje animaci každých 20 ms:

```python id="c8n5qp"
ontimer(animate, 20)
```

---

### 🔹 Funkce `flick()`

```python id="z1x6bv"
def flick():
```

* Přidá rychlost při stisku mezerníku:

```python id="u3k9el"
state['turn'] += 10000
```

---

### 🔹 Nastavení okna

```python id="m8c2wr"
setup(420, 420, 370, 0)
```

* Velikost okna: 420×420 px

```python id="b7n4qp"
hideturtle()
tracer(False)
width(20)
```

* Skryje kurzor
* Zrychlí vykreslování
* Nastaví tloušťku čar

---

### 🔹 Ovládání kláves

```python id="p6v3kd"
onkey(flick, 'space')
listen()
```

* Reaguje na stisk mezerníku

---

### 🔹 Spuštění programu

```python id="d9m2xe"
animate()
done()
```

* Spustí animaci
* Udržuje okno otevřené

---

## 🧾 Výsledek

Po spuštění se zobrazí spinner, který:

* se roztočí po stisku mezerníku
* postupně zpomaluje
* vykresluje barevná ramena

---

## 💡 Možná vylepšení

* Přidání více ramen
* Změna barev 🎨
* Zvuk při roztočení 🔊
* Ovládání myší 🖱️
* Nastavení maximální rychlosti

---

## 🧪 Příklad použití

1. Spusť program
2. Stiskni mezerník
3. Sleduj otáčení spinneru 🌀

---

## 🧾 Závěr

Projekt ukazuje práci s animací, časováním a interakcí s uživatelem v Pythonu pomocí knihovny `turtle`. Je vhodný pro začátečníky i jako základ pro grafické projekty.

---

## 👤 Autor

* Student Pythonu 😄
