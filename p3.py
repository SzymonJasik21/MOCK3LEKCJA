def f(d):

    passengers = 0

    for key,value in d.items():

        passengers += value 

    average = passengers // len(d)

    counter = 0

    for key,value in d.items():

        if value > average:

            counter += 1

    return counter



if __name__ == "__main__":
    print(f({"LO231":150,"BA787":120,"NZ15":30}))