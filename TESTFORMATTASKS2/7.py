import matplotlib.pyplot as plt

def f(data):
    cities = list(map(lambda x: x, data.keys()))
    temps = list(map(lambda x: x, data.values()))
    return cities, temps

if __name__ == "__main__":
    measurements = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}
    labels, values = f(measurements)
    plt.bar(labels, values)
    plt.title("Temperatures in Cities")
    plt.xlabel("Cities")
    plt.ylabel("Celsius")
    plt.show()