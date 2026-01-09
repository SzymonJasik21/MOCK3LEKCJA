def f(fnc,prods):
    string = ""

    for x in prods:
        string = string + ","+fnc(x)
    
    return string.lstrip(",")


if __name__ == "__main__":
    print(f(lambda x: (x[0]+x[-1]).upper(), ["water","cheese","tomato"]))
