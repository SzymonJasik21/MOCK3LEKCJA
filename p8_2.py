def f(fnc, prods):
    # Wykonuje to samo co Twój kod, ale w jednej linii
    return ",".join(fnc(x) for x in prods)

if __name__ == "__main__":
    prods = ["water", "cheese", "tomato"]
    fnc2 = lambda x: (x[0] + x[-1]).upper()
    print(f(fnc2, prods)) # Wynik: WR,CE,TO