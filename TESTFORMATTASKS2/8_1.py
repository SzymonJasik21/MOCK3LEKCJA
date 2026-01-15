def f(test_results):
    return list(filter(lambda x: x["result"] >= 50 and x["result"] <= 70, test_results))

if __name__ == "__main__":
    results = [
        {"name": "Peter", "result": 27},
        {"name": "Anna", "result": 63},
        {"name": "Robert", "result": 92},
        {"name": "Paul", "result": 46},
        {"name": "Barbara", "result": 52}]
    print(f(results))

    # Druga opcja kodu z uzyciem funkcji and w lambdzie