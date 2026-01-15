def is_incorrect(base, tolerance_pct):
    margin = base * (tolerance_pct / 100)    # 500*(2/100)=10
    return lambda amount: amount < (base - margin) or amount > (base + margin)   
    #^
    #|
    #funkcja sprawdzajaca czy ilosc napełnionej butelki nie przekracza 
    #dolnej i górnej granicy marginesu błędu tolerancji ( 10 ml - 2 % )

def f(bottles):
    incorrect_check = is_incorrect(500, 2)
    wrong_bottles = list(filter(incorrect_check, bottles)) #wybiera źle napełnione butelki
    return (len(wrong_bottles) / len(bottles)) * 100    # ilosc zke napelnionych przez ilosc butelek razy 
                                                        #100 aby wynik był w procentach 3/10*100=30                    

if __name__ == "__main__":
    bottles = [508,500,512,499,492,511,503,476,501,509]  # lista pomiarów w ml
    print(f"Incorrectly filled: {f(bottles)}%") #wydruk procentu źle napełnionych butelek z posród wszystkich

