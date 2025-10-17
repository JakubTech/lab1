#równanie liniowe ax+b=0

a = float(input("Podaj współczynnik a: "))
b = float(input("Podaj współczynnik b: "))

if a == 0:
    if b == 0:
        print("Równanie ma nieskończenie wiele rozwiązań.")
    else:
        print("Równanie sprzeczne, nie ma rozwiązania.")
else:
    x = -b/a #przestawiamy b na drugą stronę i dzielimy całe równanie przez a
    print(f"Rozwiązaniem równania {a}x+{b}=0 jest {x}.")