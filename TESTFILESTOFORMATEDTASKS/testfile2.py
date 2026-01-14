def f(data):
    # Metoda .replace(stare, nowe) zamienia znaki
    return list(map(lambda x: x.replace('e', 'E'), data))

if __name__ == "__main__":
    words = ["apple", "lemon", "orange"]
    print(f(words))