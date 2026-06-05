import random
import json
import os

# Výchozí ceny kryptoměn a hotovost
SOUBOR_DAT = "crypto_data.json"
TRH = {
    "BTC": 65000.0,
    "ETH": 3500.0,
    "SOL": 150.0
}

def nacti_data():
    if os.path.exists(SOUBOR_DAT):
        with open(SOUBOR_DAT, "r") as f:
            return json.load(f)
    return {"USD": 10000.0, "BTC": 0.0, "ETH": 0.0, "SOL": 0.0}

def uloz_data(data):
    with open(SOUBOR_DAT, "w") as f:
        json.dump(data, f, indent=4)

def aktualizuj_trh():
    print("\n--- TRH SE AKTUALIZUJE (Ceny se pohnuly) ---")
    for krypto in TRH:
        # Simulace změny ceny o -10% až +10%
        zmena = random.uniform(-0.10, 0.10)
        TRH[krypto] = round(TRH[krypto] * (1 + zmena), 2)
        smer = "📈" if zmena > 0 else "📉"
        print(f"{smer} {krypto}: {TRH[krypto]} USD ({zmena*100:+.2f}%)")

def ukaz_penezenku(data):
    print("\n=====================================")
    print("         TVÁ CRYPTO PENĚŽENKA        ")
    print("=====================================")
    print(f"Hotovost: {data['USD']:.2f} USD")
    celkova_hodnota = data['USD']
    
    for krypto, mnozstvi in data.items():
        if krypto != "USD" and mnozstvi > 0:
            hodnota = mnozstvi * TRH[krypto]
            celkova_hodnota += hodnota
            print(f"{krypto}: {mnozstvi:.4f} (Hodnota: {hodnota:.2f} USD)")
            
    print("-------------------------------------")
    print(f"CELKOVÁ HODNOTA PORTFOLIA: {celkova_hodnota:.2f} USD")
    print("=====================================")

def nakup(data):
    print("\nDostupné mince k nákupu:")
    for krypto, cena in TRH.items():
        print(f"- {krypto}: {cena} USD")
        
    volba = input("Kterou minci chceš koupit? (BTC/ETH/SOL): ").upper()
    if volba not in TRH:
        print("[!] Neplatná mince.")
        return
        
    try:
        castka_usd = float(input(f"Za kolik USD chceš koupit {volba}? (Máš {data['USD']:.2f} USD): "))
        if castka_usd <= 0:
            print("[!] Částka musí být větší než 0.")
            return
        if castka_usd > data["USD"]:
            print("[!] Nedostatek hotovosti!")
            return
            
        mnozstvi = castka_usd / TRH[volba]
        data["USD"] -= castka_usd
        data[volba] += mnozstvi
        uloz_data(data)
        print(f">> Úspěšně koupeno {mnozstvi:.4f} {volba} za {castka_usd:.2f} USD.")
    except ValueError:
        print("[!] Zadej platné číslo.")

def prodej(data):
    volba = input("\nKterou minci chceš prodat? (BTC/ETH/SOL): ").upper()
    if volba not in TRH or data.get(volba, 0) == 0:
        print("[!] Tuto minci nevlastníš nebo neexistuje.")
        return
        
    try:
        mnozstvi_k_prodeji = float(input(f"Kolik {volba} chceš prodat? (Máš {data[volba]:.4f}): "))
        if mnozstvi_k_prodeji <= 0:
            print("[!] Množství musí být větší než 0.")
            return
        if mnozstvi_k_prodeji > data[volba]:
            print("[!] Nemáš dostatek mincí!")
            return
            
        zisk_usd = mnozstvi_k_prodeji * TRH[volba]
        data[volba] -= mnozstvi_k_prodeji
        data["USD"] += zisk_usd
        uloz_data(data)
        print(f">> Úspěšně prodáno {mnozstvi_k_prodeji:.4f} {volba} za {zisk_usd:.2f} USD.")
    except ValueError:
        print("[!] Zadej platné číslo.")

def hlavni_menu():
    data = nacti_data()
    while True:
        print("\n1. Zobrazit peněženku a aktuální ceny")
        print("2. Nakoupit kryptoměnu")
        print("3. Prodat kryptoměnu")
        print("4. Počkat (Aktualizovat ceny na trhu)")
        print("5. Konec")
        
        volba = input("Vyber možnost (1-5): ").strip()
        
        if volba == "1":
            ukaz_penezenku(data)
        elif volba == "2":
            nakup(data)
        elif volba == "3":
            prodej(data)
        elif volba == "4":
            aktualizuj_trh()
        elif volba == "5":
            print("\nDíky za hru! Tvoje portfolio bylo uloženo.")
            break
        else:
            print("[!] Neplatná volba.")

if __name__ == "__main__":
    hlavni_menu()