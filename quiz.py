print("Vítejte v mojem quizu o počítačích!")

hraje = input("Chcete si zahrát ? ")

if hraje.lower() !="ano":
    quit()

print("Tak jdeme na to! ")
score = 0
odpověd = input("Co znaméná zkratka CPU ? ")
if odpověd.lower() == "central processing unit":
    print("Správně!")
    score += 1
else:
    print("Špatně")


odpověd = input("Co znamená zkratka GPU ? ")
if odpověd.lower() == "graphics processing unit":
    print("Správně!")
    score += 1
else:
    print("Špatně")


odpověd = input("Co znamená zkratka RAM ? ")
if odpověd.lower() == "random access memory":
    print("Správně!")
    score += 1
else:
    print("Špatně")


odpověd = input("Kdy byl vynalezen první počítač ? ")
if odpověd.lower() == "1970":
    print("Správně!")
    score += 1
else:
    print("Špatně")


odpověd = input("Co drží všechny komponenty pohromadě ? ")
if odpověd.lower() == "základní deska":
    print("Správně!")
    score += 1
else:
    print("Špatně")

odpověd = input("Co vlastně znamená PC ? ")
if odpověd.lower() == "personal computer":
    print("Správně!")
    score += 1
else:
    print("Špatně")


odpověd = input("V jakém programovacím jazyce je Instagram ? ")
if odpověd.lower() == "python":
    print("Správně!")
    score += 1
else:
    print("Špatně")



odpověd = input("Co je nejlepší kabel pro připojení monitoru do PC ? ")
if odpověd.lower() == "displayport":
    print("Správně!")
    score += 1
else:
    print("Špatně")


print("Uhodle si " + str(score) + " správně!")
print("Máš " + str((score / 8 ) * 100) + "% otázek správně")