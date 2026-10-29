""" kirjutame koos programmi, mis küsib kasutajalt, mis päev on homme (tööpäev või puhkepäev), ning väljastab põhjal sobiva sõnumi.
kasutaja sisestab ühe sõna
"tööpäev"
või "puhkepäev". 
Kui sisestus on "tööpäev", siis kuvatakse ekraanile tekst:
Ma lähen magama, head ööd!
Kui sisestus on "puhkepäev": kuvagtakse ekraanile tekst:
Veel üks osa Netflixist!
 """
#Alustame programmi.
#Küsi kasutajalt: "Mis päev on homme? (tööpäev/puhkepäev)".
#Salvesta vastus muutujasse day.
#Kui day on võrdne sõnadega "tööpäev", siis väljasta ekraanile: "Ma lähen magama, head ööd!".
#Muidu, kui day on võrdne sõnaga "puhkepäev", siis väljasta ekraanile: "Veel üks osa Netflixist".
#Muidu (kui sisestus ei olnud õige),siis väljasta ekraanile: "Vale väärtus".
#Lõpeta programm.


""" day = input("Mis päev on homme? (tööpäev/puhkepäev):")

if day == "tööpäev":
    print("Ma lähen magama, head ööd!")
elif day == "puhkepäev":
    print("Veel üks osa Netflixist!")
else:
    print("Vale väärtus") """



#Finantsnõustaja
""" Sa tahad osta endale uue iphone 17 pro, aga sa oled otsustanud, et krediiti sa ei võta. Selle asemel oled sa palganud range ja vastutustundliku fintantsnõustaja programmi kujul.
See programm:
- küsib, kui palju sul on praegu raha,
-võrdleb seda iphone 17 pro hinnaga (näiteks 2 500 €)
- ja annab sulle täiesti ratsionaalse, emotsioonideta soovituse.  """

""" print("Tere tulemast programmi 'Finantsnõustaja'!")
print("Sinu isiklik nõustaja ei tee emotsionaalseid oste.")

money = int(input("Kui palju raha sul praegu on?"))

if money < 2500:
    print("Sul pole veel piisavalt raha. Ole kannatlik ja kogu edasi!")
elif money == 2500:
    print("Palju õnne, saad osta uue iphone 17 pro sularahas!")
else:
    print("Saad osta iphone 17 pro ja veel jääb raha üle.") """


#Sammulugeja

""" Sul on eesmärk teha iga päev 10 000 sammu. Programm küsib kasutajalt, mitu sammu ta on juba teinud, arvutab täitmise protsendi ja annab tagasisidet.
- Kui protsent < 50: "Alles poolel teel, liigu edasi!"
- Kui protsent < 75: "Tubli, oled peaaegu kohal!"
- Kui protsent <= 100: "Palju õnne, oled oma eesmärgi täitnud!" 
"""

""" goal = 10000
steps = int(input("Mitu sammu oled kuba teinud?:"))

percent = (steps/goal) * 100

print(f"{percent}%")

if percent < 50:
    print("Alles poolel teel, liigu edasi!")
elif percent < 75:
    print("Tubli, oled peaaegu kohal!")
elif percent <100:
    print("Suurepärane, oled peaaegu kohal!")
else:
    print("Palju õnne, oled oma eesmärgi täitnud!") """