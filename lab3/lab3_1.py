def add_score(subject_score, subject, score):
    subject_score[subject] = score
    return subject_score
def calc_average_score(data):
    return "{:.2f}".format(sum([x/len(data) for x in data.values()]))
print(calc_average_score(add_score({ 'python' : 50 },'calculus',60)))