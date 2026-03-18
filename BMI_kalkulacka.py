# Tenhle program vypočítá BMI (Body Mass Index) na základě zadané výšky a váhy uživatele a poskytne zpětnou vazbu o jeho zdravotním stavu.
Výška=float(input("Enter your height in centimeters: "))
Váha=float(input("Enter your Weight in Kg: "))
Výška = Výška/100
BMI=Váha/(Výška*Výška)
print("your Body Mass Index is: ",BMI)
if(BMI>0):
	if(BMI<=16):
		print("you are severely underweight")
	elif(BMI<=18.5):
		print("you are underweight")
	elif(BMI<=25):
		print("you are Healthy")
	elif(BMI<=30):
		print("you are overweight")
	else: print("you are severely overweight")
else:("enter valid details")Výška=float(input("Enter your height in centimeters: "))
