def is_incorrect(base, tolerance_pct):
    margin = base * (tolerance_pct / 100)
    return lambda amount: amount < (base - margin) or amount > (base + margin)

def f(bottles):
    incorrect_check = is_incorrect(500, 2)
    wrong_bottles = list(filter(incorrect_check, bottles))
    return (len(wrong_bottles) / len(bottles)) * 100

if __name__ == "__main__":
    bottles = [508,500,512,499,492,511,503,476,501,509]
    print(f"Incorrectly filled: {f(bottles)}%")