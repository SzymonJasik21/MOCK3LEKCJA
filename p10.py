def f(value1):
    def g(value2):
        return value1 * value2
    return g

if __name__ == "__main__":
    times_five = f(5)
    print(times_five(8))
    
    times_three = f(3)
    print(times_three(7))