def swap_case(s):
    lwords = list(s)
    for i in range(len(lwords)):
        if lwords[i] == lwords[i].upper():
            lwords[i] = lwords[i].lower()
        else:
            lwords[i] = lwords[i].upper()

    return "".join(lwords)
