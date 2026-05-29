def vypocitej_ohm():
    print("\n--- Výpočet Ohmova zákona ---")
    print("Zadej hodnoty, které znáš. Pro neznámou hodnotu zadej '?'")
    
    u = input("Zadej napětí U (V): ")
    i = input("Zadej proud I (A): ")
    r = input("Zadej odpor R (Ω): ")

    try:
        if u == "?":
            vysledek = float(i) * float(r)
            print(f"\n>> Vypočítané napětí U = {vysledek} V")
        elif i == "?":
            vysledek = float(u) / float(r)
            print(f"\n>> Vypočítaný proud I = {vysledek} A")
        elif r == "?":
            vysledek = float(u) / float(i)
            print(f"\n>> Vypočítaný odpor R = {vysledek} Ω")
        else:
            print("\n[!] Nezadali jste žádnou neznámou (?) nebo jsou zadané hodnoty špatně.")
    except ValueError:
        print("\n[!] Chyba: Zadávejte pouze čísla nebo '?'!")
    except ZeroDivisionError:
        print("\n[!] Chyba: Nulou nelze dělit!")

def vypocitej_odpory():
    print("\n--- Spojování odporů ---")
    print("1. Sériové zapojení (za sebou)")
    print("2. Paralelní zapojení (vedle sebe)")
    volba = input("Vyber typ zapojení (1/2): ")
    
    try:
        r1 = float(input("Zadej hodnotu R1 (Ω): "))
        r2 = float(input("Zadej hodnotu R2 (Ω): "))
        
        if volba == "1":
            celkovy_r = r1 + r2
            print(f"\n>> Celkový odpor v sérii R = {celkovy_r} Ω")
        elif volba == "2":
            if r1 + r2 == 0:
                print("\n[!] Chyba: Odpory nemohou být nulové.")
                return
            celkovy_r = (r1 * r2) / (r1 + r2)
            print(f"\n>> Celkový odpor paralelně R = {celkovy_r} Ω")
        else:
            print("\n[!] Neplatná volba zapojení.")
    except ValueError:
        print("\n[!] Chyba: Zadávejte pouze čísla!")

def hlavni_menu():
    while True:
        print("\n=============================")
        print("    ELEKTRO POMOCNÍK v1.0    ")
        print("=============================")
        print("1. Výpočet Ohmova zákona (U, I, R)")
        print("2. Výpočet výsledného odporu (R1, R2)")
        print("3. Konec")
        
        volba = input("Vyber možnost (1-3): ")
        
        if volba == "1":
            vypocitej_ohm()
        elif volba == "2":
            vypocitej_odpory()
        elif volba == "3":
            print("\nDíky za použití programu. Ať se daří v elektru!")
            break
        else:
            print("\n[!] Neplatná volba, zkus to znovu.")

if __name__ == "__main__":
    hlavni_menu()