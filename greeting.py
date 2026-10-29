""" Programm "Tervitus"
Kirjuta programm, mis küsib kasutajalt tema perekonnanime ja sugu (vali „m“ või „n“).
Programm tervitab kasutajat vastavalt soole:
Kui kasutaja valib „m“, väljasta: „Tere, härra [Perekonnanimi]!“
Kui kasutaja valib „n“, väljasta: „Tere, proua [Perekonnanimi]!“
Kui kasutaja sisestab midagi muud, väljasta: „Tere tulemast, [Perekonnanimi]! (sugu ei olegi tähtis).“ """

#Programmi algus
#Küsi kasutajalt perekonnanime
#küsi kasutajalt sugu ("m" või "n")
#Tervita vastavalt soole kas härra või proua.
#Kui "m" siis väljasta "Tere, härra [Perekonnanimi]!"
#Kui "n" siis väljasta "Tere, proua [Perekonnanimi]!"
#Lõpp


lastname = input("Mis on teie perekonnanimi?:")
sex = input("Mis on teie sugu? (m/n):")

if sex == "m":
    print(f"Tere, härra {lastname}!")
elif sex == "n":
    print(f"Tere, proua {lastname}!")
else:
    print(f"Tere tulemast, {lastname}!")






