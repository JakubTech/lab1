#Zadanie 6
droga = float(input("Podaj drogę pokonaną przez samochód (w km): "))
srednie_spalanie = float(input("Podaj średnie spalanie samochodu (litry/100km): "))

zuzycie_paliwa = round((droga/100)*srednie_spalanie,1)
koszta_podrozy = round(zuzycie_paliwa*6.5,2)

print(f"Samochód zużyje {zuzycie_paliwa} litrów paliwa, a koszta podróży wyniosą {koszta_podrozy} zł.")