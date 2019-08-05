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

def invertMap(regMap):
    invMap = {}
    for key in regMap.keys():
        keySet = set()
        for otherKey, val in regMap.items():
            if key in val:
                keySet.add(otherKey)
        invMap[key] = keySet
    return invMap

def largest(key, val, existingVal): 
    return existingVal == None or len(val) > len(existingVal)

def smallest(key, val, existingVal):
    return existingVal == None or len(val) < len(existingVal)

def largestNotInBuilding(key, val, existingVal):
    return "in" not in key and largest(key, val, existingVal)