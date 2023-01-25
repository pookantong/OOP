def add_score(subject_score, subject, score):
    subject_score[subject] = score
    return subject_score
def calc_average_score(data):
    return f'{sum(data.values())/len(data):.2f}'
print(add_score({ 'python' : 50, 'calculus' : 60 },'oop',42))
print(calc_average_score(add_score({ 'python' : 50, 'calculus' : 60 },'oop',42)))