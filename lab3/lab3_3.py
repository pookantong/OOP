def is_plusone_dictionary(d):
    pass
def calc_average_score(data):
    score = ["{:.2f}".format(elem) for elem in [sum([score/len(data[x]) for score in data[x].values()]) for x in data.keys()]]
    return {[x for x in data.keys()][i] : ["{:.2f}".format(elem) for elem in [sum([score/len(data[x]) for score in data[x].values()]) for x in data.keys()]][i] for i in range(len(data))}