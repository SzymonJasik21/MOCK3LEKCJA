def f(word):

    wave = []
    for i in range(len(word)):
        litery = list(word.lower())
        litery[i] = litery[i].upper()
        wave.append("".join(litery))
    
    return "-".join(wave)

if __name__ == "__main__":
    print(f("water"))
    print(f("a"))
    print(f(""))