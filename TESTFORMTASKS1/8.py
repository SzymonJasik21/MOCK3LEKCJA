class C:
    def __init__(self, sectors):
        self.sectors = sectors

    def m1(self, s, n):
        self.sectors[s] = n

    def m2(self, s):
        total = 0
        for char in s:
            if char in self.sectors:
                total += self.sectors[char]
        return total

if __name__ == "__main__":
    obj = C({"A": 120, "D": 150, "G": 90, "K": 110})
    obj.m1("G", 130)
    print(obj.m2("GD"))
    print(obj.m2("KEJ"))