#Zadanie 6 A

import random
droga = random.randint(1,1000)

srednie_spalanie = float(input("Podaj średnie spalanie samochodu (litry/100km): "))
cena_paliwa = float(input("Aktualna cena paliwa wynosi: "))

zuzycie_paliwa = round((droga/100)*srednie_spalanie,1)
koszta_podrozy = round(zuzycie_paliwa*cena_paliwa,2)

print(f"Samochód przejedzie {droga} km i zużyje {zuzycie_paliwa} litrów paliwa, a koszta podróży wyniosą {koszta_podrozy} zł.")