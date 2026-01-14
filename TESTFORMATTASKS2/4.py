def f(scores):
    def calculate_score(judges_score):
        return sum(judges_score) - min(judges_score) - max(judges_score)
    
    return list(map(calculate_score, scores))

if __name__ == "__main__":
    #ratings = [(17,15,16,17,15), (16,18,19,17,19), (19,15,15,19,18), (18,17,19,15,16)]
    #print(f(ratings))

    print(f([(17,15,16,17,15), (16,18,19,17,19), (19,15,15,19,18), (18,17,19,15,16)]))

