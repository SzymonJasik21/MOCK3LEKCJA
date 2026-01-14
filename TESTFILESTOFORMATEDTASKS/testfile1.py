def f(data):
    # x[0] to 1. litera, x[1].upper() to 2. litera, x[2:] to reszta wyrazu
    return list(map(lambda x: x[0] + x[1].upper() + x[2:] if len(x) > 1 else x, data))

if __name__ == "__main__":
    words = ["smith", "jones", "lee"]
    print(f(words))