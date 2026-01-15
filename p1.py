def f(word):

    result = []
    for i in range(len(word)):
        chars = list(word.lower())
        chars[i] = chars[i].upper()
        result.append("".join(chars))
    
    return "-".join(result)

if __name__ == "__main__":
    print(f("water"))
    print(f("a"))
    print(f(""))