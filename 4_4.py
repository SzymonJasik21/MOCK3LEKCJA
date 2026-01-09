def f(fnc, res):
    # Filter the results according to the criteria in fnc
    filtered_res = [x for x in res if fnc(x)]
    
    # If no results meet the criteria, return 0
    if not filtered_res:
        return 0
    
    # Return the difference between the highest and lowest result
    return max(filtered_res) - min(filtered_res)

if __name__ == "__main__":
    # Test cases from image
    res = [95, 90, 20, 50, 70]
    
    fnc1 = lambda x: x > 50
    print(f(fnc1, res))  # Filtered: [95, 90, 70] -> 95 - 70 = 25
    
    fnc2 = lambda x: x > 30 and x < 90
    print(f(fnc2, res))  # Filtered: [50, 70] -> 70 - 50 = 20