if __name__ == '__main__':
    n = int(input())
    studentMarks = {}
    for _ in range(n):
        line = input().split()
        studentMarks[line[0]] = [
            float(line[1]), float(line[2]), float(line[3])]

    q = input()
    if q in studentMarks:
        print("{:0.2f}".format(
            (studentMarks[q][0]+studentMarks[q][1]+studentMarks[q][2])/3))
