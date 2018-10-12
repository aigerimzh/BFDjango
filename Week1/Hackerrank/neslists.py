if __name__ == '__main__':
    students = []
    s = []
    n = int(input())
    students = [[input(), float(input())] for x in range(n)]

    #print(students)
    s = list(set([s for n, s in students]))
    sh = sorted(s)[1]
    #print (sh)
    r = (n for n, s in students)
    print ("\n".join([n for n, s in sorted(students) if s == sh]))
