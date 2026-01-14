class C:
    def __init__(self, name, surname, age, seniority):
        self.name = name
        self.surname = surname
        self.age = age
        self.seniority = seniority

    def __str__(self):
        res = f"{self.surname}{self.name[0]}{self.seniority}"
        return res.upper() if self.age >= 18 else res.lower()

if __name__ == "__main__":
    print(str(C("Anna", "May", 17, 7)))
    print(str(C("George", "Brown", 21, 4)))