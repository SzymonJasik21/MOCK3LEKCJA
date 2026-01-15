import matplotlib.pyplot as plt

def f(data):
    countries = list(map(lambda x: x["country"], data))
    total_medals = list(map(lambda x: x["gold"] + x["silver"] + x["bronze"], data))

    return countries, total_medals
    
    #plt.bar(countries, total_medals)
    #plt.title("Olympic Medals")
    #plt.xlabel("Countries")
    #plt.ylabel("Total Medals")
    #plt.show()

if __name__ == "__main__":
    olympics = [
        {"country":"Denmark","gold":2,"silver":4,"bronze":6},
        {"country":"Finland","gold":5,"silver":0,"bronze":4},
        {"country":"USA","gold":12,"silver":5,"bronze":11},
        {"country":"Peru","gold":0,"silver":1,"bronze":7}
    ]

    countries, total_medals = f(olympics)

    plt.bar(countries, total_medals)
    plt.title("Olympic Medals")
    plt.xlabel("Countries")
    plt.ylabel("Total Medals")
    plt.show()

   

    