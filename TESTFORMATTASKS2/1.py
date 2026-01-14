def f(data):
    return list(map(lambda x: x**3, data))

if __name__ == "__main__":
    #numbers = list(range(1, 21))
    #print(f(numbers))

    print(f(list(range(1, 21))))