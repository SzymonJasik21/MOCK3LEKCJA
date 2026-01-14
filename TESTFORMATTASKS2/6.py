def f(data):
    cities = filter(lambda x: data[x] > 0, data)
    return " ".join(cities)

if __name__ == "__main__":
    temps = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}
    print(f"Cities with positive temperatures: {f(temps)}")