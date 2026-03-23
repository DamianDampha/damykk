# Tento kód vytváří animaci spinneru pomocí knihovny turtle v Pythonu. Spinner se otáčí, když uživatel stiskne mezerník, a zobrazuje tři barevné tečky na konci ramen spinneru.
from turtle import *
state = {'turn': 0}

# definice funkce pro animaci spinneru, která se otáčí o úhel založený na hodnotě 'turn' v 'state' slovníku. 
# Funkce také kreslí tři barevné tečky (červenou, zelenou a modrou) na konci každé z tří ramen spinneru.

def spinner():
    clear()
    angle = state['turn']/10000
    right(angle)
    forward(100)
    dot(120, 'red')
    back(100)
    right(120)
    forward(100)
    dot(120, 'green')
    back(100)
    right(120)
    forward(100)
    dot(120, 'blue')
    back(100)
    right(120)
    update()
def animate():
    if state['turn']>0:
        state['turn']-=1

    spinner()
    ontimer(animate, 20)
def flick():
    state['turn']+=10000

# Nastavení okna a inicializace animace spinneru. Okno má rozměry 420x420 pixelů, a spinner se bude otáčet o 370 stupňů při každém stisknutí mezerníku.

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
width(20)
onkey(flick, 'space')
listen()
animate()
done()