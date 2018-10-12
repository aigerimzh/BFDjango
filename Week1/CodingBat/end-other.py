def end_other(a, b):
    al = a.lower()
    bl = b.lower()
    if al.endswith(bl) or bl.endswith(al):
        return True
    return False
