def add_score(subject_score, student, subject, score):
    if subject_score.get(student):
        subject_score[student].update({subject : score})
    else:
        subject_score.update({student : {subject : score}})
    return subject_score    
def calc_average_score(data):
    return {i : f'{sum(data[i].values())/len(data[i]):.2f}' for i in data}
print(add_score({ '65010895' : { 'python' : 50 }, '65010896' : {'python': 80, 'calculus': 90} },'65010895','calculus',60))
print(calc_average_score(add_score({ '65010895' : { 'python' : 50 }, '65010896' : {'python': 80, 'calculus': 90} },'65010895','calculus',60)))