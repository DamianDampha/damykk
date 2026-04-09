def get_number(prompt):
    """Získá číslo od uživatele s kontrolou chyb."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Neplatné číslo. Zkuste to znovu.")

def get_operator():
    """Získá operátor od uživatele."""
    while True:
        operator = input("Zadejte operátor (+, -, *, /) nebo 'k' pro konec: ")
        if operator in ['+', '-', '*', '/', 'k']:
            return operator
        else:
            print("Neplatný operátor. Zkuste to znovu.")

def calculate(num1, operator, num2):
    """Provede výpočet na základě operátoru."""
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Chyba: Dělení nulou!"
        return num1 / num2

def main():
    """Hlavní funkce programu."""
    print("Vítejte v kalkulačce!")

    while True:
        num1 = get_number("Zadejte první číslo: ")
        operator = get_operator()

        if operator == 'k':
            print("Děkujeme za použití kalkulačky!")
            break

        num2 = get_number("Zadejte druhé číslo: ")
        result = calculate(num1, operator, num2)

        if isinstance(result, str):
            print(result)
        else:
            print(f"Výsledek: {num1} {operator} {num2} = {result}")
        print()  # Prázdný řádek pro lepší čitelnost

if __name__ == "__main__":
    main()
