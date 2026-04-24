
import sys
from googletrans import Translator, LANGUAGES

def preloz_text():
    translator = Translator()
    
    print("--- Vítejte v aplikaci Překladač ---")
    print("Zadejte text, který chcete přeložit do angličtiny (nebo 'konec' pro ukončení):")
    
    while True:
        vstup = input("\nText k překladu: ")
        
        if vstup.lower() == 'konec':
            print("Děkuji za použití překladače. Nashledanou!")
            break
        
        try:
            # Automatická detekce jazyka a překlad do angličtiny (dest='en')
            vysledek = translator.translate(vstup, dest='en')
            
            print(f"Detekovaný jazyk: {LANGUAGES.get(vysledek.src, 'Neznámý').upper()}")
            print(f"Překlad (EN): {vysledek.text}")
            
        except Exception as e:
            print(f"Chyba při překladu: {e}")
            print("Ujistěte se, že máte nainstalovanou knihovnu 'googletrans==4.0.0-rc1' a jste připojeni k internetu.")

if __name__ == "__main__":
    preloz_text()
