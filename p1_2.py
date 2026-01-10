def f(word):
    if not word:
        return ""
    
    wave = []
    word = word.lower()
    
    for i in range(len(word)):
        current_variation = word[:i] + word[i].upper() + word[i+1:]
        wave.append(current_variation)
    
    return "-".join(wave)

print(f"water: {f('water')}")
print(f"a: {f('a')}")
print(f"pusty ciąg: {f('')}")