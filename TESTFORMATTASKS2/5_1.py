def min_pts(limit):
    def check(pts):
        return pts >= limit
    return check

def f(results, limit):
    return list(filter(min_pts(limit), results))

if __name__ == "__main__":
    results = [37, 51, 44, 23, 78, 92, 39, 84, 83, 51]
    
    print(f"Min 70 pts: {f(results, 70)}")
    print(f"Min 40 pts: {f(results, 40)}")
    print(f"Min 30 pts: {f(results, 30)}")

    #Druga opcja kodu bez uzycia lambdy na poczatku z zdefiniowaniem sprawdzania punktów 