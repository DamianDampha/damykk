#!/usr/bin/env python3

"""Interaktivní textová hra: Únik z laboratoře."""


def clear_screen() -> None:
    # Vytiskne oddělovací řádek, aby se simulovalo vyčištění obrazovky.
    print("\n" + "=" * 60 + "\n")


def pause() -> None:
    # Pauzuje hru mezi scénami, dokud hráč nestiskne Enter.
    input("Stiskni Enter pro pokračování...")


def print_inventory(inventory: list[str]) -> None:
    clear_screen()
    print("Tvůj inventář:")
    if inventory:
        for item in inventory:
            print(f" - {item}")
    else:
        print(" - Prázdný")
    print()


def ask_option(options: dict[str, str]) -> str:
    # Zobrazí hráčovy možnosti a vrátí výběr.
    # Vrací speciální příkazy "inventory" a "quit" pro zpracování inventáře a ukončení.
    while True:
        for key, text in options.items():
            print(f" {key}) {text}")
        choice = input("Vyber číslo nebo příkaz (i = inventář, q = konec): ").strip().lower()
        if choice == "i":
            return "inventory"
        if choice == "q":
            return "quit"
        if choice in options:
            return choice
        print("Neplatná volba. Zkus to prosím znovu.")


def intro() -> None:
    # Úvodní obrazovka hry s vysvětlením cíle a ovládání.
    clear_screen()
    print("Únik z laboratoře")
    print("Vítej v dobrodružné hře, kde musíš uniknout z tajné laboratoře.")
    print("Prozkoumávej místnosti, sbírej předměty a vyřeš hádanky.")
    print("\nTip: V každé místnosti můžeš napsat i, abys zobrazil inventář.")
    pause()


def laboratory(state: dict) -> None:
    # Laboratoř je výchozí scéna. Hráč zde sbírá klíč, přívěsek a odemyká počítač.
    clear_screen()
    print("Jsi v laboratoři. Vše je pokryté papíry, chemikáliemi a monitor monitoru bliká.")
    print("Dveře vedou do chodby, ale jsou zamčené. K úniku budeš potřebovat klíč nebo kód.")
    options = {
        "1": "Prozkoumat pracovní stůl",
        "2": "Otevřít kovovou skříň",
        "3": "Jít do chodby",
        "4": "Prozkoumat počítač"
    }
    choice = ask_option(options)
    if choice == "inventory":
        print_inventory(state["inventory"])
        pause()
        laboratory(state)
        return
    if choice == "quit":
        state["game_over"] = True
        return
    if choice == "1":
        clear_screen()
        if "přívěsek" in state["inventory"]:
            print("Už jsi stůl prozkoumal a našel jsi všechno, co zde bylo.")
        else:
            print("Na stole leží starý přívěsek s tajemným nápisem a šroubovák.")
            state["inventory"].append("přívěsek")
            state["inventory"].append("šroubovák")
            print("Přidal jsi do inventáře přívěsek a šroubovák.")
        pause()
    elif choice == "2":
        clear_screen()
        if "klíč" in state["inventory"]:
            print("Skříň je prázdná, už jsi z ní vzal klíč.")
        else:
            print("Uvnitř skříně se nachází malý klíč, který může otevřít dveře.")
            state["inventory"].append("klíč")
            print("Vzali jste klíč do inventáře.")
        pause()
    elif choice == "3":
        state["location"] = "corridor"
        return
    elif choice == "4":
        clear_screen()
        if state["computer_unlocked"]:
            print("Počítač je odemčený. Zadání kódu je možné zkusit u východu.")
        else:
            print("Monitor zobrazuje zprávu: 'Hledáš kód? Zkus nechápeš slova, ale zvuky.'")
            print("Vyskytuje se soubor s názvem 'notatky.txt'.")
            # Poznámka u počítače znamená, že hráč získal nápovědu ke kódu.
            state["computer_unlocked"] = True
        pause()


def corridor(state: dict) -> None:
    # Chodba propojuje laboratoř, sklad a východ. Volba mění aktuální lokaci.
    clear_screen()
    print("Jsi na chodbě. Vpravo je sklad, vlevo jsou dveře vedoucí k východu.")
    options = {
        "1": "Jít do skladu",
        "2": "Podívat se na dveře k východu",
        "3": "Vrátit se do laboratoře"
    }
    choice = ask_option(options)
    if choice == "inventory":
        print_inventory(state["inventory"])
        pause()
        corridor(state)
        return
    if choice == "quit":
        state["game_over"] = True
        return
    if choice == "1":
        state["location"] = "supply"
        return
    if choice == "2":
        state["location"] = "exit_door"
        return
    if choice == "3":
        state["location"] = "laboratory"
        return


def supply_room(state: dict) -> None:
    # Sklad má zásuvku, kterou můžeš prozkoumat a získat baterku.
    clear_screen()
    print("Vcházíš do skladu. Police jsou plné krabic, ale jedna zásuvka je otevřená.")
    options = {
        "1": "Prozkoumat zásuvku",
        "2": "Vrátit se do chodby"
    }
    choice = ask_option(options)
    if choice == "inventory":
        print_inventory(state["inventory"])
        pause()
        supply_room(state)
        return
    if choice == "quit":
        state["game_over"] = True
        return
    if choice == "1":
        clear_screen()
        if "baterka" in state["inventory"]:
            print("Zásuvka je prázdná. Nic už zde není.")
        else:
            print("Uvnitř zásuvky je baterka. Je to užitečné světlo pro tmavé chodby.")
            state["inventory"].append("baterka")
        pause()
    elif choice == "2":
        state["location"] = "corridor"
        return


def exit_door(state: dict) -> None:
    # V lokaci východu může hráč použít klíč nebo zadat kód.
    clear_screen()
    print("Stojíš před dveřmi k východu. Na zámku je malý displej a klíčová dírka.")
    options = {
        "1": "Použít klíč na zámek",
        "2": "Zkusit zadat kód",
        "3": "Vrátit se na chodbu"
    }
    choice = ask_option(options)
    if choice == "inventory":
        print_inventory(state["inventory"])
        pause()
        exit_door(state)
        return
    if choice == "quit":
        state["game_over"] = True
        return
    if choice == "1":
        clear_screen()
        if "klíč" in state["inventory"]:
            print("Použil jsi klíč. Dveře se pomalu otevírají.")
            state["escaped"] = True
        else:
            print("Nemáš klíč. Dveře zůstávají zamčené.")
        pause()
    elif choice == "2":
        clear_screen()
        print("Na displeji se objevují otázky. Můžeš zadat čtyřmístný kód.")
        code = input("Zadej kód: ").strip()
        if code == state["secret_code"]:
            print("Kód je správný! Dveře se otevřou.")
            state["escaped"] = True
        else:
            print("Kód je špatný. Displej zamrzl jen na chvíli.")
            if state["computer_unlocked"] and "přívěsek" in state["inventory"]:
                # Zobrazení této nápovědy závisí na předchozím průzkumu počítače a přívěsku.
                print("Všiml jsi si, že přívěsek je naladěný na tóny 7-4-0-2.")
        pause()
    elif choice == "3":
        state["location"] = "corridor"
        return


def game_loop() -> None:
    # Hlavní smyčka spouští jednotlivé scény podle stavu hry.
    state = {
        "location": "laboratory",
        "inventory": [],
        "computer_unlocked": False,
        "secret_code": "7402",
        "escaped": False,
        "game_over": False
    }
    intro()
    while not state["game_over"] and not state["escaped"]:
        if state["location"] == "laboratory":
            laboratory(state)
        elif state["location"] == "corridor":
            corridor(state)
        elif state["location"] == "supply":
            supply_room(state)
        elif state["location"] == "exit_door":
            exit_door(state)
        else:
            # Pokud nastane neočekávaná hodnota lokace, vrátíme hráče do laboratoře.
            state["location"] = "laboratory"
    clear_screen()
    if state["escaped"]:
        print("Gratuluji! Úspěšně jsi unikl z laboratoře.")
        if "baterka" in state["inventory"]:
            print("Světlo tvé baterky ti pomohlo projít tmavými chodbami.")
    else:
        print("Hra byla ukončena. Přijď znovu a dokonči únik.")


def main() -> None:
    # Vstupní bod programu. Zachytí stisknutí Ctrl+C a ukončí hru hezky.
    try:
        game_loop()
    except KeyboardInterrupt:
        print("\nHra přerušena. Ulož si své nápady a vrať se později.")


if __name__ == "__main__":
    main()
