def min_pts(limit):
    return lambda pts: pts >= limit

def f(results, limit):
    return list(filter(min_pts(limit), results))

if __name__ == "__main__":
    results = [37,51,44,23,78,92,39,84,83,51]
    print(f"Min 70 pts: {f(results, 70)}")
    print(f"Min 40 pts: {f(results, 40)}")
    print(f"Min 30 pts: {f(results, 30)}")