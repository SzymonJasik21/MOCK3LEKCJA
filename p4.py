def f(fnc, res):
    filtered_results = []
    
    for x in res:
        if fnc(x):
            filtered_results.append(x)
            
    if not filtered_results:
        return 0
        
    #highest = max(filtered_results)
    #lowest = min(filtered_results)
    
    #return highest - lowest
    return max(filtered_results) - min(filtered_results)

if __name__ == "__main__":
    res = [95, 90, 20, 50, 70]
    fnc1 = lambda x: x > 50
    print(f(fnc1, res))
    fnc2 = lambda x: x>30 and x<90
    print(f(fnc2, res))