def is_plusone_dictionary(d):
    for i in range(1,len(d)):
        list = [x for x in d.keys()]
        if list[i] != [x for x in d.values()][i] - 1 or list[i] != i*2+list[0]:
            return False
    return True
print(is_plusone_dictionary({1:2, 3:4, 5:6, 7:8}))