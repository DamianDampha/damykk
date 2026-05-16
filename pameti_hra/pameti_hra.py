import os
import random
import time


def clear_screen() -> None:
    """Vyčistí obrazovku konzole pro Windows i unixové systémy."""
    os.system("cls" if os.name == "nt" else "clear")


def generate_sequence(length: int) -> str:
    """Vygeneruje náhodnou číselnou sekvenci dané délky."""
    return "".join(str(random.randint(1, 9)) for _ in range(length))


def show_sequence(sequence: str) -> None:
    """Zobrazí sekvenci hráči, počká chvíli a poté obrazovku vymaže."""
    print("Paměťová sekvence:", sequence)
    time.sleep(2 + len(sequence) * 0.5)
    print("\nPamatujte si ji a stiskněte Enter, až budete připraveni...")
    input()
    clear_screen()


def get_player_answer(length: int) -> str:
    """Požádá hráče o zadání sekvence stejné délky."""
    while True:
        answer = input(f"Zadejte sekvenci {length} číslic: ").strip()
        if len(answer) != length or not answer.isdigit():
            print(f"Neplatný vstup. Zadejte přesně {length} číslic (1-9).")
            continue
        return answer


def display_results(level: int, highest: int) -> None:
    """Zobrazí aktuální skóre a nejlepší dosaženou úroveň."""
    print(f"\nSprávně! Postupujete na další úroveň.")
    print(f"Aktuální úroveň: {level}")
    print(f"Nejvyšší úroveň: {highest}")


def main() -> None:
    print("=== Paměťová hra ===")
    print("Zapamatujte si sekvenci číslic a zopakujte ji ve správném pořadí.")
    print("Každá správná odpověď prodlužuje sekvenci o další číslici.")
    print("Stiskněte Enter pro začátek...")
    input()

    level = 1
    highest_level = 1

    while True:
        clear_screen()
        sequence = generate_sequence(level)
        show_sequence(sequence)
        answer = get_player_answer(level)

        if answer == sequence:
            highest_level = max(highest_level, level)
            display_results(level, highest_level)
            level += 1
            time.sleep(1.5)
        else:
            print("\nŠpatně. Hra končí.")
            print(f"Správná sekvence byla: {sequence}")
            print(f"Dosáhli jste úrovně: {level}")
            print(f"Nejlepší úroveň v tomto běhu: {highest_level}")
            break

    print("\nDěkujeme za hraní paměťové hry!")


if __name__ == "__main__":
    main()
