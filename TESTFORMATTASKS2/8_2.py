def f(test_results):
    # list(x.values()) bierze wartości [imię, wynik]
    # [1] wybiera drugą wartość, czyli wynik
    return list(filter(lambda x: list(x.values())[1] >= 50 and list(x.values())[1] <= 70, test_results))

if __name__ == "__main__":
    results = [
        {"name": "Peter", "result": 27},
        {"name": "Anna", "result": 63},
        {"name": "Robert", "result": 92},
        {"name": "Paul", "result": 46},
        {"name": "Barbara", "result": 52}]
    print(f(results))

    # Przekształcony kod na używanie indeksu do odczytu danych do zadania
    # ( "name" : "Barbara" ---> [0] ) , ( "result": 52 ---> [1] )
