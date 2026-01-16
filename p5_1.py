import re

def f(mnumbers):
    pattern = r"^[+-]?[1-7a-dA-D]+$"
    return sum(1 for i in mnumbers if re.match(pattern, i))

if __name__ == "__main__":
    print(f(["A15","-31","7abC","+D1","-g4"]))
    print(f(["A05","-3+1","7ab8C","+Bb7","-22c55"]))