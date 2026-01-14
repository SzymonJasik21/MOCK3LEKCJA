def f(data):
    return list(filter(lambda x: x % 2 == 0 and x % 3 == 0, data))

if __name__ == "__main__":
    numbers = list(range(1, 21))
    print(f(numbers))