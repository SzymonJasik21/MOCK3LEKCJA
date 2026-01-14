def f(countries):
    is_at_least_10 = lambda c: (c["gold"] + c["silver"] + c["bronze"]) >= 10
    filtered = filter(is_at_least_10, countries)
    return list(map(lambda c: f"{c['country']}: {c['gold']},{c['silver']},{c['bronze']}", filtered))

if __name__ == "__main__":
    data = [
        {"country":"Denmark","gold":2,"silver":4,"bronze":6},
        {"country":"Finland","gold":5,"silver":0,"bronze":4},
        {"country":"USA","gold":12,"silver":5,"bronze":11},
        {"country":"Peru","gold":0,"silver":1,"bronze":7}
    ]
    print("\n".join(f(data)))