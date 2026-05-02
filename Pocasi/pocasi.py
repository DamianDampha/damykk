"""
pocasnik.py — simulátor počasí pro různá města
Nepotřebuje žádné API klíče, data jsou fiktivní.
"""

import random
import datetime


MESTA = {
    "Praha":    {"zima": (-5, 3),  "jaro": (8, 18),  "leto": (20, 32), "podzim": (5, 15)},
    "Brno":     {"zima": (-6, 2),  "jaro": (9, 19),  "leto": (21, 33), "podzim": (4, 14)},
    "Ostrava":  {"zima": (-7, 1),  "jaro": (7, 17),  "leto": (19, 31), "podzim": (3, 13)},
    "Plzen":    {"zima": (-4, 4),  "jaro": (8, 18),  "leto": (20, 31), "podzim": (5, 14)},
    "Liberec":  {"zima": (-8, 0),  "jaro": (6, 16),  "leto": (18, 29), "podzim": (3, 12)},
    "Olomouc":  {"zima": (-5, 3),  "jaro": (9, 19),  "leto": (21, 32), "podzim": (4, 14)},
}

STAVY = ["Jasno", "Polojasno", "Zatazeno", "Dést", "Snízení", "Bouřka", "Mlha"]

STAVY_VAHA = {
    "zima":   [10, 15, 25, 10, 25, 5, 10],
    "jaro":   [20, 25, 20, 20, 0,  10, 5],
    "leto":   [30, 30, 15, 10, 0,  15, 0],
    "podzim": [10, 20, 30, 25, 0,  5,  10],
}


def get_rocni_obdobi(mesic: int) -> str:
    if mesic in (12, 1, 2):
        return "zima"
    elif mesic in (3, 4, 5):
        return "jaro"
    elif mesic in (6, 7, 8):
        return "leto"
    else:
        return "podzim"


def generuj_pocasi(mesto: str, datum: datetime.date) -> dict:
    obdobi = get_rocni_obdobi(datum.month)
    rozsah = MESTA[mesto][obdobi]
    teplota = round(random.uniform(*rozsah), 1)
    stav = random.choices(STAVY, weights=STAVY_VAHA[obdobi])[0]
    vlhkost = random.randint(40, 95)
    victr = random.randint(0, 60)
    return {
        "město": mesto,
        "datum": datum.strftime("%d.%m.%Y"),
        "teplota": teplota,
        "stav": stav,
        "vlhkost": vlhkost,
        "vítr": victr,
        "období": obdobi,
    }


def vytiskni_pocasi(data: dict):
    sep = "─" * 36
    print(sep)
    print(f"  {data['město']}  |  {data['datum']}")
    print(sep)
    print(f"  Teplota  : {data['teplota']:>6.1f} °C")
    print(f"  Stav     : {data['stav']}")
    print(f"  Vlhkost  : {data['vlhkost']:>6} %")
    print(f"  Vítr     : {data['vítr']:>6} km/h")
    print(f"  Období   : {data['období'].capitalize()}")
    print(sep)


def predpoved(mesto: str, dni: int):
    print(f"\nPředpověď pro {mesto} na {dni} dní:")
    dnes = datetime.date.today()
    for i in range(dni):
        datum = dnes + datetime.timedelta(days=i)
        data = generuj_pocasi(mesto, datum)
        ikona = {
            "Jasno": "☀", "Polojasno": "⛅", "Zatazeno": "☁",
            "Dést": "🌧", "Snízení": "❄", "Bouřka": "⛈", "Mlha": "🌫",
        }.get(data["stav"], "?")
        print(f"  {datum.strftime('%a %d.%m.')}  {ikona}  {data['stav']:<12} {data['teplota']:>5.1f} °C")


def porovnej_mesta(dni: int = 1):
    print(f"\nPorovnání měst — průměr za {dni} dní:")
    dnes = datetime.date.today()
    vysledky = []
    for mesto in MESTA:
        teploty = []
        for i in range(dni):
            datum = dnes + datetime.timedelta(days=i)
            data = generuj_pocasi(mesto, datum)
            teploty.append(data["teplota"])
        prumer = round(sum(teploty) / len(teploty), 1)
        vysledky.append((mesto, prumer))
    vysledky.sort(key=lambda x: x[1], reverse=True)
    for i, (mesto, prumer) in enumerate(vysledky, 1):
        print(f"  {i}. {mesto:<10} {prumer:>5.1f} °C")


def hlavni_menu():
    print("\n╔══════════════════════════════╗")
    print("║       POČASNÍK v1.0          ║")
    print("╚══════════════════════════════╝")

    while True:
        print("\nCo chceš udělat?")
        print("  1 — Aktuální počasí pro město")
        print("  2 — Předpověď na 5 dní")
        print("  3 — Porovnat všechna města")
        print("  4 — Konec")

        volba = input("\nVyber (1-4): ").strip()

        if volba == "1":
            print("\nDostupná města:", ", ".join(MESTA.keys()))
            mesto = input("Zadej město: ").strip().capitalize()
            if mesto not in MESTA:
                print(f"Město '{mesto}' neznám.")
            else:
                data = generuj_pocasi(mesto, datetime.date.today())
                vytiskni_pocasi(data)

        elif volba == "2":
            print("\nDostupná města:", ", ".join(MESTA.keys()))
            mesto = input("Zadej město: ").strip().capitalize()
            if mesto not in MESTA:
                print(f"Město '{mesto}' neznám.")
            else:
                predpoved(mesto, 5)

        elif volba == "3":
            porovnej_mesta(dni=7)

        elif volba == "4":
            print("Nashledanou!")
            break

        else:
            print("Neplatná volba, zkus 1–4.")


if __name__ == "__main__":
    hlavni_menu()