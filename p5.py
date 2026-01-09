import re

def f(mnumbers):
    pattern = r"^[+-]?[1-7a-dA-D]+$" 

    count = 0
    for i in mnumbers:
        if re.match(pattern,i):
            count += 1
    return count 

if __name__ == "__main__":
    print(f(["A15","-31","7abC","+D1","-g4"]))
