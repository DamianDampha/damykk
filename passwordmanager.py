master_pwd = input("Co je vaše hlavní heslo ? ")

def view():
     with open("hesla.txt", "r") as f:
        for line in f.readlines():
            print(line.strip())
            user, passw = data.split ("|")
            print("Název účtu: ", user, " | Heslo: ", passw)
def add():
    pass
    name = input("Název účtu: ")
    pwd = input("Heslo: ")
    
    with open("hesla.txt", "a") as f:
        f.write(name + "|" + pwd + "\n")

while True:
    mode = input("Chcete přidat nové heslo nebo si jej zobrazit ? (zobrazit/přidat) ").lower()
    if mode == "zobrazit":
        view()
    elif mode == "přidat" :
        add()
else:
    print("Neplatný režim!")
