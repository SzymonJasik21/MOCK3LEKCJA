def f(employees):
    return list(map(lambda x: f"{x[0].upper()}, {x[1]}", employees))

if __name__ == "__main__":
    data = [("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),("Jackson","Peter")]
    print(f(data))