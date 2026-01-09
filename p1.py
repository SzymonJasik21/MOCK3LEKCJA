def f(word):
    if not word:
        return ""

    wave = []

    for i in range(len(word)):
        wrd = word[:i].lower() + word[i].upper() + word[i+1:].lower()
        wave.append(wrd)

    return "-".join(wave)

if __name__ == "__main__":
    print(f"water")
