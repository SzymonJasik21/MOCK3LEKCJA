import statistics

class Statistics:
    def __init__(self):
        self.numbers = []

    def add_number(self, n):
        self.numbers.append(n)

    def get_max(self):
        return max(self.numbers) if self.numbers else None

    def get_mean(self):
        return sum(self.numbers) / len(self.numbers) if self.numbers else 0

    def get_median(self):
        return statistics.median(self.numbers) if self.numbers else 0

if __name__ == "__main__":
    s = Statistics()
    for n in [12, 37, 6, 9, 17]:
        s.add_number(n)
    print(f"Max: {s.get_max()}, Mean: {s.get_mean()}, Median: {s.get_median()}")