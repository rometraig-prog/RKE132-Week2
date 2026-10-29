""" Programm "Veejoomise kalkulaator"
Arstid soovitavad juua päevas 2 liitrit vett.
Kirjuta programm, mis küsib kasutajalt, kui palju klaase vett ta juba joonud on. Oletame, et üks klaas = 250 ml.
Programm arvutab, mitu protsenti päevanormist on täidetud, ja annab tagasisidet:
Kui protsent < 50: väljasta: „Joo rohkem vett, keha vajab seda!“
Kui protsent < 100: väljasta: „Tubli, jätka samas vaimus!“
Kui protsent ≥ 100: väljasta: „Suurepärane, oled oma päevase eesmärgi täitnud!“ """


#Alustame programmiga
#Tervita 
#Kirjuta "Arstid soovitavad juua päevas 2 liitrit vett."
#küsi kui palju klaase vett ta juba joonud on. Oletame, et üks klaas = 250 ml.
#Arvutab, mitu protsenti päevanormist on täidetud, ja annab tagasisidet:
#Kui protsent < 50: väljasta: „Joo rohkem vett, keha vajab seda!“
#Kui protsent < 100: väljasta: „Tubli, jätka samas vaimus!“
#Kui protsent ≥ 100: väljasta: „Suurepärane, oled oma päevase eesmärgi
#Lõpp


print("Tervitus, See on veejoomise kalkulaator!")
print("Arstid soovitavad juua päevas 2 liitrit vett.")

goal = 2000
glass_ml = 250

glass = int(input("Mitu klaasi vett olete te joonud? Oletame, et üks klaas on 250 ml."))

water = (glass_ml * glass)
percent = (water * 100 / goal)

if percent < 50:
    print("Joo rohkem vett, keha vajab seda!")
elif percent < 100:
    print("Tubli, jätka samas vaimus!")
elif percent >= 100:
    print("Suurepärane, oled oma päevase eesmärgi!")

