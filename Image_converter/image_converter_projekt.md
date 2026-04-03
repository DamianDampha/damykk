# Image Converter Projekt - Dokumentace

## Přehled Projektu

Tento projekt je jednoduché desktopové GUI (grafické uživatelské rozhraní) aplikace, která slouží k konverzi obrázků z PNG formátu do JPG formátu. Aplikace byla vytvořena pomocí knihovny **Tkinter** pro uživatelské rozhraní a knihovny **PIL (Pillow)** pro zpracování obrázků.

---

## Použité Knihovny

### 1. **tkinter**
- Standardní Python knihovna pro vytváření grafických uživatelských rozhraní (GUI)
- Součást standardní instalace Pythonu
- V tomto projektu se používá pro:
  - Vytvoření hlavního okna aplikace
  - Vytvoření tlačítek
  - Vytvoření canvasu (plátna) pro umístění prvků
  - Umožnění uživateli vybrat soubory (filedialog)

### 2. **PIL (Pillow)**
- Knihovna pro zpracování obrázků
- Musí se nainstalovat příkazem: `pip install pillow`
- V tomto projektu se používá pro:
  - Otevírání obrázků (Image.open)
  - Ukládání obrázků v jiném formátu (image.save)

---

## Struktura Kódu

### Inicializace Aplikace (Řádky 1-10)

```python
import tkinter as tk
from tkinter import filedialog
from PIL import Image

root = tk.Tk()
canvas1 = tk.Canvas(root, width=300, height=250, bg='azure3', relief='raised')
canvas1.pack()
```

- **import tkinter as tk** - Importuje tkinter knihovnu a přiřazuje jí zkratku `tk`
- **from tkinter import filedialog** - Importuje modul pro otevírání dialogů pro výběr souborů
- **from PIL import Image** - Importuje modul Image z Pillow pro práci s obrázky
- **root = tk.Tk()** - Vytváří hlavní okno aplikace
- **canvas1** - Vytváří plátno (canvas) o velikosti 300×250 pixelů s azurovou barvou pozadí
- **canvas1.pack()** - Umisťuje canvas do okna

### Nadpis Aplikace (Řádky 12-17)

```python
label1 = tk.Label(root, text="Image Converter", bg='azure3')
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 60, window=label1)
```

- Vytváří popisek (Label) s textem "Image Converter"
- Nastavuje font na Helvetica o velikosti 20 pixelů
- Umisťuje popisek na canvas na pozici (150, 60)

### Funkce getPNG() (Řádky 19-23)

```python
def getPNG():
    global im1
    import_file_path = filedialog.askopenfilename()
    im1 = Image.open(import_file_path)
```

**Účel:** Umožňuje uživateli vybrat PNG soubor k otevření

**Popis:**
- **global im1** - Deklaruje proměnnou `im1` jako globální (lze ji používat v jiných funkcích)
- **filedialog.askopenfilename()** - Otevře dialog pro výběr souboru z počítače
- **Image.open()** - Otevře vybraný obrázek a uloží jej do proměnné `im1`

### Tlačítko pro Výběr PNG (Řádky 25-27)

```python
browse_png = tk.Button(text="Select PNG file", command=getPNG, bg="royalblue", fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 130, window=browse_png)
```

- Vytváří tlačítko s textem "Select PNG file"
- **command=getPNG** - Nastaví, že kliknutí na tlačítko spustí funkci `getPNG()`
- Tlačítko má modrou barvu pozadí (royalblue) a bílý text
- Umisťuje tlačítko na canvas na pozici (150, 130)

### Funkce convert() (Řádky 29-32)

```python
def convert():
    global im1
    export_file_path = filedialog.asksaveasfilename(defaultextension='.jpg')
    im1.save(export_file_path)
```

**Účel:** Převádí PNG obrázek na JPG a uložit jej

**Popis:**
- **global im1** - Přistupuje k globální proměnné `im1` (obrázku nahlášenému v getPNG)
- **filedialog.asksaveasfilename()** - Otevře dialog pro uložení souboru
- **defaultextension='.jpg'** - Automaticky nastaví koncovku na .jpg
- **im1.save()** - Uloží obrázek v JPG formátu

### Tlačítko pro Konverzi (Řádky 34-36)

```python
saveasbutton = tk.Button(text="Convert PNG to JPG", command=convert, bg='royalblue', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 180, window=saveasbutton)
root.mainloop()
```

- Vytváří tlačítko s textem "Convert PNG to JPG"
- **command=convert** - Spustí funkci `convert()` při kliknutí
- Umisťuje tlačítko na canvas na pozici (150, 180)
- **root.mainloop()** - Spouští nekonečnou smyčku, která udržuje okno aplikace otevřené a čeká na uživatelské akce

---

## Jak Funguje Aplikace

### Krok za Krokem:

1. **Spuštění aplikace** - Vytvoří se GUI okno s nadpisem a dvěma tlačítky
2. **Uživatel klikne na "Select PNG file"** - Otevře se dialog pro výběr souboru
3. **Uživatel vybere PNG soubor** - Obrázek se načte do paměti (v proměnné `im1`)
4. **Uživatel klikne na "Convert PNG to JPG"** - Otevře se dialog pro uložení souboru
5. **Uživatel vybere místo a název** - Obrázek se uloží v JPG formátu na vybrané místo

### Schéma Toku:

```
Start aplikace
    ↓
Zobrazí se GUI okno
    ↓
Čekání na klik uživatele
    ├→ Klik "Select PNG file"
    │   ↓
    │   Dialog - výběr souboru
    │   ↓
    │   Obrázek se načte (im1)
    │   ↓
    │   Čekání na další akci
    │
    └→ Klik "Convert PNG to JPG"
        ↓
        Dialog - uložení souboru
        ↓
        Obrázek se uloží jako JPG
        ↓
        Konec
```

---

## Barvy a Design Aplikace

| Prvek | Barva | Kód |
|-------|-------|-----|
| Pozadí okna | Azurová | `azure3` |
| Tlačítka - pozadí | Královská modrá | `royalblue` |
| Tlačítka - text | Bílá | `white` |

---

## Požadavky k Spuštění

1. **Python 3.x** - Interpreter Pythonu
2. **tkinter** - Standardně součást Pythonu
3. **Pillow (PIL)** - Nutné nainstalovat:
   ```bash
   pip install pillow
   ```

---

## Spuštění Aplikace

```bash
python Image_converter.py
```

Aplikace se ihned spustí a zobrazí se okno s PNG konvertorem.

---

## Možná Vylepšení

### 1. **Validace vstupů**
- Zkontrolovat, zda byl vybrán soubor před kliknutím "Convert"
- Ošetřit chybu, pokud se nepodaří uložit soubor

### 2. **Rozšíření Formátů**
- Umožnit konverzi z více formátů (BMP, GIF, TIFF)
- Umožnit konverzi do více formátů

### 3. **Uživatelské Nastavení**
- Možnost nastavit kvalitu JPG (0-100)
- Možnost změnit velikost obrázku

### 4. **Zpětná Vazba**
- Zobrazit zprávu o úspěšné konverzi
- Zobrazit chybové hlášky, pokud něco selže

---

## Příklad Vylepšeného Kódu (s Validací)

```python
def convert():
    global im1
    try:
        if 'im1' not in globals():
            print("Prosím, nejdříve vyberte PNG soubor!")
            return
        export_file_path = filedialog.asksaveasfilename(defaultextension='.jpg')
        if export_file_path:
            im1.save(export_file_path)
            print(f"Obrázek byl úspěšně uložen: {export_file_path}")
    except Exception as e:
        print(f"Chyba při konverzi: {e}")
```

---

## Závěr

Image Converter je jednoduchá, ale funkční aplikace pro konverzi obrázků. Jej základní struktura ji činí ideální pro začátečníky, kteří se chtějí naučit pracovat s GUI pomocí Tkinter a zpracování obrázků pomocí Pillow.
