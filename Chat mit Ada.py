import time
name = input("Wie heißt du? ")
time.sleep(2)
print(f"{name.title()}, was für ein schöner Name du hast!\n")
time.sleep(2)

age = input("Wie alt bist du? ")
if int(age) <= 20:
	print("Also immer noch voller Kraft!\n")
else:
	print("Du bist also in meinem Alter!\n")
	
time.sleep(2)
question = input("willst du fortfahren? ")
if question.lower() == "ja":
	print("Gerne!\n")
if question.lower() == "nein":
	print("Danke für deine Aufmerksamkeit!\n")
	

prompt = input("Hast du noch Fragen an mich?\n")
if prompt.lower() == "ja":
        print("Also machen wir weiter")
if prompt.lower() == "nein \n":
           print("ok!\n")("\n")

prompt = "Du kannst nach meinem Namen fragen. "
question2 = input(prompt)
if 'name' in question2.lower():
	print("Mein Name lautet Ada!")
else:
	print("\nVielen Dank für das Gespräch!")
