def f(word):
    wave = []
    i = 0
    wynik = ""
    

    while 0 < len(word):

        wave.append(list(word))
        wave[i] = "-".join(wave)

        wave[i][i] = wave[i][i].upper()

        i+=i

    

    return "-".join(wave)

if __name__ == "__main__":
    print(f"water")
