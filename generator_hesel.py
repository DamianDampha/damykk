import random
import string

def generuj_heslo(delka=16):
    # Definice znaků, které chceme použít
    pismena = string.ascii_letters  # malá i velká
    cisla = string.digits           # 0-9
    symboly = string.punctuation    # !@#$%...
    
    vsechny_znaky = pismena + cisla + symboly
    
    # Náhodný výběr znaků
    heslo = "".join(random.choice(vsechny_znaky) for _ in range(delka))
    return heslo

def main():
    print("--- GENERÁTOR BEZPEČNÝCH HESEL ---")
    try:
        vstup = input("Zadej délku hesla (nebo nechej prázdné pro 16 znaků): ")
        delka = int(vstup) if vstup.strip() else 16
        
        nove_heslo = generuj_heslo(delka)
        
        print("\n" + "="*30)
        print(f"Vaše heslo: {nove_heslo}")
        print("="*30)
        
    except ValueError:
        print("Chyba: Musíš zadat celé číslo!")

if __name__ == "__main__":
    main()
  
