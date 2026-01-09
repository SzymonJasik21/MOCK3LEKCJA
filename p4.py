def f(fnc,res):

    reslist = [x for x in res if fnc(x)]

    if not reslist:
        return 0    

    return max(reslist) - min(reslist)


if __name__ == "__main__":
    res = [95,90,20,50,70]

    fnc1 = lambda x: x>50 
    print(f(fnc1, res)) 

    fnc2 = lambda x: x>30 and x<90 
    print(f(fnc1, res)) 
