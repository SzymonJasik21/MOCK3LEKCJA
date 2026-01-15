def f(countries):
    # Wersja "wszystko w jednym" z filter i map
    return list(map(lambda c: f"{c['country']}: {c['gold']},{c['silver']},{c['bronze']}", filter(lambda c: (c["gold"] + c["silver"] + c["bronze"]) >= 10, countries)))

if __name__ == "__main__":
    data = [
        {"country":"Denmark","gold":2,"silver":4,"bronze":6},
        {"country":"Finland","gold":5,"silver":0,"bronze":4},
        {"country":"USA","gold":12,"silver":5,"bronze":11},
        {"country":"Peru","gold":0,"silver":1,"bronze":7}
    ]

    print("\n".join(f(data)))

    # "\n" pełni role separatora co ma zostać wstawione między elementy listy podczas 
    # łączenia ich w jeden string (ma przejsc do nowej linii) co powoduje własnie ta funkcja ( \n)


    #return list(map(lambda c: f"{c["country"]}: {c["gold"]}, {c["silver"]}, {c["bronze"]}", filter(lamda c: (c["gold"]) + c["silver"] + c["bronze"] >= 10, countries)))