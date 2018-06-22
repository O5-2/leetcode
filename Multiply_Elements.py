def eval(element1, element2):
    """
    :type element1: string
    :type element2: string
    :rtype: string
    """
    if element1[1] == element2[1]:
        return element1[:2] + str(int(element1[2:]) + int(element2[2:]))
    else:
        if element1[2:] == element2[2:]:
            return []
        elif abs(int(element1[2:])) > abs(int(element2[2:])):
            return [element1[0]+element1[1]+ str(int(element1[2:])-int(element2[2:]))]
        else:
            return [element2[0]+element2[1]+ str(int(element2[2:])-int(element1[2:]))]

def evalElements(elements1, elements2):
    """
    :type elements1: List[string]
    :type elements2: List[string]
    :rtype: List[string]
    """
    while elements1[-1][0] == elements2[0][0]:
        elements1 = elements1[:-1] + eval(elements1[-1], elements2[0])
        elements2 = elements2[1:]
        if (len(elements1) == 0) or (len(elements2) == 0):
            break
    return elements1+elements2

one = ["a+1","b+2"]
two = ["b-2","a-6"]

print evalElements(one, two)
