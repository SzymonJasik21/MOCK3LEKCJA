def f(data):
    # Dla każdego wyrazu tworzymy nową listę liter, 
    # zmieniając na dużą te, których indeks jest parzysty
    return list(map(lambda word: "".join([char.upper() if i % 2 == 0 else char for i, char in enumerate(word)]), data))

if __name__ == "__main__":
    words = ["python", "java"]
    print(f(words))