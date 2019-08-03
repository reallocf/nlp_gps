def exactlyOneOf(lst):
    res = False
    for elem in lst:
        if res == True and elem == True:
            return False
        if elem == True:
            res = elem
    return res

def uniquenessTest(listOfDescription):
    assert(len(set(listOfDescription)) == len(listOfDescription))
