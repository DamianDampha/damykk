# Použiju knihovnu random pro generování náhodného čísla

import random

top_of_range = input("Napiš číslo: ")

# Kontrola, zda uživatel zadal číslo a jestli je větší než 0. Pokud ne, program se ukončí.

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Napiš číslo větší než 0.')
        quit()
else:
    print('Příště prosím napiš číslo.')
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

# Hlavní smyčka, která pokračuje, dokud neuhodne správné číslo.

while True:
    guesses += 1
    user_guess = input("Hádej : ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Příště prosím napiš číslo.')
        continue

    if user_guess == random_number:
        print("Dal jsi to!")
        break
    elif user_guess > random_number:
        print("Byl jsi nad číslem!")
    else:
        print("Byl jsi pod číslem!")

# Po uhádnutí čísla se vypíše, kolik pokusů uživatel potřeboval.

print("Dal jsi to za", guesses, "pokusů!")
