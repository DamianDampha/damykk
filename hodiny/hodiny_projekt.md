# 🕒 Digitální hodiny v Pythonu (Tkinter)

## 📌 Popis projektu

Tento program vytváří jednoduché digitální hodiny pomocí knihovny Tkinter. Zobrazuje aktuální čas ve formátu HH:MM:SS a automaticky ho aktualizuje v reálném čase.

---

## ⚙️ Použité technologie

* Python 3
* Knihovna `tkinter` (GUI – grafické rozhraní)
* Knihovna `time` (práce s časem)

---

## ▶️ Spuštění programu

1. Ujisti se, že máš nainstalovaný Python
2. Spusť soubor:

```bash id="o2q8xq"
python digital_clock.py
```

---

## 🧠 Jak program funguje

### 🔹 Vytvoření okna

```python id="x3sl0d"
app_window = Tk()
```

* Vytvoří hlavní okno aplikace

```python id="1x0k2s"
app_window.title("Digital Clock")
```

* Nastaví název okna

```python id="dpg3b4"
app_window.geometry("420x150")
```

* Nastaví velikost okna

---

### 🔹 Nastavení vzhledu

```python id="p3r6qz"
text_font = ("Boulder", 68, 'bold')
```

* Font a velikost textu

```python id="v6tn7k"
background = "#f2e750"
foreground = "#363529"
```

* Barvy pozadí a textu

```python id="5t7b4y"
border_width = 25
```

* Šířka okraje

---

### 🔹 Vytvoření labelu (textového pole)

```python id="c5y6m1"
label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
label.grid(row=0, column=1)
```

* Zobrazuje aktuální čas v okně

---

### 🔹 Aktualizace času

```python id="2h6n8x"
def digital_clock():
```

* Funkce pro aktualizaci času

```python id="x6n3jv"
time_live = time.strftime("%H:%M:%S")
```

* Získá aktuální čas

```python id="j3k8p1"
label.config(text=time_live)
```

* Aktualizuje text

```python id="9m2s8q"
label.after(200, digital_clock)
```

* Opakuje funkci každých 200 ms

---

### 🔹 Spuštění aplikace

```python id="w3k9zn"
digital_clock()
app_window.mainloop()
```

* Spustí hodiny a GUI smyčku

---

## 🧾 Výsledek

Po spuštění se zobrazí okno s digitálními hodinami, které se automaticky aktualizují každých 0,2 sekundy.

---

## 💡 Možná vylepšení

* Přidání data 📅
* Přepnutí mezi 12h / 24h formátem
* Alarm (budík) 🔔
* Změna barev nebo fontu
* Přidání tlačítka (start/stop)

---

## 🧪 Příklad použití

Program běží automaticky po spuštění a není potřeba žádný vstup od uživatele.

---

## 🧾 Závěr

Projekt ukazuje práci s grafickým rozhraním, časem a automatickou aktualizací dat v Pythonu. Je vhodný pro začátečníky i jako základ pro složitější GUI aplikace.

---

## 👤 Autor

* Student Pythonu 😄
