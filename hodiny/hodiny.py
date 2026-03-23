#Digitální hodiny v Pythonu pomocí Tkinter

from tkinter import Label, Tk 
import time

# Vytvoření hlavního okna aplikace

app_window = Tk() 
app_window.title("Digital Clock") 
app_window.geometry("420x150") 
app_window.resizable(1,1)

# Nastavení fontu, barvy pozadí, barvy textu a šířky okraje pro zobrazení hodin

text_font= ("Boulder", 68, 'bold')
background = "#f2e750"
foreground= "#363529"
border_width = 25

# Vytvoření štítku pro zobrazení času a umístění do mřížky

label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width) 
label.grid(row=0, column=1)

# Funkce pro aktualizaci času na štítku každých 200 milisekund

def digital_clock(): 
   time_live = time.strftime("%H:%M:%S")
   label.config(text=time_live) 
   label.after(200, digital_clock)

digital_clock()
app_window.mainloop()