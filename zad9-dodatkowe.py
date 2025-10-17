#kalkulator

pierwsza_liczba = float(input("Podaj pierwszą liczbę: "))
druga_liczba = float(input("Podaj drugą liczbę: "))

print(f"Dodawanie: {pierwsza_liczba} + {druga_liczba} = {pierwsza_liczba+druga_liczba}")
print(f"Odejmowanie: {pierwsza_liczba} - {druga_liczba} = {pierwsza_liczba-druga_liczba}")
print(f"Mnożenie: {pierwsza_liczba} * {druga_liczba} = {pierwsza_liczba*druga_liczba}")
if druga_liczba == 0:
    print("Dzielenie nie możliwe, druga liczba nie może być zerem.")
else:
    print(f"Dzielenie: {pierwsza_liczba} : {druga_liczba} = {round(pierwsza_liczba/druga_liczba,2)}")
print(f"Potęgowanie: {pierwsza_liczba} ^ {druga_liczba} = {pierwsza_liczba**druga_liczba}")
