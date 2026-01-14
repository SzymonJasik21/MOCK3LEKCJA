import random

class Thermometer:
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def measure(self):
        return round(random.uniform(34.0, 42.0), 1)

    def display(self, temp):
        msg = f"Temperature: {temp}C"
        if temp >= 41.0:
            msg += " (CRITICAL TEMPERATURE!!)"
        elif temp >= 37.0:
            msg += " (fever)"
        return msg

if __name__ == "__main__":
    t = Thermometer()
    t.turn_on()
    temp = t.measure()
    print(t.display(temp))