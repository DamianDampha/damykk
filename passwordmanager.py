from cryptography.fernet import Fernet

"""
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)"""
        

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


master_pwd = input("Co je vaše hlavní heslo ? ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

"""
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)"""


def view():
     with open("passwords.txt", "r") as f:
        for line in f.readlines():
            print(line.strip())
            user, passw = data.split ("|")
            print("Název účtu: ", user, " | Heslo: ", str(fer.decrypt(passw.encode())))

def add():
    pass
    name = input("Název účtu: ")
    pwd = input("Heslo: ")
    
    with open("passwords.txt", "a") as f:
        f.write(name + "|" + str(fer.encrypt(pwd.encode())) + "\n")

while True:
    mode = input("Chcete přidat nové heslo nebo si jej zobrazit ? (zobrazit/přidat) ").lower()
    if mode == "zobrazit":
        view()
    elif mode == "přidat" :
        add()
else:
    print("Neplatný režim!")
