def add_score(subject_score, subject, score):
    subject_score[subject].update(score)
    return subject_score
def calc_average_score(data):
    return "{:.2f}".format(sum(data.values())/len(data))
print(add_score({ 'python' : 50, 'calculus' : 60 },'oop',42))
print(calc_average_score(add_score({ 'python' : 50, 'calculus' : 60 },'oop',42)))