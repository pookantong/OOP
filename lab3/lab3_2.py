def add_score(subject_score, student, subject, score):
    if subject_score.get(student):
        subject_score[student].update({subject : score})
    else:
        subject_score.update({student : {subject : score}})
    return subject_score
def calc_average_score(data):
    return {[x for x in data.keys()][i] : ["{:.2f}".format(elem) for elem in [sum(data[x].values())/len(data[x]) for x in data.keys()]][i] for i in range(len(data))}
print(add_score({ '65010895' : { 'python' : 50 }, '65010896' : {'python': 80, 'calculus': 90} },'65010895','calculus',60))
print(calc_average_score(add_score({ '65010895' : { 'python' : 50 }, '65010896' : {'python': 80, 'calculus': 90} },'65010895','calculus',60)))