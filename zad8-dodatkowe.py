#równanie kwadratowe ax^2+bx+c=0
a = float(input("Podaj współczynnik a: "))
b = float(input("Podaj współczynnik b: "))
c = float(input("Podaj współczynnik c: "))

if a == 0:
    if b == 0:
        if c == 0:
            print("Równanie ma nieskończenie wiele rozwiązań.")
        else:
            print("Równanie sprzeczne, nie ma rozwiązań.")
    else:
        x = -c/b
        print(f"To jest równanie liniowe i rozwiązaniem jest x = {round(x,2)}.")
else:
    delta = b**2-(4*a*c)
    sqrt_delta = delta**(1/2)
    if delta > 0:
        x1 = (-b+sqrt_delta)/(2*a)
        x2 = (-b-sqrt_delta)/(2*a)
        print(f"Rozwiązaniem równania {a}x^2+{b}x+{c}=0 są x1 = {round(x1,2)} i x2 = {round(x2,2)}.")
    elif delta == 0:
        x0 = -b/ (2*a)
        print(f"Rozwiązaniem równania {a}x^2+{b}x+{c}=0 jest x0 = {round(x0,2)}.")
    else:
        print(f"Delta jest mniejsza od zera, równanie nie ma rozwiązań.")

