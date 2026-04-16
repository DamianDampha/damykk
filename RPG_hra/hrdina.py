# hrdina.py — třída pro hráčovu postavu

class Hrdina:
    def __init__(self, jmeno):
        self.jmeno = jmeno
        self.hp = 100
        self.max_hp = 100
        self.utok = 15
        self.obrana = 5
        self.level = 1
        self.xp = 0
        self.xp_limit = 100

    def utoc(self, nepritel):
        poskozeni = max(1, self.utok - nepritel.obrana)
        nepritel.hp -= poskozeni
        print(f"{self.jmeno} útočí za {poskozeni} poškození!")

    def pij_lektvar(self):
        heal = 30
        self.hp = min(self.max_hp, self.hp + heal)
        print(f"Vypil jsi lektvar a obnovil sis {heal} HP!")

    def ziskej_xp(self, xp):
        self.xp += xp
        print(f"Získal jsi {xp} XP!")
        if self.xp >= self.xp_limit:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.xp -= self.xp_limit
        self.xp_limit = int(self.xp_limit * 1.5)
        self.max_hp += 20
        self.hp = self.max_hp
        self.utok += 5
        print(f"LEVEL UP! Jsi teď level {self.level}! HP a útok zvýšeny.")

    def je_nazivu(self):
        return self.hp > 0

    def __str__(self):
        return (
            f"--- {self.jmeno} | Level {self.level} ---\n"
            f"HP: {self.hp}/{self.max_hp} | Útok: {self.utok} | XP: {self.xp}/{self.xp_limit}"
        )